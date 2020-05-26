ans = input("Name a file to output to (Do not include the extension!): ")
output = open(str(ans) + ".geojson", "w")
finalwrite = []
finalwrite.append("{\n")
finalwrite.append("\t\"type\": \"FeatureCollection\",\n")
finalwrite.append("\t\"features\": [\n")
finalwrite.append("\t\t{\n")
finalwrite.append("\t\t\"type\": \"Feature\",\n")
finalwrite.append("\t\t\"geometry\": {\n")
finalwrite.append("\t\t\t\"type\": \"Point\",\n")

ans = input("Input the longitude of your place, in degrees, with negative if needed: ")
temp = "\t\t\t\"coordinates\": [" + ans + ", "
ans = input("Input the latitude of your place, in degrees, with negative if needed: ")
temp = temp + ans + "]\n"
finalwrite.append(temp)
finalwrite.append("\t\t},\n")
finalwrite.append("\t\t\"properties\": {\n")
finalwrite.append("\t\t\t\"name\": \"" + input("Enter the name of the place: ") + "\"\n")
finalwrite.append("\t\t}\n")
finalwrite.append("\t}]\n")
finalwrite.append("}")

print(finalwrite)
output.writelines(finalwrite)
output.close()
