import pyperclip
import random
import string

global users
class User:
	'''
	Class to create user accounts and save their information
	'''

	users_list = []
	def __init__(self,firstName,lastName,password):
		'''
		Method to outline the objects that will store user information
		'''


		self.firstName = firstName
		self.lastName = lastName
		self.password = password

	def save_user(self):
		'''
		A function to store/save users
		'''
		User.users_list.append(self)
		
class Credential:
	'''
	A class to create credentials, generate passwords and store user information
	'''
	credentials_list =[]
	user_credentials_list = []
	@classmethod

	def check_user(cls,firstName,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.firstName == firstName and user.password == password):
				current_user = user.first_name
		return current_user

	def __init__(self,userName,siteName,accountName,password):
		'''
		Method to define the properties for each user object will hold.
		'''


		self.userName = userName
		self.siteName = siteName
		self.accountName = accountName
		self.password = password

	def save_credentials(self):
		'''
		Function to save a newly created user instance
		'''
		Credential.credentials_list.append(self)
	
	def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass

	@classmethod
	def display_credentials(cls,user_name):
		'''
		Class method to display the list of credentials saved
		'''
		user_credentials_list = []
		for credential in cls.credentials_list:
			if credential.user_name == user_name:
				user_credentials_list.append(credential)
		return user_credentials_list
				

	
# 	@classmethod
# 	def find_by_site_name(cls, site_name):
# 		'''
# 		Method that takes in a site_name and returns a credential that matches that site_name.
# 		'''
# 		for credential in cls.credentials_list:
# 			if credential.site_name == site_name:
# 				return credential

# 	@classmethod
# 	def copy_credential(cls,site_name):
# 		'''
# 		Class method that copies a credential's info after the credential's site name is entered
# 		'''
# 		find_credential = Credential.find_by_site_name(site_name)
# 		return pyperclip.copy(find_credential.password)

# © 2019 GitHub, Inc.