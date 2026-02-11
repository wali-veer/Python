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
        FileType=filePath.suffix.lower()
        DestinationDir=whichDirectroy(FileType)
        DestinationDirPath=Path("My_Practice\\Organized",DestinationDir)
        if DestinationDirPath.is_dir() != True:        
            DestinationDirPath.mkdir()

        filePath.rename(DestinationDirPath.joinpath(os.path.basename(filePath)))


organizeFileInPWD()