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

# result------------  {1, 2, 3, 5, 6, 7} {3, 6, 7}


##################Intersection Method------

cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities.intersection(cities2)
print(cities3)

# result------------  {'Tokyo', 'Madrid'}

cities.intersection_update(cities2)
print(cities)

# result------------  {'Tokyo', 'Madrid'}


cities3=cities.symmetric_difference(cities2)
print(cities3)

# result------------  {'Berlin', 'Delhi', 'Kabul', 'Seoul'}

cities.symmetric_difference_update(cities2)
print(cities)

# result------------  {'Berlin', 'Delhi', 'Kabul', 'Seoul'}
