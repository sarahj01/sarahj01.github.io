from hashlib import *

# The above will give you a hash of MYSTRING
password = sha256("jhingan".encode('utf-8')).hexdigest() 
account = { "sarah": password
	
}
start = True			
#pass_input = input("enter password: ")

while start:
	user_input = input("enter username: ")
	if user_input in account:
		print("recognized")
		pass_input = input("enter password: ")
		hash_pass = sha256(pass_input.encode('utf-8')).hexdigest() 
		if hash_pass in account[user_input]:
			print("login successful")
			start = False
		else:
			pass_input = input("try again: ")


	else: 
		print("username not recognized")
		create = input("want to make an account(Yes or No: ")
		if create == "Yes":
			user_var = input("what's your username: ")
			pass_var = input("what's your password: ")
			hash_pass = sha256(pass_var.encode('utf-8')).hexdigest() 
			account[user_var] = hash_pass
			print("Sign up successful")
			login = input("Do you want to log in? y/n")
			if login == "n":
				start = False















