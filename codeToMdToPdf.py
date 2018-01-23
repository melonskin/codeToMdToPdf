import os
import subprocess
from PyPDF2 import PdfFileMerger

sourceDir = "C:\\projects\\network-csce612\\p1-web-client"
targetDir = "d:\\gdrive\\Spring2018\\csce612\\submit\\p1\\part1"
allowedExt = [".cpp", ".h"]
codeTags = {".h" : "c", ".cpp": "cpp"}
pdfFiles = []
for dirName, subdirList, fileList in os.walk(sourceDir):
    for file in fileList:
        fileName, fileExt = os.path.splitext(file)
        if fileExt in allowedExt:
            print("\t%s" % fileName)
            sourceFile = os.path.join(dirName, file)
            targetFile = os.path.join(targetDir, fileName + "_" + fileExt[1:] + ".md")
            targetPdfFile = os.path.join(targetDir, fileName + "_" + fileExt[1:] + ".pdf")
            with open(sourceFile) as inFile:
                with open(targetFile, "w") as outFile:
                    outFile.write("---\n")
                    outFile.write("geometry: margin=2cm\n")
                    outFile.write("---\n\n\n")
                    outFile.write("File name: " + file + "\n")
                    outFile.write("\n\n```" + codeTags[fileExt] + "\n")
                    outFile.writelines(inFile.readlines())
                    outFile.write("\n```" + "\n")
            cmd = "pandoc " + targetFile + " -o " + targetPdfFile
            subprocess.check_call(cmd, shell=True)
            pdfFiles.append(targetPdfFile)

merger = PdfFileMerger()

for pdf in pdfFiles:
    merger.append(pdf)

merger.write(os.path.join(targetDir, "combinedResult.pdf"))