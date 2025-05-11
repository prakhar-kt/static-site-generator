import unittest

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):

    def test_props_to_html(self):
        node1 = HtmlNode(tag= "h1", 
                         value="This is a heading",
                         props = {
                            "href": "https://www.google.com",
                            "target": "_blank",
                          })
        
        prop_string1 = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node1.props_to_html(), prop_string1)
        
        # Node 2: An image with src and alt attributes
        node2 = HtmlNode(tag="img",
                        value=None,
                        props={
                            "src": "https://example.com/image.jpg",
                            "alt": "Example Image",
                            "class": "responsive-image"
                        })
        
        prop_string2 = ' src="https://example.com/image.jpg" alt="Example Image" class="responsive-image"'
        self.assertEqual(node2.props_to_html(), prop_string2)
        
        # Node 3: A paragraph with styling
        node3 = HtmlNode(tag="p",
                        value="This is a styled paragraph",
                        props={
                            "class": "text-primary",
                            "style": "font-size: 16px; color: blue;",
                            "id": "main-paragraph"
                        })
        
        prop_string3 = ' class="text-primary" style="font-size: 16px; color: blue;" id="main-paragraph"'
        self.assertEqual(node3.props_to_html(), prop_string3)
        
        # Node 4: A link with multiple attributes
        node4 = HtmlNode(tag="a",
                        value="Click here",
                        props={
                            "href": "https://example.com",
                            "class": "button",
                            "data-tooltip": "Visit our website",
                            "rel": "noopener noreferrer"
                        })
        
        prop_string4 = ' href="https://example.com" class="button" data-tooltip="Visit our website" rel="noopener noreferrer"'
        self.assertEqual(node4.props_to_html(), prop_string4)
        
