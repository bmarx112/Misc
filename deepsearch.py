import os
import re

while True:
    st = input("Enter Directory Path: ")
    if st == "": break

    try:
        os.chdir(st)

    except Exception as e:
        print(st,"is an invalid directory. Please enter proper directory path.")
        print("Error:",e)
        break

    term = input("Enter Search Term: ")
    if term == "": break

    bad_ext, match = [],[]

    for root, dirs, files in os.walk(st):
        for file in files:
            path = os.path.join(root, file)

            try:
                ext = re.findall('\.[^.]+$',str(path))[0]
            except: continue

            if ext in bad_ext: continue
            else:
                try:
                    fread = open(path).read()
                    if term in fread: match.append(str(path))
                except:
                    bad_ext.append(re.findall('\.[^.]+$',str(path))[0])
                    #print(bad_ext)
                    continue

    print(bad_ext)
    if len(match)>0:
            for i in match:
                print(i)
    else: print("No results found in scannable files.")
