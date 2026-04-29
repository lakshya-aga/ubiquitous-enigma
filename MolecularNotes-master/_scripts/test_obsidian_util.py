import unittest


from obsidian_util import extract_wikilinks


class TestExtractWikilinks(unittest.TestCase):
    def test_supports_cplusplus(self):
        self.assertEqual(extract_wikilinks("See [[C++]] for details."), ["C++"])

    def test_strips_alias_heading_and_block(self):
        text = "Links: [[C++#Templates|tmpl]] and [[Foo^bar|baz]]"
        self.assertEqual(extract_wikilinks(text), ["C++", "Foo"])


if __name__ == "__main__":
    unittest.main()

