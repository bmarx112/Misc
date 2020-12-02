import os

while True:

    st = input("Enter Directory Path:")
    if st == "": break

    i = 0
    try:
        os.chdir(st)
        for root, dirs, files in os.walk(".", topdown = False):
            for name in files:
                if name.endswith(".bak"):
                    os.remove(os.path.join(root, name))
                    i += 1
                #print(os.path.join(root, name))
        print(i,"files removed.")
    except Exception as e:
        print(st,"is an invalid directory. Please enter proper directory path.")
        print("Error:",e)
