def file_io():
	filename = "test.txt"
	with open(filename, "w") as f_write:
		f_write.write("Hello World \n How are you doing?")
		f_write.close()
	with open(filename, "r") as f_read:
		print(f_read.readlines())



file_io()



