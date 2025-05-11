import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        leaf1 = LeafNode(tag="h1", 
                         value="This is a heading")
        
        self.assertEqual(leaf1.to_html(), '"<h1>This is a heading<h1>"')

        leaf2 = LeafNode(tag="h2", value=None)
        
        self.assertRaises(ValueError, leaf2.to_html)

        leaf3 = LeafNode(tag=None, value="Only text")

        self.assertEqual(leaf3.to_html(), "Only text")

        leaf4 = LeafNode(tag="a",
                        value="Click here",
                        props={
                            "href": "https://example.com",
                            "class": "button",
                            "data-tooltip": "Visit our website",
                            "rel": "noopener noreferrer"
                        })
        
        self.assertEqual(leaf4.to_html(), '"<a href="https://example.com" class="button" data-tooltip="Visit our website" rel="noopener noreferrer">Click here<a>"')




