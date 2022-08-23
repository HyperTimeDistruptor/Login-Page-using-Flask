# Setting the defaults for the variable "logged_user"
logged_user = None

# Defining the function valid_login to tell the application when it should log the user in
def valid_login(username = None, password = None):
    if username is not None and password is not None:
        if username == 'user' and password == 'password':
            return True
        else: 
            return False
    else:
        return False
    
# The function to log the user in
def log_the_user_in(username = None):
    if username is not None:
        logged_user = username
        return logged_user
    else:
        return False