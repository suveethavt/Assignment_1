'''Registration and Login system using Python,
file handling'''

import re
regs=input("Enter register or log in:")

special_char="?.,';\:[]{}!@#$%^=+_-&*()|"
if regs.lower()=='register':
 e_id=input("Enter the email id: ")
#stage 1
 f=0
 for e in special_char:
    if e==e_id[0]:
     #   print("1")
        f=1
 a=re.findall('.+@\.[a-z]',e_id)
 if a!=[]:
    #print("2")
    f=1

 b=re.findall('\d\#@[a-z].[a-z]',e_id)
 if b!=[]:
    #print("3")
    f=1

 if f==0:
    c=re.findall('.+@[a-z].[a-z]',e_id)
    print("valid")
 else:
    print("Invalid")

#password
 password=input("Enter password:")
 p=len(password)
 countt=0

 for i in special_char:
  for j in range(p):
    if i==password[j]:
        countt=1
 d=re.findall('\d+',password)
 U=re.findall('[A-Z]+',password)
 l=re.findall('[a-z]+',password)
 if p<=4 or p<16:
    if d!=[] and U!=[] and l!=[] and countt==1:
        print("You have successfully registered ")
    else:
        print("your password must have minimum one special character, one digit,one uppercase, one lowercase character")
 else:
    print("Password length should be greater than 5 and less than 16")

 reg="{}:{}".format(e_id,password)
#stage 2

 name_password="{}".format(reg)
 with open("ID_files.txt","a+") as file:
    file.write(str(name_password)+"\n")
 file.close()

else:
#stage 3'''For login'''
   log=input("Enter the login id:")
   check_list=0
   with open("ID_files.txt","r+") as fc:
    check=fc.readlines()
    cl=len(check)
    for r in range(cl):
        row = check[r]
        row_split=row.split(':')
        if row_split[0]==log:
            UP = row_split[0]
            UP1 = row_split[1]
            check_list=1
            break

    if check_list==1:
           ent_pass=input("Enter password or Forget password:")
           if ent_pass.lower()=="forget password":
                  print(f'Based on user name your password is :{row_split[1]}')
           elif ent_pass.lower()=="password":
                  pw=input("Enter password:")
                  print("Successfully logined ")
           elif ent_pass==UP1:
                  print("Successfully logined ")

    else:
           print("Entered id is not registered, please register")

   fc.close()
