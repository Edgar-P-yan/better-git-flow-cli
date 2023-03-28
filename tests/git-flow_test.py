import unittest
from helpers import import_path, Case

gitflow = import_path("git-flow")


class TestGitFlow(unittest.TestCase):

    def test_semverAddPatch(self):
        cases = [
            Case("1.0", "1.1"),
            Case("1.0.1", "1.0.2"),
            Case("1", "2"),
            Case("v1.1234.999", "v1.1234.1000")
        ]

        for case in cases:
            self.assertEqual(gitflow.semverAddPatch(case.input), case.want)

    def test_exec(self):
        self.assertEqual(gitflow.exec("echo hello").strip(), "hello")

if __name__ == '__main__':
    unittest.main()
