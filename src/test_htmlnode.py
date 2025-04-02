import unittest
from htmlnode import HTMLNode

class TestHMTLNode(unittest.TestCase):

    def test_HTMLNode_basic(self):
        node = HTMLNode("p", "this is a paragraph", None, None)
      
        self.assertEqual(
            node.__repr__(),
           'HTMLNode(p, this is a paragraph, Children: None, None)',)

    def test_HTMLNode_children(self):
        node = HTMLNode("p", "this is a paragraph", None, {"keything": "valuething"})
      
        self.assertEqual(
            node.__repr__(),
           "HTMLNode(p, this is a paragraph, Children: None, {'keything': 'valuething'})",)

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )