from os import path, listdir, mkdir, makedirs
from shutil import copy, rmtree 

def clean_copy():
    if path.exists("public"):
        rmtree("public")
    mkdir("public")
    file_list = copy_files("static")

def copy_files(directory):
        file_list = []
        for item in listdir(directory):
            item_path = path.join(directory, item)
            if directory == "static":
                dst_dir = "public"
            else:
                dst_dir = directory.replace("static", "public", 1)
            dst_dir = path.join(dst_dir, item)
#            print(f"item path : {item_path} new_dir:{dst_dir}")
            if path.isfile(item_path):
                file_list.append(item_path)
#                print(f"copy file from {item_path} to {dst_dir}")
                copy(item_path, dst_dir)
            elif path.isdir(item_path):
#                print(f"makedir: {dst_dir}")
                mkdir(dst_dir)
                file_list.extend(copy_files(item_path))
        return file_list
