#Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(num):
    if x == 2 or x == "2":
        return True
    else:
        return False

#Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(letter_type):
    return letter_type.lower() in ['a', 'e', 'i', 'o', 'u']

#Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(letter):
    if is_vowel(letter):
        return False
    else:
        return True

#Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

def cap_first_letter(word):
    if is_consonant(word[0]) == str:
        return word.capitalize()
    else:
        return word

#Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tips_percentage, bill_total):
    if tips_percentage >= 1:
         tips_percentage /= 100
    tips_amount = tips_percentage * bill_total
    return tips_amount

#Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount_percent):
    discount = original_price * discount_percent
    return discount_percent - discount

#Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(c):
    return float(c.replace(',', ''))

#Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(letter_grade):
    if 90 <= letter_grade <= 100:
        return "A"
    elif 80 <= letter_grade <= 89:
        return "B"
    elif 70 <= letter_grade <= 79:
        return "C"
    elif 60 <= letter_grade <= 69:
        return "D"
    else:
        return "F"

#Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(rm_vowels):
    for i in rm_vowels:
        if i in "aeiou":
            rm_vowels = rm_vowels.replace(i, '')
    return rm_vowels

#Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores
#for example:
#Name will become name
#First Name will become first_name
# % Completed will become completed

def normalize_name(rm_char):
    result = ''

    rm_char = rm_char.lower()

    for i in rm_char:
        if i.isidentifier() or i == " ":
            result += i
    
    result = result.replace(" ", "_")
    result = result.strip()
    
    return result

#Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
#cumulative_sum([1, 1, 1]) returns [1, 2, 3]
#cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(lst):
    for i in range (1, len(lst)):
        lst[i] += sum(lst[i -1:i])
    return lst

#Bonus

#Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
def twelveto24(time):
    #Check the last two element of the time is am and first two element is 12
    if time[-2:] == "am" and time[:2] == "12":
        return "00" + time[2:-2]
    #remove am
    elif time[:-2] == "am" and time[:2] != "12":
        return time[:-2]
    elif time[-2:] == "pm" and time[:2] == "12":
        return time[:-2]
    else:
        time = str(int(time[:2]) + 12) + time[2:8]
        return time

#Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
