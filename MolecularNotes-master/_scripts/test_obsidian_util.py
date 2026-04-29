import unittest


from obsidian_util import extract_wikilinks, has_obsidian_tag


class TestExtractWikilinks(unittest.TestCase):
    def test_supports_cplusplus(self):
        self.assertEqual(extract_wikilinks("See [[C++]] for details."), ["C++"])

    def test_strips_alias_heading_and_block(self):
        text = "Links: [[C++#Templates|tmpl]] and [[Foo^bar|baz]]"
        self.assertEqual(extract_wikilinks(text), ["C++", "Foo"])


class TestHasObsidianTag(unittest.TestCase):
    def test_matches_type_line(self):
        self.assertTrue(has_obsidian_tag("Type: #topic\n", "#topic"))

    def test_matches_inline_tag(self):
        self.assertTrue(has_obsidian_tag("Some text #topic more text", "#topic"))

    def test_matches_hierarchical_tag(self):
        self.assertTrue(has_obsidian_tag("Some text #topic/sub more text", "#topic"))

    def test_is_case_insensitive(self):
        self.assertTrue(has_obsidian_tag("Type: #Topic\n", "#topic"))

    def test_ignores_fenced_code_blocks(self):
        text = "```python\n#topic\n```\nOutside"
        self.assertFalse(has_obsidian_tag(text, "#topic"))

    def test_matches_frontmatter_tags_list(self):
        text = "---\ntags: [topic, other]\n---\nBody"
        self.assertTrue(has_obsidian_tag(text, "#topic"))

    def test_matches_frontmatter_type(self):
        text = "---\ntype: topic\n---\nBody"
        self.assertTrue(has_obsidian_tag(text, "#topic"))

    def test_does_not_match_unrelated(self):
        self.assertFalse(has_obsidian_tag("Type: #author\n", "#topic"))


if __name__ == "__main__":
    unittest.main()
