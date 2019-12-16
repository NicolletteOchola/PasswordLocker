### PASSWORD LOCKER
This is a python application that allows users to generte passwords randomly to enhance security. It also allows useres to store their credentials for different websites and their respective passwords.

## Author
Nicollette Ochola

## BDD
| Behaviour     |  Input          | Output        |
| :-----------: |:---------------:| :-----------: |
|Welcome remarks|-| Hello! Welcome to Password Locker, where your passwords are safe!|
|Dispaly navigation commands|-|   Use these words to choose action:  - c - Create a new Account,  l - Log Into account,  e - Exit from application|
|Show the prompts for creating an account|c|First name, Last name, Password|
|Display login prompt|l|Enter Account Name, Password|
|Display commands for navigation|-|Navigation codes: c - Create a Credential,  d - Display Credentials,  cc - Copy Password,  e - Exit|
|Show prompts for creating a new credential|c|Site name, Account name|
|Dispaly options to enter/generate password|-|Choose an option: p - enter existing, password,  n - generate a password,  e - Exit|
|Show prompt to enter existing password|p|Enter your password|
|Generates password randomly|n|generated password and prints thebcredential details|
|Displays saved credentials|d|All the saved credentials|
|Copyies the password|cc|The password is copied and saved on the clipboard|
|Exits that part of the application|e|Leaves current application location|
|Displays an error message|wrong command/no input|Sorry, not an option. Please try again.|

## Technologies Used
Python 3.6
## Setup Requirements
- Python 3.6
- Internet Connection
- Run the following commands on your terminal:
`$ git clone https://github.com/NicolletteOchola/PasswordLocker.git`
- Navigate to the folder
 `$ cd <folder/file name>`
- To run the application;
 `$ python3.6 password_locker.py`

## Testing
- To run the tests on the application run `$ user_details_test.py`


## Contacts
nicoeochola@gmail.com
+254 726 868063

## License
MIT Licence Nicollette Ochola 2019