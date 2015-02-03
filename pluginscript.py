import os
import zipfile

folderdir = input("Enter the directory of the folder you want to convert. ")
type = input("Enter the type to convert to. Use 'game', 'trans', or 'theme'")
def zip(path, zip):
    for root, dirs, files in os.walk(folderdir):
        for file in files:
            zip.write(os.path.join(root, file))


if __name__ == '__main__':
    if type == "game":
        zipf = zipfile.ZipFile(os.path.basename(folderdir[:-1]) + '.rngame', 'w')
    elif type == "trans":
        zipf = zipfile.ZipFile(os.path.basename(folderdir[:-1]) + '.rntrans', 'w')
    elif type == "theme":
        zipf = zipfile.ZipFile(os.path.basename(folderdir[:-1]) + '.rntheme', 'w')
    else:
        print("That isn't a valid type.")
    zipdir = ('tmp/', zipf)
    zipf.close()


