# list=[1,2,3,4,5]

# def add(list):
#     total=0;
#     for i in list:
#         total+=i
#     return total
    
# print(add(list))

# dictionary={
#     "name":"vishal",
#     "city":"lucknow"
# }

# for keys,values in dictionary.items():
#     print(keys,values)

# radius=float(input("Enter radius"))

# def circleArea(radius):
#     area=3.14*radius*radius
#     return area;

# print(circleArea(radius))

# def printUser():
#     firstName=input("Enter firstName");
#     lastName=input("Enter lastName");
#     print(lastName +" " + firstName)

# printUser()


# import calendar
# y = int(input("Input the year : "))
# m = int(input("Input the month : "))
# print(calendar.month(y,m))

# def includesNumber(list,n):
#     cond=False;
#     for value in list:
#         if n==value:
#             cond=True;
#         else:
#             cond;
#     return cond;

# print(includesNumber([1,2,3,4,5],4))

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]

# inputValue=float(input("Enter Your value"))

# def evenAndBreak(numbers,inputValue):
#     for i in numbers:
#         if i==237:
#             print(i)
#             break;
#         elif i%2==0:
#             print(i)
#     return i


# print(evenAndBreak(numbers,inputValue))

# def sumThree(x,y,z):
#     sum=0;
#     if x==y or y==z or x==z  :
#        return sum;
#     else:
#         sum=x+y+z;
#     return sum;

# print(sumThree(1,2,2))


# def inRangessss(x,y):
#     sum=0
#     sum=x+y;
#     if sum in range(15,20):
#         sum=20
#     return sum;

# print(inRangessss(6,9))


# def differenceSeventeen(a):
#     diff =17-a
#     if a>17:
#         diff*2
#     return diff;


# print(differenceSeventeen(18));

# def EvenOrOdd(num):
#     str=""
#     if num%2==0:
#         str="Even";
#     else:
#         str="Odd";
#     return str;
        
# print(EvenOrOdd(8));

items=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5];

# def occurences():
#     dict={}
#     for item in items:
#        if item in dict:
#               dict[item]+=1;
#        else:
#               dict[item]=1
#     return dict;

# print(occurences());

# def vowel(letter):
#     vowels=["a","e","i","o","u"]
#     for vowel in vowels:
#         if vowel in letter:
#             return True;
#         else:
#             return False;

# print(vowel("c"));
items =[1,5,8,3]

# def containValues(items,num):
#     for item in items:
#         if item==num:
#             return True; 
#     return False;

# print(containValues(items,4));

# def mult(x,y):
#     res=x*x+y*y+2*x*y
#     return res;

# print(mult(2,3))


#40
# import struct
# print(struct.calcsize("P") * 8)

def printVal(x,y):
    return   (x, y, x+y)

print(printVal(30,20))