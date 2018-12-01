

'''
Revature is building a new API! This API contains functions for validating data, 
solving problems, and encoding data. 

The API consists of 10 functions that you must implement.

Guidelines:
1) Edit the file to match your first name and last name with the format shown.

2) Provide tests in the main method for all functions, We should be able to run
this script and see the outputs in an organized manner.

3) You can leverage the operating system if needed, however, do not use any non
legacy command that solves the problem by just calling the command.

4) We believe in self commenting code, however, provide comments to your solutions
and be organized.

5) Leverage resources online if needed, but remember, be able to back your solutions
up since you can be asked.

6) Plagiarism is a serious issue, avoid it at all costs.

7) Don't import external libraries which are not python native

8) Don't change the parameters or returns, follow the directions.

9) Assignment is optional, but totally recommend to achieve before Monday for practice.

Happy Scripting!

© 2018 Revature. All rights reserved.
'''

'''
Use the main function for testing purposes and to show me results for all functions.
'''
def main():  
        reverse('example')
        acronym('Portable Network Graphics')
        whichTriangle(2,2,2) #equi
        whichTriangle(1,2,2) #isoceles
        whichTriangle(2,1,2) #isoceles
        whichTriangle(3,2,1) #scalene
        scrabble("lebowski") #13
        armstrong(153)
        armstrong(9)
        armstrong(154)

'''
1. Reverse a String. Example: reverse("example"); -> "elpmaxe"

Rules:
- Do NOT use built-in tools
- Reverse it your own way

param: str
return: str
'''
def reverse(s):
        str = ""
        for i in s:
                str = i + str
        print(str)

'''
2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
Acronyms)! Help generate some jargon by writing a program that converts a
long name like Portable Network Graphics to its acronym (PNG).

param: str
return: str
'''
def acronym(phrase):
        output = ''
        seperate_words = phrase.split(' ')
        for char in seperate_words:
                output = output + char[0]
        print(output)
        ### FIRST CODE ###
        # acronym = []
        # whitespace = ' '
        # i = 0
        # if phrase[0]:
        #         acronym.append(phrase[0])
        # for char in phrase:
        #         if char == whitespace and i < len(phrase):
        #                 acronym.append(phrase[i + 1])
        #         i = i + 1
        # acronym = ''.join(acronym)
        # print(acronym)
'''
3. Determine if a triangle is equilateral, isosceles, or scalene. An
equilateral triangle has all three sides the same length. An isosceles
triangle has at least two sides the same length. (It is sometimes specified
as having exactly two sides the same length, but for the purposes of this
exercise we'll say at least two.) A scalene triangle has all sides of
different lengths.

param: float, float, float
return: str -> 'equilateral', 'isoceles', 'scalene'
'''
def whichTriangle(sideOne, sideTwo, sideThree):
        if sideOne == sideTwo and sideTwo == sideThree:
                result = 'equilateral'
        elif sideOne == sideThree or sideTwo == sideThree or sideOne == sideTwo:
                result = 'Isoceles'
        else :
                result = 'scalene'
        print(result)   


'''
4. Given a word, compute the scrabble score for that word.

--Letter Values-- Letter Value A, E, I, O, U, L, N, R, S, T = 1; D, G = 2; B,
C, M, P = 3; F, H, V, W, Y = 4; K = 5; J, X = 8; Q, Z = 10; Examples
"cabbage" should be scored as worth 14 points:

3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
point for E And to total:

3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14

param: str
return: int
'''
def scrabble(word):
        score = 0
        onePoint = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']
        twoPoints = ['D', 'G']
        threePoints = ['B', 'C', 'M', 'P']
        fourPoints = ['F', 'H', 'V', 'W', 'Y', ]
        fivePoints = 'K'
        eightPoints = ['J','X']
        tenPoints = ['Q', 'Z']
        word = word.upper()
        for letter in word:
                if letter in onePoint:
                        score = score + 1
                        print(letter,end=', ')
                        print(score)
                elif letter in twoPoints:
                        score = score + 2
                        print(letter,end=', ')
                        print(score)
                elif letter in threePoints:
                        score = score + 3
                        print(letter,end=', ')
                        print(score)
                elif letter in fourPoints:
                        score = score + 4
                        print(letter,end=', ')
                        print(score)
                elif letter in fivePoints:
                        score = score + 5
                        print(letter,end=', ')
                        print(score)
                elif letter in eightPoints:
                        score = score + 8
                        print(letter,end=', ')
                        print(score)
                elif letter in tenPoints:
                        score = score + 10
                        print(letter,end=', ')
                        print(score)
                else:
                        print("NOT A LETTER! = 0 points")
        print('Your total score is: ' + str(score))

'''
5. An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9 10 is not an Armstrong number,
because 10 != 1^2 + 0^2 = 2 153 is an Armstrong number, because: 153 = 1^3 +
5^3 + 3^3 = 1 + 125 + 27 = 153 154 is not an Armstrong number, because: 154
!= 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190 Write some code to determine whether
a number is an Armstrong number.

param: int
return: bool
'''
def armstrong(number):
        number_string = str(number)
        output = []
        is_armstrong = False
        sum = 0
        number_of_digits = len(str(number))

        for digit in number_string:
                output = output + digit.split(' ')
                digit = int(digit)
                sum = sum + (digit**(number_of_digits))
        if sum == number:
                is_armstrong = True
                print(str(is_armstrong) + ', THIS IS AN ARMSTRONG NUMBER!')
        else:
                print(str(is_armstrong) + ', NOT AN ARMSTRONG NUMBER!')

'''
6. Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.
 
Note that 1 is not a prime number.

param: int
return: list
'''
def primeFactors(number):
        print('test')   

'''
7. Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
gramma, "every letter") is a sentence using every letter of the alphabet at
least once. The best known English pangram is:

The quick brown fox jumps over the lazy dog.
 
The alphabet used consists of ASCII letters a to z, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
 
param: str
return: bool
'''
def pangram(sentence):
        print('test')   

'''
8. Sort list of integers.
f([2,4,5,1,3,1]) = [1,1,2,3,4,5]

Rules:
- Do NOT sort it with .sort() or sorted(list) or any built-in tools.
- Sort it your own way

param: list
return: list
'''
def sort(numbers):
        print('test')   

'''
9. Create an implementation of the rotational cipher, also sometimes called
the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the
letters in the alphabet using an integer key between 0 and 26. Using a key of
0 or 26 will always yield the same output due to modular arithmetic. The
letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly
used rotational cipher is ROT13.

A ROT13 on the Latin alphabet would be as follows:

Plain: abcdefghijklmnopqrstuvwxyz Cipher: nopqrstuvwxyzabcdefghijklm It is
stronger than the Atbash cipher because it has 27 possible keys, and 25
usable keys.

Ciphertext is written out in the same formatting as the input including
spaces and punctuation.

Examples: ROT5 omg gives trl ROT0 c gives c ROT26 Cool gives Cool ROT13 The
quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire
gur ynml qbt. ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The
quick brown fox jumps over the lazy dog.

param: int, str
return: str
'''
def rotate(key, string):
        print('test')   

'''
10. Take 10 numbers as input from the user and store all the even numbers in a file called even.txt and
the odd numbers in a file called odd.txt.

param: none, from the keyboard
return: nothing
'''
def evenAndOdds():
        print('test')   

if __name__ == "__main__":
        main()
