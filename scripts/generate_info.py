#!/usr/bin/env python

from MythTV import MythDB
import sys
out = "/var/lib/mythtv/recordings/recordings.txt"

if __name__ == "__main__":
	try:
		db = MythDB()
	except:
		print("Unable to connect to the MythTV database, aborting.")
		sys.exit(1)

	try:
		mylist = list()
		recs = db.searchRecorded()
		for recording in recs:
			try:
				y = recording.getProgram()
				_when = y["starttime"]
				a = "{Title}###---###{description}###---###{filename}###---###{filesize}###---###{starttime}".format(
						Title=y["title"],
						description=y["description"],
						filename = y["filename"],
						filesize = y["filesize"],
						starttime = _when
					)
				add_this = (_when.timestamp(), a)
				mylist.append(add_this)
			except:
				print("Skipping", recording)

		if mylist:
			mylist.sort(reverse=True)
			with open(out, "w") as fobj:
				for i in mylist:
					#print(i[1])
					fobj.write(i[1] + "\n")
		else:
			print("Error 22.1, please check!")
			
	except:
		print("Some error")
	
