s={2,4,2,6}
print(s)

# result---------{2, 4, 6}

info={"Carla",19, False, 5.9,19}
print(info)

# result-------{False, 'Carla', 19, 5.9}

harry=set()
print(type(harry))

# result------- <class 'set'>


for value in info:
    print(value)

 #result-------- False
 #               Carla
 #                19
 #                5.9



##################Union Method------

s1={1,2,5,6}
s2={3,6,7}
s3=s1.union(s2)
print(s3)

# result------------{1, 2, 3, 5, 6, 7}


s1.update(s2)
print(s1)

# result------------  {1, 2, 3, 5, 6, 7} 


##################Intersection Method------

cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities.intersection(cities2)
print(cities3)

# result------------  {'Tokyo', 'Madrid'}

cities.intersection_update(cities2)
print(cities)

# result------------  {'Tokyo', 'Madrid'}


##################Symmetric Method------


cities3=cities.symmetric_difference(cities2)
print(cities3)

# result------------  {'Berlin', 'Delhi', 'Kabul', 'Seoul'}

cities.symmetric_difference_update(cities2)
print(cities)

# result------------  {'Berlin', 'Delhi', 'Kabul', 'Seoul'}


##################Difference Method------

cities3=cities.difference(cities2)
print(cities3)

# result------------   {'Berlin', 'Delhi'}


cities.difference_update(cities2)
print(cities3)

# result------------   {'Berlin', 'Delhi'}


##################isdisjoint Method------


#if even single value is common will return false else true
values1={"vishal","arjun","shubham","vikas"}
values2={"vishal","nishtha","sakshi","arjun"}

print(values1.isdisjoint(values2));

# result------------   False


values3={"vishal1","arjun1","shubham","vikas"}
values4={"vishal","nishtha","sakshi","arjun"}

print(values3.isdisjoint(values4))

# result------------   True


################## issuperset Method------


#if values of child set are present in parent set then return true else false
values3={"vishal","arjun","shubham","vikas"}
values4={"nishtha","sakshi"}

print(values3.issuperset(values4))

# result------------   False


values3={"vishal","arjun","shubham","vikas"}
values4={"vishal","arjun"}


print(values3.issuperset(values4))

#result------------   True


################## isubset Method------

values3={"vishal","arjun","shubham","vikas"}
values4={"vishal","arjun"}

print(values4.issubset(values3))

#result------------   True


################## add Method------

data1={"r1","r2","r3","r4"}
data1.add("helsinki")
print(data1)

#result------------   {'r4', 'helsinki', 'r1', 'r3', 'r2'}


################## update Method------


data1={"r1","r2","r3","r4"}
data1.update({"helsinki","tokyo","berlin"})
print(data1)

#result------------   {'berlin', 'r1', 'helsinki', 'r4', 'r3', 'tokyo', 'r2'}


################## remove/discard Method------


data1={"r1","r2","r3","r4"}
data1.discard("r3")
print(data1)

#result------------   {'r1', 'r2', 'r4'}

################## pop Method------


data1={"r1","r2","r3","r4"}
data1.pop()
print(data1)

#result------------   {'r3', 'r2', 'r4'}


################## clear Method------

data1={"r1","r2","r3","r4"}
data1.clear()
print(data1)

#result------------   set()




