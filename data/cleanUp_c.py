import sys

numToRemove = str(sys.argv[1])
with open("proverbs.txt", "r") as file:
    originalText = file.read()
    #mergedLines = "".join(originalText.split("\n"))
    newText = originalText.replace(numToRemove, "")

with open("proverbs.txt", "w") as file:
    file.write(newText)
