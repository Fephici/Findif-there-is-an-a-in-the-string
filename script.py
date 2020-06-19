import time

def sleep():
	print()
	time.sleep(2)
 
 # The actual program
 print("This program will find if there is an a in a string.")
 
 sleep()
 
 string = input("Enter a string: ")
 
 if string.find("a") == -1:
 	print('Sorry we couldn\'t find an "a" string')
elif string.find("a") >= 0:
	sleep()
	print("We found an a at index " + str(string.find("a")))
	
