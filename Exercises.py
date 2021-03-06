# =============================== Exercise 1 ===============================
# Write a function that takes a list of numbers and returns a new list that only
# contains numbers greater than 20 and divisible by 3.

list = [12, 1, 34, 26, 39, 44, 30, 27, 44, 3]

def newlist():
    newlist = []
    for i in list:
        if i >= 20 and i % 3 == 0:
            newlist.append(i)
    print(newlist)

newlist()

# =============================== Exercise 2 ===============================
# (A) Write a function that will take a text and reverse every second word.
# (B) Use part A function to save reversed text in a second file.

def reverse_every_second(line):
    words = line.split()
    reversed_words = []
    for i in range(len(words)):

        if i % 2 == 0:
            reversed_words.append(words[i])
        else:
            reversed_words.append(words[i][::-1])
    new_sentence = ' '.join(reversed_words)
    return new_sentence

try:
    input_file = open('LabTextFile.txt', 'r')
    output_file = open('ReversedTextFile.txt', 'w')

    for line in input_file:
        new_line = reverse_every_second(line)
        output_file.write(new_line)
        output_file.write('\n')

    input_file.close()
    output_file.close()
except IOError:
    print('Problem with the file, please check the name and location.')

# =============================== Exercise 3 ===============================
# Write a function divisors(n) that returns a list of the divisors of the integer (n)
# including 1 but excluding the number itself. For example, divisors (24) → [1,2,3,4,6,8,12]

def divisor(n):
    div_list = []
    non_div_list = []
    for i in range(n):
        if n % i == 0:
            div_list.append(i)
        else:
            non_div_list.append(i)

    print(div_list)
    print(non_div_list)

n = int(input("Enter a number and see the divisors - "))
divisor(n)

# =============================== Exercise 4 ===============================
# Write a function fib(n) that returns a list of the first n Fibonacci numbers
def fib(n):
    seq = []
    a, b = 0, 1

    while b < n:
        seq.append(b)
        a, b = b, a+b
    print(seq)

n = int(input("Enter a number and checks it's Fibonacci sequence - "))
fib(n)


# =============================== Exercise 5 ===============================
# Write a function that will prompt a user for a number, and print all kaprekar numbers from 10 to that number.
# Use functions to structure your code where appropriate (kaprekar number, user input (10 - n))

# need to fix list in this

def kaprekar_num(i):
    square = i**2
    str_square = str(square)
    split_square = (str_square[:2], str_square[-2:])
    kap_num = int(split_square[0]) + int(split_square[1])
    if kap_num == i:
        return i

def number_input():
    kap_num_list = []
    n = int(input("Enter any number to check all kaprekar numbers from 10 to that number, press '0' to quit -> "))
    if n > 10:
        for i in range(10, n+1):
            kap_num_list.append(kaprekar_num(i)) ## here
        print(kap_num_list,"- are kaprekar numbers in range 10 - {0}".format(n))
    else:
        print("Input should be bigger than 10")

number_input()

# =============================== Exercise 6 ===============================
# Write a program to check if a number is a Narcissistic number

def narcissistic(num):
    multiple_v = 0
    for i in num:
        digit = int(i)
        power = digit**len(num)
        multiple_v += power
    if multiple_v == int(num):
        print("{0} is a Narcissistic number.".format(num))
    else:
        print("{0} is not a Narcissistic number.".format(num))

def number():
    num = input("Enter a number to see if its a Narcissistic number -> ")
    narcissistic(num)

number()
