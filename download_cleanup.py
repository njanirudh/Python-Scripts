import os
import mimetypes
import glob
import shutil

folder_names = ["Images","Videos","Audio","Application","Extras","Folders"]

def make_folders(path):
    for val in folder_names:
        extrasPath = os.path.join(path, val)
        os.makedirs(extrasPath, exist_ok=True)

def updateDirs(path):

    path = path
    mime = mimetypes.MimeTypes()
    fileList = glob.glob(path + "*")

    appPath = os.path.join(path, "Application")
    imgPath = os.path.join(path, "Images")
    videoPath = os.path.join(path, "Videos")
    txtPath = os.path.join(path, "Audio")
    audioPath = os.path.join(path, "Text")
    extrasPath = os.path.join(path,"Extras")
    folderPath = os.path.join(path,"Folders")

    for file in fileList:
        if(os.path.isfile(file)):
            if(mime.guess_type(file)[0] != None):
                descrete_mime = mime.guess_type(file)[0].split('/')[0]
                print(descrete_mime)

                if(descrete_mime == "application"):
                    shutil.move(file, appPath)

                elif (descrete_mime == "image"):
                    shutil.move(file, imgPath)

                elif (descrete_mime == "video"):
                    shutil.move(file, videoPath)

                elif (descrete_mime == "audio"):
                    shutil.move(file, audioPath)

                elif (descrete_mime == "text"):
                    shutil.move(file, txtPath)

                else:
                    pass

            else:
                shutil.move(file, extrasPath)

        else:
            print(os.path.basename(file))
            if((os.path.basename(file) in folder_names) == False):
                shutil.move(file, folderPath)

if __name__ == "__main__":

    downloads_path = "C:/Users/ANIRUDH/Downloads/"

    make_folders(downloads_path)
    updateDirs(downloads_path)