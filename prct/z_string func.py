s="my name is akhsat "
s1=" "
s2="123akshat"
s3="123"


False
False
True
True
False
True
print(s.capitalize())                   #          My name is akhsat 
print(s.isalnum())                      #          False
print(s.isalpha())                      #          False
print(s1.isspace())                     #          True
print(s2.isalnum())                     #          True
print(s2.isdigit())                     #          False
print(s3.isdigit())                     #          True
print(s.title())                        #          My Name Is Akhsat 
print("*".join(s))                      #          m*y* *n*a*m*e* *i*s* *a*k*h*s*a*t* 




print("\n\n\n\n")



s="akshat"
s2="  hello my    name is  abc     "
s3=" aur bhaiii "
print(s.upper())                #                AKSHAT
print(s.isupper())              #                False
print(s.islower())              #                True
print(s2.lstrip())              #               "hello my    name is  abc   "       
print(s2.rstrip())              #               "  hello my    name is  abc"
print(s2.strip())               #               "hello my    name is  abc"
print(s3.endswith("i "))         #              True
print(s3.startswith("aur"))     #               False   as it starts with "  aur"
print(s2.replace("abc","akshat")) #             "  hello my name is akshat"
print(s.find("a",3))            #               4
print(min(s))                   #               a



print()
print("akshat1".isalnum())
print("akshat".isalpha())
