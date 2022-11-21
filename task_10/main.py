class workWithFiles:
    def createFile(self, name):
        newFile = open(f"{name}.txt", "x")
        print(f"1) The file with name {name}.txt has just been created ")
        newFile.close()
        pass
    def openFile(self, name):
        createdFile = open(f"{name}.txt", "w")
        print(f"2) The file {name}.txt was opened")
        return createdFile
        pass
    def writeInFile(self, name):
        opennedFile = self.openFile(name)
        textToWrite = [
            "This is the coding exercise proposed by the Open Bootcamp course\n",
            "I'm Carlos Guerra and I'm happy to be doing it.\n",
            "This is to improve and increase my range of programming languages.\n"]
        opennedFile.writelines(textToWrite)
        print(f"3) We have just written the sentences inside the file {name}.txt")
        opennedFile.close()

    def readFile(self, name):
        print(f"4) We started by reading the file")
        readFileTxt = open(f"{name}.txt", "r")
        sentences = readFileTxt.readlines()
        for sentence in sentences:
            print(sentence)


def main():
    workFile = workWithFiles()
    workFile.createFile("OpenBootcamp")
    workFile.writeInFile("OpenBootcamp")
    workFile.readFile("OpenBootcamp")

if __name__ == "__main__":
    main()