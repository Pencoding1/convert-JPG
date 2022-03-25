from PIL import Image
import os, glob
import sys

def convert(first, seccond):
    for infile in glob.glob(f"images/*.{first}"):
        file,ext = os.path.splitext(infile)
        file = file.replace("images\\", "")
        with Image.open(infile).convert('RGB') as im:
            im.save(f"result\\{file}" + f'.{seccond}', quality = 100)
if __name__ == "__main__":
    TYPE_NAME = ['png','jpg','jpeg','webp']
    type_name = [i.lower() for i in input("Enter the type name you want to convert to(separated by commas): ").split(",")]
    if type_name[0] not in TYPE_NAME or type_name[1] not in TYPE_NAME:
        raise Exception("Type name is not exist or this moudule doesn't support")
    else:
        first, seccond = type_name[0], type_name[1]
        convert(first,seccond)