import math

ans = input("Provide the name for an input CSV, no need to write the extension: ")
file = None

try:
    file = open(ans + ".csv", "r")
except FileNotFoundError:
    print("File was not found. Aborting")
    exit("FNF")

inputlist = file.readlines()

finalwrite = []
finalwrite.append("{\n")
finalwrite.append("\t\"type\": \"FeatureCollection\",\n")
finalwrite.append("\t\"features\": [\n")




for i in inputlist:
    if i == inputlist[0]:
        continue
    temp = i.split(",")
    locationID = temp[1].strip()
    name = temp[0].strip()
    x = math.floor(int(locationID) / 360)
    y = int(locationID) % 360
    finalwrite.append("\t\t{\n")
    finalwrite.append("\t\t\"type\": \"Feature\",\n")
    finalwrite.append("\t\t\"geometry\": {\n")
    finalwrite.append("\t\t\t\"type\": \"Point\",\n")
    finalwrite.append("\t\t\t\"coordinates\": [" + str(y) + ", " + str(x) + "]\n")
    finalwrite.append("\t\t},\n")
    finalwrite.append("\t\t\"properties\": {\n")
    finalwrite.append("\t\t\t\"name\": \"" + name + "\"\n")
    finalwrite.append("\t\t}\n")

    if i == inputlist[-1]:
        finalwrite.append("\t}\n")
    else:
        finalwrite.append("\t},\n")
finalwrite.append("]}")
ans = input("Name a file to output to (Do not include the extension!): ")
output = open(str(ans) + ".geojson", "w")
output.writelines(finalwrite)
output.close()