filename = input("Input the Filename: ")
parts = filename.split(".")
extension = parts[-1]
print("The extension of the file is: '{}'".format(extension))
