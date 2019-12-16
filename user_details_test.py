import unittest
import pyperclip
from user_details import User, Credential


class TestUser(unittest.TestCase):
	'''
	Test class that defines test cases for the user class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''

	def setUp(self):
		'''
		Function to create a user account before each test
		'''
		self.new_user = User('Nicole', 'Ochola', 'pass3006')

	def test__init__(self):
		'''
		Test to if check the creation of new user has been done properly
		'''
		self.assertEqual(self.new_user.firstName, 'Nicole')
		self.assertEqual(self.new_user.last_name, 'Ochola')
		self.assertEqual(self.new_user.password, 'pass3006')

	def test_save_user(self):
		'''
		Test to check if the new users information is saved
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list), 1)


class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''

	def test_check_user(self):
		'''
		Function to test whether the the function for login works well. i.e user credentials should mathch if already in the list
		'''
		self.new_user = User('Nicole', 'Ochola', 'pass3006')
		self.new_user.save_user()
		user2 = User('Paul', 'Ochola', 'pass3006')
		user2.save_user()

		for user in User.users_list:
			if user.firstName == user2.firstName and user.password == user2.password:
				current_user = user.firstName
		return current_user

		self.assertEqual(current_user, Credential.check_user(
		    user2.password, user2.firstName))

	def setUp(self):
		'''
		Function to create an account's information before each test
		'''
		self.new_credential = Credential(
		    'Nicole', 'Instagram', 'nicollette', 'pass3006')

	def test__init__(self):
		'''
		Test to if check the creation of account instances is properly done
		'''
		self.assertEqual(self.new_credential.user_name, 'Niocle')
		self.assertEqual(self.new_credential.siteName, 'Instagram')
		self.assertEqual(self.new_credential.accountName, 'nicollette')
		self.assertEqual(self.new_credential.password, 'pass3006')

	def test_save_credentials(self):
		'''
		Test to check if the new account info is saved into the credentials list
		'''
		self.new_credential.save_credentials()
		facebook = Credential('Nicole', 'Facebook', 'nicollette', 'pass3006')
		facebook.save_credentials()
		self.assertEqual(len(Credential.credentials_list), 2)

	def test_generate_password(self):
		'''
		Test to check if the password generator generates an 8 character password
		'''
		self.facebook = Credential('Facebook', 'nicollette', '')
		self.facebook.password = generate_password()
		self.assertEqual()

	def delete(self):
		'''
		Function to delete the information after every test
		'''
		Credential.credentials_list = []
		User.users_list = []

	def test_display_credentials(self):
		'''
		Test to check if the method to display credentials works
		'''
		self.new_credential.save_credentials()
		facebook = Credential('Nicole', 'Facebook', 'nicollette', 'pass3006')
		facebook.save_credentials()
		instagram = Credential('Paul', 'Instagram', 'barryp', 'pass0603')
		instagram.save_credentials()
		self.assertEqual(len(Credential.display_credentials(facebook.user_name)), 2)

	def test_find_by_siteName(self):
		'''
		Test to check if the method to find the credentials by site works
		'''
		self.new_credential.save_credentials()
    facebook = Credential('Nicole', 'Facebook', 'nicollette', 'pass3006')
		facebook.save_credentials()
		credential_exists = Credential.find_by_siteName('facebook')
		self.assertEqual(credential_exists,facebook)

	def test_copy_credential(self):
		'''
		Test to check if the copy a credential method copies the correct credential
		'''
		self.new_credential.save_credentials()
    facebook = Credential('Nicole','Facebook','nicollette','pass3006')
    facebook.save_credentials()
		find_credential = None
		for credential in Credential.user_credentials_list:
				find_credential = Credential.find_by_siteName(credential.siteName)
				return pyperclip.copy(find_credential.password)
		Credential.copy_credential(self.new_credential.siteName)
		self.assertEqual('pass3006',pyperclip.paste())
		print(pyperclip.paste())

if __name__ == '__main__':
	unittest.main(verbosity = 2)
