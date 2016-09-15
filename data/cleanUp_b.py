import sys

#numToRemove = str(sys.argv[1])
with open("proverbs.txt", "r") as file:
    originalText = file.read()
    mergedLines_a = "".join(originalText.split("\n   "))
    mergedLines_b = "".join(mergedLines_a.split("\n"))

with open("proverbs.txt", "w") as file:
    file.write(mergedLines_b)
