f = open("./fonts.csv", "w")

f.write("index,name,path,encoding\n")

import os
index = 0
def add_fonts(path, encoding):
    global index
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".ttf"):
                f.write(",".join([str(index), file[:len(file) - 4], root + "/" + file, encoding]) + "\n")
                index += 1
                print(file)

add_fonts("./fonts/Adobe", "ADOB")
add_fonts("./fonts/JIS", "sjis")

f.close()