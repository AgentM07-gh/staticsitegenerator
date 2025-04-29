import os
from blockmd import markdown_to_html_node

def extract_title(markdown):
    header = ""
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            header = line.lstrip("#").strip()
    if header == "":
        raise Exception("No H1 header available")
    return header

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if os.path.exists(from_path):
        with open(from_path, 'r') as file:
            markdown = file.read()
    print(markdown) 
    if os.path.exists(template_path):
        with open(template_path, 'r') as file:
            template = file.read()
    print(template)
    html_node = markdown_to_html_node(markdown)
    print(html_node.__repr__())
    html_string = html_node.to_html()
#    print(html_string)
    title = extract_title(markdown)
#    print(title)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)
#    print(template)
    dirs = os.path.dirname(dest_path)
    if dirs and not os.path.exists(dirs):
        os.makedirs(dirs)
    with open(dest_path, "w") as file:
        file.write(template)

    
    



