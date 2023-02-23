def checkEmail(email):
    # +Some text before '@'
    # +There must be '@' symbol
    # +Some text between '@' and '.'
    # +There must be '.' symbol, after '@' symbol
    # +Some text after the '.'
    t = email.split('@')
    if len(t) != 2 or len(t[0])==0 or len(t[1])==0:
        return False
    #print(t)
    username, domain = email.split('@')
    #print(username, domain)

    t = domain.split('.')
    if len(t) != 2 or len(t[0])==0 or len(t[1])==0:
        return False
    
    return True

import re
def checkEmail2(email):
    pattern = '^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$'
    m = re.search(pattern, email)
    if m != None:
        return True
    return False

print('Enter a valid email address: ')
email = input() # abc@gmail, a@xyz.w

# Check whether the email is valid or not
emailIsCorrect = checkEmail2(email)

if emailIsCorrect:
    print('Great!')
else:
    print('You entered invalid email')