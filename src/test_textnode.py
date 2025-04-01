import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_link(self):
        node = TextNode("This is a text node", TextType.LINK, "www.link.com")
        node2 = TextNode("This is a text node", TextType.LINK, "www.link.com")
        self.assertEqual(node, node2)

    def test_neq_texttype(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_neq_text(self):
        node = TextNode("This is a  node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_url(self):
        node = TextNode("This is a text node", TextType.LINK, "www.image.com")
        node2 = TextNode("This is a text node", TextType.LINK, "www.link.com")
        self.assertNotEqual(node, node2)
    
    def test_neq_url_none(self):
        node = TextNode("This is a text node", TextType.LINK, None)
        node2 = TextNode("This is a text node", TextType.LINK, "www.link.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()