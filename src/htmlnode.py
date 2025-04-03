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
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None ,props)
    
    def to_html(self):
        if self.value == "":
            return ValueError("Function requires Value")
        elif self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == "":
            raise ValueError("Parent Node requires tag argument")
        elif self.children == []:
            raise ValueError("Parent Children cannot be empty")
        else:
            html_str = ""
            for child in self.children:
                html_str += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_str}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"