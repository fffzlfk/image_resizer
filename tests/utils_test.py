import unittest
import pic_resizer.utils as utils


class UtilsTest(unittest.TestCase):
    def test_parse_file_size(self):
        got = utils.parse_file_size("1k")
        self.assertEqual(1000, got)
        got = utils.parse_file_size("01")
        self.assertIsNone(got)
        got = utils.parse_file_size("100M")
        self.assertEqual(100 * 1000**2, got)

    def test_filepath2basename_without_extension(self):
        got = utils.filepath2basename_without_extension("/home/fffzlfk/a/b.png")
        self.assertEqual("b", got)


if __name__ == "__main__":
    unittest.main()
