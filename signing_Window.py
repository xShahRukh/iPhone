import requests # pip import requests
import json
import os

device = input("Enter Your Device Code... Example: iPhone9,3. (or else press 'Y' to go with default(iPhone 7))")
if device == "Y" or device == "y":
	url= "https://ipsw.me/api/ios/v3/device/iPhone9,3"
else:
	url= "https://ipsw.me/api/ios/v3/device/"+device
a = requests.get(url)

response = a.content

#dir(res)

d =  json.loads(response)

firmwares = d["iPhone9,3"]["firmwares"]

#print firmwares.length
with open("iossign.txt", "w") as outfile:
	for check in firmwares:
		if check["signed"] == True:
			#outfile.write("Filename: " + check["filename"] + "\nVersion: " +check["version"] + "\nUrl:" + check["url"]  + "\n\n\n")
			print("Filename: " + check["filename"] + "\nVersion: " +check["version"] + "\nUrl:" + check["url"]  + "\n\n\n")
			

os.system("pause")
