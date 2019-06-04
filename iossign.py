import requests # pip import requests
import json
import os

url= "https://ipsw.me/api/ios/v3/device/iPhone9,3"

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