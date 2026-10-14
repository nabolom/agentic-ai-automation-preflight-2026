import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import preflight  # noqa: E402


class PreflightHardeningTests(unittest.TestCase):
    def init_repo(self, root: Path, remote: str) -> None:
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.name", "Test User"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=root, check=True)
        (root / "README.md").write_text("test\n", encoding="utf-8")
        subprocess.run(["git", "add", "README.md"], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "test"], cwd=root, check=True)
        subprocess.run(["git", "remote", "add", "origin", remote], cwd=root, check=True)

    def repo_check(self, root: Path):
        checks = preflight.check_git_workspace()
        return next(check for check in checks if check.name == "Repo propio")

    def test_only_template_origin_is_partial(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.init_repo(root, "https://github.com/nabolom/agentic-ai-automation-preflight-2026.git")
            with patch.object(preflight, "ROOT", root):
                self.assertEqual(self.repo_check(root).status, "PARTIAL")

    def test_different_repo_from_same_owner_is_pass(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.init_repo(root, "https://github.com/nabolom/otro-repo.git")
            with patch.object(preflight, "ROOT", root):
                self.assertEqual(self.repo_check(root).status, "PASS")

    def test_nested_workspace_does_not_inherit_parent_repo(self):
        with tempfile.TemporaryDirectory() as temp:
            parent = Path(temp)
            self.init_repo(parent, "https://github.com/student/parent.git")
            nested = parent / "downloaded-zip"
            nested.mkdir()
            with patch.object(preflight, "ROOT", nested):
                check = self.repo_check(nested)
            self.assertEqual(check.status, "BLOCKED")
            self.assertIn("dentro de otro repo", check.detail)

    def test_invalid_dataset_is_blocked_without_traceback(self):
        with tempfile.TemporaryDirectory() as temp:
            dataset = Path(temp) / "casos-minimos.json"
            dataset.write_bytes(b"[\xff")
            with patch.object(preflight, "DATASET", dataset):
                check = preflight.check_dataset()
            self.assertEqual(check.status, "BLOCKED")

    def test_malformed_origin_is_blocked_without_traceback(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.init_repo(root, "https://github.com/student/project.git")
            subprocess.run(
                ["git", "config", "remote.origin.url", "https://[invalid/audit/repo.git"],
                cwd=root,
                check=True,
            )
            with patch.object(preflight, "ROOT", root):
                check = self.repo_check(root)
            self.assertEqual(check.status, "BLOCKED")
            self.assertIn("no se pudo verificar", check.detail)

    def test_missing_git_identity_is_blocked(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)
            empty_global = root / "empty-global"
            empty_system = root / "empty-system"
            with patch.dict(
                os.environ,
                {
                    "GIT_CONFIG_GLOBAL": str(empty_global),
                    "GIT_CONFIG_SYSTEM": str(empty_system),
                    "GIT_CONFIG_NOSYSTEM": "1",
                },
                clear=False,
            ), patch.object(preflight, "ROOT", root):
                check = preflight.check_git_identity("git")
            self.assertEqual(check.status, "BLOCKED")
            self.assertIn("user.name", check.detail)

    def test_terminal_lab_practica_edicion_reversible(self):
        lab = (HERE.parent / "terminal-lab" / "README.md").read_text(encoding="utf-8")
        for fragment in (
            "## 5a. Haz un cambio temporal y recupéralo",
            "git diff -- notes/terminal-lab/prueba.txt",
            "git restore -- notes/terminal-lab/prueba.txt",
            "Si el cambio ya estuviera en un commit",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, lab)

    def test_report_next_step_matches_result(self):
        with tempfile.TemporaryDirectory() as temp:
            report = Path(temp) / "preflight-report.md"
            with patch.object(preflight, "REPORT", report):
                preflight.write_report([], "BLOCKED")
                blocked = report.read_text(encoding="utf-8")
                self.assertIn("detente", blocked)
                self.assertNotIn("crea el commit de cierre después", blocked)
                preflight.write_report([], "PARTIAL")
                self.assertIn("fallback", report.read_text(encoding="utf-8"))
                preflight.write_report([], "PASS")
                self.assertIn("crea el commit de cierre", report.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
