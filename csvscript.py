f = open("./fonts.csv", "w")

f.write("index,name,path\n")

import os
index = 0
def add_fonts(path):
    global index
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".ttf") or file.endswith(".otf"):
                f.write(",".join([str(index), file[:len(file) - 4], root + "/" + file]) + "\n")
                index += 1
                print(file)

add_fonts("./fonts")

f.close()