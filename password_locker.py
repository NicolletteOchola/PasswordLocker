import pyperclip
from user_details import User, Credential

def create_user(firstName,lastName,password):
	'''
	Function to create a new user account
	'''
	new_user = User(firstName,lastName,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def verify_user(first_name,password):
	'''
	Function that checks if the user exists (Verification)
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def create_credential(userName,siteName,accountName,password):
	'''
	Function to add new credentials
	'''
	new_credential=Credential(userName,siteName,accountName,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def display_credentials(userName):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials(userName)
	
def copy_credential(sitName):
	'''
	Function to copy a credentials details to the clipboard
	'''
	return Credential.copy_credential(siteName)

def main():
	print(' ')
	print('Hello! Welcome to Password Locker.')
	while True:
		print(' ')
		print("-"*60)
		print('Use these words to choose action: \n c - Create a new Account \n l - Log Into account \n e - Exit from application')
		codeWord = input('Enter a choice: ').lower().strip()
		if codeWord == 'Exit':
			break

		elif codeWord == 'c':
			print("-"*60)
			print(' ')
			print('To create a new account:')
			firstName = input('Enter your first name - ').strip()
			lastName = input('Enter your last name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(firstName,lastName,password))
			print(" ")
			print(f'New Account details: {firstName} {lastName} using password: {password}')

		elif codeWord == 'l':
			print("-"*60)
			print(' ')
			print('To login, please enter your account details:')
			userName = input('Enter Username - ').strip()
			password = str(input('Enter password - '))
			user_exists = verify_user(userName,password)
			if user_exists == userName:
				print(" ")
				print(f'Welcome {userName}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigation codes: \n c - Create a Credential \n d - Display Credentials \n cc - Copy Password \n e - Exit')
					codeWord = input('Enter an action: ').lower().strip()
					print("-"*60)
					if codeWord == 'e':
						print(" ")
						print(f'Thank you! Have a nice day :) {userName}')
						break
					elif codeWord == 'c':
						print(' ')
						print('Enter your credential details:')
						siteName = input('Site name - ').strip()
						accountName = input('Account name - ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Choose an option: \n p - enter existing password \n n - generate a password \n e - Exit')
							psw_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if psw_choice == 'p':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'n':
								password = generate_password()
								break
							elif psw_choice == 'e':
								break
							else:
								print('Sorry, not an option. Please try again')
						save_credential(create_credential(userName,siteName,accountName,password))
						print(' ')
						print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif codeWord == 'd':
						print(' ')
						if display_credentials(userName):
							print('Below is a list of your credentials:')
							print(' ')
							for credential in display_credentials(user_name):
								print(f'Site Name: {credential.site_name} \n  Account Name: {credential.account_name} \n - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("Sorry, no credentials stored for this username")
							print(' ')
					elif codeWord == 'cce':
						print(' ')
						chosen_site = input('Enter the name of the site: ')
						copy_credential(chosen_site)
						print('')
					else:
						print('Sorry, not an option. Please try again.')

			else: 
				print(' ')
				print('Sorry, wrong details, please try again or create a new account')		
		
		else:
			print("-"*60)
			print(' ')
			print('Sorry, not an option. Please try again.')
if __name__ == '__main__':
	main()
