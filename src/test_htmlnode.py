import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHMTLNode(unittest.TestCase):
    '''
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
        )'
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_img(self):
        node = LeafNode("img", "my picture", {"src": "www.pics.com/pic.jpg"})
        self.assertEqual(node.to_html(), '<img src="www.pics.com/pic.jpg">my picture</img>')
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "mylink", {"href": "www.linksrus.com/mylink"})
        self.assertEqual(node.to_html(), '<a href="www.linksrus.com/mylink">mylink</a>')
    
    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, world!")
        self.assertEqual(node.to_html(), "<div>Hello, world!</div>")'
    '''

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_multi_children(self):
        child_node1 = LeafNode("span", "child")
        child_node2 = LeafNode("b", "bchild2")
        child_node3 = LeafNode("i", "ichild3")
        parent_node = ParentNode("div", [child_node1, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><b>bchild2</b><i>ichild3</i></div>")
    
    def test_to_html_with_multi_grandchildren(self):
        grandchild_node1 = LeafNode("b", "grandchild1")
        grandchild_node2 = LeafNode("i", "grandchild2")
        grandchild_node3 = LeafNode("p", "grandchild3")
        child_node = ParentNode("span", [grandchild_node1, grandchild_node2, grandchild_node3])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b><i>grandchild2</i><p>grandchild3</p></span></div>",)