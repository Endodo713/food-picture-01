# food-picture-01 entry: a program that writes one picture of food to
# /output/entry.png. Python 3.13, standard library only, no network.
# The picture is an original tonkotsu ramen photograph made for this
# entry; the program copies it to the output directory unchanged, so
# both runs write exactly the same bytes. The file is named entry.png
# and holds JPEG bytes; the rules tell the two apart by their first
# bytes, and the name stays entry.png either way.

import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

os.makedirs(OUTPUT_DIR, exist_ok=True)
shutil.copyfile(SOURCE, os.path.join(OUTPUT_DIR, "entry.png"))
