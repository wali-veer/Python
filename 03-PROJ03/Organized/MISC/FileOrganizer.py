import os
from pathlib import Path

SUBDIR = {
    "DOCUMENTS":['.pdf','.txt','.rtf'],
    "AUDIOS":['.mp3','.m4a','.m4b'],
    "IMAGES":['.jpeg','.jpg','.png'],
    "VIDEOS":['.mov','.avi','.mp4']
}

def whichDirectroy(nameOfTheFile):
    for category, suffix in SUBDIR.items():
        if nameOfTheFile in suffix:
            return category
    return "MISC"

def organizeFileInPWD():
    for item in os.scandir("My_Practice\\04-OranizeMe"):
        if item.is_dir():
            continue
        filePath = Path(item)
        print('filePath ---> ' + str(filePath))
        FileType=filePath.suffix.lower()
        print('FileType ---> ' + str(FileType))
        DestinationDir=whichDirectroy(FileType)
        print('DestinationDir  ---> ' + str(DestinationDir))
        DestinationDirPath=Path("My_Practice\\Organized",DestinationDir)
        print('DestinationDirPath ---> ' + str(DestinationDirPath))

        print('----------------------')

        if DestinationDirPath.is_dir() != True:        
            DestinationDirPath.mkdir()

        filePath.rename(DestinationDirPath.joinpath(os.path.basename(filePath)))


organizeFileInPWD()