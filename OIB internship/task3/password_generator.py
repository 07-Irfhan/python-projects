import random
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
         'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')']
l=int(input("Enter no of letters:"))
n=int(input("Enter no of numbers:"))
s=int(input("Enter no of symbols:"))

password_list=[]
for i in range(1,l+1):
     char=random.choice(letters)
     password_list+=char
for i in range(1,n+1):
    char=random.choice(numbers)
    password_list+=char

for i in range(1,s+1):
   char=random.choice(symbols)
   password_list+=char
random.shuffle(password_list)
passwords=""

for char in password_list:
  passwords+=char  
print("Genrated password:",passwords)


   
