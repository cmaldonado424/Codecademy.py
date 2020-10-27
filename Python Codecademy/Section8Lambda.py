# Basic Lambda Function
add_two = lambda my_input: my_input + 2
print(add_two(3))
print(add_two(100))
print(add_two(-2))

# difference between lamda and def:

# Lambda is an anonymous, single expression function 
# that can be used in the block they were created

# Def breaks code into smaller modular chunks that can be called and used anywhere we want 

# CONTAINS A: function to check if a word contains letter "a", returns True/False
contains_a = lambda fruit: "a" in fruit
print contains_a("banana")
print contains_a("apple")
print contains_a("cherry")

# LONG STRING: confirms if a string has more than a certain amount of characters
long_string =  lambda word: len(word) > 12

print long_string("short")
print long_string("photosynthesis")

# ENDS IN "A"
ends_in_a = lambda word: word[-1] == "a"

print ends_in_a("data")
print ends_in_a("aardvark")

# DOUBLE OR ZERO if statement
double_or_zero = lambda num:num*2 if num > 10 else 0
print double_or_zero(15)
print double_or_zero(5)

#EVEN OR ODD modulo
even_or_odd = lambda num: "even" if num%2 == 0 else "odd"

print even_or_odd(10)
print even_or_odd(5)

# NOT A MULTIPLE
multiple_of_three = lambda num: "multiple of three" if num%3==0 else "not a multiple"
print multiple_of_three(9)
print multiple_of_three(10)

# MOVIE RATING if statment
rate_movie = lambda rating: "I liked this movie" if rating > 8.5 else "This movie was not very good"

print rate_movie(9.2)
print rate_movie(7.2)

#ONES PLACE
ones_place = lambda num: num%10 

print ones_place(123)
print ones_place(4)

#DOUBLE SQUARE 
double_square = lambda num: num**2*2

print double_square(5)
print double_square(3)

#ADD RANDOM
import random
#Write your lambda function here
add_random = lambda num: num+random.randint(1,10)
print add_random(5)
print add_random(100)











