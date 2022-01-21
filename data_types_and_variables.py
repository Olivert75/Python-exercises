#Identify the data type of the following values:
type (99.9)

type("False")

type(False)

type('0')

type(0)

type(True)

type('True')

type([{}])

type({'a':[]})

# What data type would best represent:
"""""
A term or phrase typed into a search box? String
If a user is logged in? boolean
A discount amount to apply to a user's shopping cart? float
Whether or not a coupon code is valid? boolean
An email address typed into a registration form? string
The price of a product? float
A Matrix? list
The email addresses collected from a registration form? string
Information about applicants to Codeup's data science program? string
"""

#For each of the following code blocks, read the expression and predict what the result of evaluating it would be, 
#then execute the expression in your Python REPL.
"""
# I will get an error because we are adding a string with a number  
'1' + 2

#  2
6 % 4

# int
type(6 % 4)

# string
type(type(6 % 4))

#  Error beause + 
'3 + 4 is ' + 3 + 4

# False
0 < 0

# False
'False' == False

# False
True == 'True'

# True
5 >= -5

# True
True or "42"

# 1
6 % 5

# False
5 < 4 and 1 == 1

# False
'codeup' == 'codeup' and 'codeup' == 'Codeup'

# True
4 >= 0 and 1 !== '1'

# True
6 % 3 == 0

# True
5 % 2 != 0

# error
[1] + 2

# [1,2]
[1] + [2]

# error
[1] * 2

# [2]
[1] * [2]

#true
[] + [] == []

# error
{} + {}
"""

#You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?

littleMermaid = 3
brotherBear = 5
hercules = 1 
rentalLst = [littleMermaid, brotherBear, hercules]

price = sum(rentalLst) * 3

print (price)

#Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. 
# Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.

googlePay = 400
amazonPay = 380
facebookPay = 350 

googleHrs = 6
amazonHrs = 4
facebookHrs = 10

payment = (googlePay * googleHrs) + (amazonPay * amazonHrs) + (facebookPay * facebookHrs)

print (payment)

#A student can be enrolled to a class only if the class is not full 
# and the class schedule does not conflict with her current schedule.

classFull = False
scheduleConflict = False

enrolled = not (classFull or scheduleConflict)

print (enrolled)

#A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium members do not need to buy a specific amount of products.

premiumMem = True
currentOffer = False 
noItems = 2

offer = currentOffer and (noItems > 2 or premiumMem)

print(offer) 

#Create a variable that holds a boolean value for each of the following conditions:
#the password must be at least 5 characters
#the username must be no more than 20 characters
#the password must not be the same as the username
#bonus neither the username or password can start or end with whitespace 

username = 'codeup'
password = 'notastrongpassword'

userChar = len(username) < 20
passChar = len(password) >= 5

passUserSame = username == password

validRegistration = userChar and passChar and not passUserSame

print (validRegistration)

#bonus
userSpace = username[0] == ' ' or username[-1] == ' '
passSpace = password[0] == ' ' or password[-1] == ' '

validRegistration = userChar and passChar and not passUserSame and not (userSpace or passSpace)

print (validRegistration)