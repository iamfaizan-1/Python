try:
    with open("sample/test2.txt",mode = 'a') as file:
    # file.write("This is a new file") # This is used to add a single line

        file.writelines(["This is the new method to add multiple lines, it accepts a list","\nThis is the second line\n"])

except FileNotFoundError as e:
    print(e)
