import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        node4 = TextNode("This is an image node", TextType.IMAGE, "image.png")

        self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node3)
        self.assertNotEqual(node1, node4)

if __name__=="__main__":
    unittest.main()