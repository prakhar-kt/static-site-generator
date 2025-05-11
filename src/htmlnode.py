

class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        string_attribute = ""
        if self.props is not None:
            for key, value in self.props.items():
                string_attribute += f' {key}="{value}"'
        return string_attribute    
    
    
    def __repr__(self) -> str:
        return f"HtmlNode({self.tag},{self.value}, {self.children}, {self.props_to_html()})"