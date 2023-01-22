# import required module
import os
import re
import csv
import subprocess

#convert the doc files to txt files
exit_code = subprocess.call('./docToTxt.sh')
if exit_code != 0:
	print("ERROR: something went wrong in docToTxt")
	exit(-1)

directory = '~/Desktop/random/momEms/docFiles'
emailRegex = re.compile(r'[a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+')
with open('emails.csv', 'w', ) as csvFile:
	#prep csv file
	writer = csv.writer(csvFile, dialect='excel')
	writer.writerow(["Email", "Origin"])

	for file in os.scandir(directory):
		if file.is_file() and file.name[-4:]==".txt": 
			fieldValue = file.name.replace("_till_2022_Ferin_.txt", "").replace("_till_2022_Ferin.txt", "")
			with open(file.path) as opFile:
				for line in opFile:
					emails = re.findall(emailRegex, line)
					for em in emails:
						print(f"{em} -- {fieldValue}")
						writer.writerow([em, fieldValue])

		print(file.name)
		print("------------------------------------------------")
