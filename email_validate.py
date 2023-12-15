#Function to check email string - will return 1 if input string is Valid or returns 0 is input is Invalid

def ValidateEmail(TestString):        #returns 1 if satisfied
  if '@' in TestString:
    if TestString.startswith('@') or TestString.endswith('@'):
      return 0
    if TestString.count('@')>1:       # @ is permitted
      first, second = TestString.split('@',1)
      if first == '' or second == '':
        return 0
      if first[-1] == "'" and second[0] == "'":
        status = 1
      else:
        return 0
    else:
      status = 1                     #valid
  else:
    return 0                        # @ is not present atleast once



  test= '!#$%^&*\'+-/?_=|{~}.'
  for c in test:
    if TestString.startswith(c) or TestString.endswith(c):
      return 0


  digits='0123456789'
  for c in digits:
    if TestString.startswith(c):
      return 0
  if len(TestString)>=254:
      return 0


  if ' ' in TestString:            #to check ' '
    first, second = TestString.split(' ',1)
    if first == '' or second == '':
      return 0
    if first[-1] == "'" and second[0] =="'":
      status = 1
    else:
      return 0


  local,domain = TestString.split('@')
  Local_status= ValidateLocal(local)              #1 is valid, 0 is invalid
  Domain_status = ValidateDomain(domain)          #1 valid, 0 invalid
  if Local_status == 1 and Domain_status ==1:
    status= 1
  else:
    status= 0

  return status







#Function to check the Local part of the email

def ValidateLocal(local):
  if len(local)>64:
    return 0
  test = '!#$%^&*\'+-/?_=|{~}.'
  if set(local).issubset(set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')):
    status =1
    if set(local).issubset(set(test)):
      for c in test:
        if local.startswith(c) or local.endswith(c):
          return 0
      for c in test:
        if c in local:
          first, second = local.split(c,1)
          if first == '' or second == '':
            return 0
          if first[-1]=="'" and second[0]=="'":
            status =1
          else:
            return 0
  else:
    status =0
  return status








#Function to check the Domain part of email

def ValidateDomain(domain):
  if set(domain).issubset(set('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')):
    status=1
  else:
    status=0
  last_domain= domain.split('.')[-1]
  if last_domain == 'org' or last_domain == 'edu' or last_domain == 'com':
    status= 1
  else:
    status =0

  if len(domain)<7:
    return 0
  if domain.startswith('-') or domain.endswith('-'):
    return 0
  return status







#Interactive mode - email validation

def interactively():
  email = input("Enter email id:")
  status = ValidateEmail(email)
  if status == 1:
    print(email, " is Valid \n")
  else:
    print(email," is NOT Valid \n")
choice = 'y'                                          #initialize
while choice == 'y' or choice == 'Y':
  interactively()                                     # email validity check
  choice = input("\nDo you wish to cintinue: (Y/N)")
print("\n-------INTERACTIVE MODE VALIDATION DONE-------")








#Batch mode - email validation

file_ptr = open('input.txt','r')
f2 = open('out.txt','w')
for line in file_ptr:
  print(line)
  status = ValidateEmail(line.strip())
  if (status==1):
    f2.write("*VALID*---"+line)
  else:
    f2.write('INVALID--'+line)
  print(status)
