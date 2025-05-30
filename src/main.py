import os
import shutil

from copyfiles import copy_files_recursive
from generatepage import generate_page


dir_path_static = "./static"
dir_path_public = "./public"



def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)
    generate_page("content/index.md", "template.html", "public/index.html")

main()