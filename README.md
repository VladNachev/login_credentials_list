# Login Credentials List
## Test login using credentials from credentials username/password file list
I created this script for testing login form by using file-list with prepared combinations of usernames and passwords. 

The script can be used in the scope of security testing and not only.

Target URL which is currently set: https://practicetestautomation.com/practice-test-login/

![](/resources/login_form.png?raw=true)

Target URL can be changed at any time.

## Short description
- login_script.py - main script 
- resources/credentials.csv - this file contains the username/password list. You can create your own as well. 
- resources/output.txt - the program will save the results to the output.txt file.

## Clone repository

```bash
$ git clone https://github.com/VladNachev/login_credentials_list.git
```

## Requirements
- python
- selenium