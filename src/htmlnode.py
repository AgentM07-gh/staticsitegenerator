class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented("to_html not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        prop_str = ""
        for prop in self.props:
            prop_str += f' {prop}="{self.props[prop]}"'
        return prop_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, Children: {self.children}, {self.props})"