from PIL import Image
import os
import shutil
from helpers import sizeCalculator

userName = os.path.expanduser('~')
pathName = '\Downloads'
downloadsFolder = userName + pathName
softwareFolder = "G:\Documents\Software" #Destination directory
totalSize = 0

if __name__ == "__main__":
  
  for filename in os.listdir(downloadsFolder):
    name, extension = os.path.splitext(f"{downloadsFolder}\{filename}")
    fileSize = os.path.getsize(f"{downloadsFolder}\{filename}")
    
    if extension in [".exe"]:
      fileName = f"{name}{extension}"
      # print(fileName)
      fileSize = os.path.getsize(fileName)
      fileN = fileName.split("\\")
      copyDirectory = shutil.copy(fileName, softwareFolder) #shutil copy files to the new directory
      print(f"Nombre del archivo: 💾 {fileN[4]}\t\t [Peso: {sizeCalculator.convert_size(fileSize)}] Copiado =====> {softwareFolder}")
      totalSize += fileSize
  
  print( "\n 🗂️ Peso total de los archivos copiados: " + sizeCalculator.convert_size(totalSize))