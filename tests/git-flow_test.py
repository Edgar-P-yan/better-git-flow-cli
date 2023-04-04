import unittest
from helpers import import_path, Case

gitflow = import_path("git-flow")


class TestGitFlow(unittest.TestCase):

    def test_semver_add_patch(self):
        cases = [
            Case("1.0", "1.1"),
            Case("1.0.1", "1.0.2"),
            Case("1", "2"),
            Case("v1.1234.999", "v1.1234.1000")
        ]

        for case in cases:
            self.assertEqual(gitflow.semver_incr_patch(case.input), case.want)

    def test_exec(self):
        self.assertEqual(gitflow.exec_cmd("echo hello").strip(), "hello")


if __name__ == '__main__':
    unittest.main()
