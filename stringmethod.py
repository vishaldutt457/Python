str = "i love PYTHON";
print(str.capitalize());
# output=I love python

text = "pYtHon"
print(text.casefold());
# Output: python

sentence = "Python is awesome";
print(sentence.center(24,'*'));
# Output: ***Python is awesome****


message = 'python is popular programming language';
print(message.count('p'))
# Output: Number of occurrence of p: 4


title = 'Python Programming';
print(title.encode())
# Output: b'Python Programming'


message = 'Python is fun'
print(message.endswith('fun'))
# Output: True


str = 'xyz\t12345\tabc';
print(str.expandtabs())
# Output: xyz     12345   abc


message = 'Python is a fun programming language'
print(message.find('fun'))
# Output: 12

point = {'x':4,'y':-5}
print('{x} {y}'.format(**point))


text = 'Python is fun'
print(text.index('is'))
# Output: 7


name = "JoHn CeNa"
print(name.swapcase())
# Output: jOhN cEnA


# string contains either alphabet or number 
name1 = "Python3"
print(name1.isalnum()) #True
name2 = "Python 3"
print(name2.isalnum()) #False


name = "Monica"
print(name.isalpha())
# contains whitespace
name = "Monica Geller"
print(name.isalpha())
# contains number
name = "Mo3nicaGell22er"
print(name.isalpha())


s = "28212"
print(s.isdecimal())
# contains alphabets
s = "32ladk3"
print(s.isdecimal())
# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdecimal())


str1 = '342'
print(str1.isdigit())
str2 = 'python'
print(str2.isdigit())
# Output: True
#         False


str = 'Python'
print(str.isidentifier())
# Output: True
str = 'Py thon'
print(str.isidentifier())
# Output: False
str = '22Python'
print(str.isidentifier())
# Output: False
str = ''
print(str.isidentifier())
# Output: False


s = 'this is good'
print(s.islower())
# Output: True
s = 'th!s is a1so g00d'
print(s.islower())
# Output: True
s = 'this is Not good'
print(s.islower())
# Output: False


pin = "523"
print(pin.isnumeric())
# Output: True


text = 'apple'
result = text.isprintable()
print(result)
# Output: True


s = '   \t'
print(s.isspace())
# Output: True
s = ' a '
print(s.isspace())
# Output: False
s = ''
print(s.isspace())
# Output: False

text = 'My favorite number is 25.'
print(text.title())
# Output: My Favorite Number Is 25.
text = '234 k3l2 *43 fun'
print(text.title())
# Output: 234 K3L2 *43 Fun


s = 'Python Is Good.'
print(s.istitle())
# Output: True
s = 'Python is good'
print(s.istitle())
# Output: False

message = 'python is fun'
print(message.upper())
# Output: PYTHON IS FUN

string = "THIS IS GOOD!"
print(string.isupper());
# Output: True
string = "THIS IS not GOOD!"
print(string.isupper());
# Output: False


text = ['Python', 'is', 'a', 'fun', 'programming', 'language']
print(' '.join(text))
# Output: Python is a fun programming language


string = 'cat'
width = 5
print(string.ljust(width))
# Output: cat  


message = 'PYTHON IS FUN'
print(message.lower())
# Output: python is fun


random_string = '   this is good ';
print(random_string.lstrip())
# Output:this is good 
print(random_string.lstrip('sti'))
# Output:  this is good 
print(random_string.lstrip('s ti'))
# Output:his is good 
website = 'https://www.programiz.com/'
print(website.lstrip('htps:/.'))
# Output:www.programiz.com/


text = 'bat ball'
replaced_text = text.replace('ba', 'ro')
print(replaced_text)
# Output: rot roll


cars = 'BMW-Telsa-Range Rover'
print(cars.split('-'))
# Output: ['BMW', 'Tesla', 'Range Rover']




