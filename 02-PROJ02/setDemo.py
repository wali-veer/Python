family=set(['Raj','baba','mom','akka','roopa','vijay'])
teammate=set(['vijay','rahul','siva'])
college=set(['siva','vijay'])

print(family)
print(teammate)
print(college)

print(len(family))
print(len(teammate))
print(len(college))
print(family.union(teammate, college))
print(len(family.union(teammate,college)))
print(family.intersection(teammate,college))
print(family.difference(teammate))
print(family.symmetric_difference(teammate))
print(teammate.symmetric_difference(family))

print('Vijay' in family )
print('vijay' in family )

family.add('Santosh')
print(family)

college.remove('siva')
print(college)

college.pop()
print(college)

college.pop()
print(college)
