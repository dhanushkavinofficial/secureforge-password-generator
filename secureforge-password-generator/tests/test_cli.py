import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from secureforge.cli import main


class TestCLI(unittest.TestCase):
    def run_cli(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = main(list(args))
        return code, out.getvalue(), err.getvalue()

    def test_quiet_output(self):
        code, out, _ = self.run_cli("-l", "32", "-q")
        self.assertEqual(code, 0)
        self.assertEqual(len(out.strip()), 32)

    def test_count(self):
        code, out, _ = self.run_cli("-l", "24", "-c", "3", "-q")
        self.assertEqual(code, 0)
        self.assertEqual(len(out.strip().splitlines()), 3)

    def test_bad_length(self):
        code, _, err = self.run_cli("-l", "5", "-q")
        self.assertEqual(code, 1)
        self.assertIn("Error", err)


if __name__ == "__main__":
    unittest.main()
