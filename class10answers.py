#######################################################################################
# 10.1
list = []
print(list)

#######################################################################################
# 10.2
list = [1,2,3,4,5]
print(str(list[1]) + ' ' + str(list[4]))


#######################################################################################
# 10.3
list = [1,2,3,4]
print(str(list[-1]))

#######################################################################################
# 10.4
list = [True, 1, 5.3, 'Hello']
print(list)


#######################################################################################
# 10.5
list = [[1, True], ['Hello', 2.5], [1, 2.4]]
for i in range(len(list)):
    print(list[i])

#######################################################################################
# 10.6
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[2:5])

#######################################################################################
# 10.7
list = [1,2,'Hello',True,5.3]
print(len(list))

#######################################################################################
# 10.8
list = [1,2,3,4,5]
print(list)
list[0]=2
list[1]=3
print(list)

#######################################################################################
# 10.9
list = [10,20,30,40,50]
for i in range(len(list)):
    print(list[i])

#######################################################################################
# 10.10
list = [10,20,30,40,50]
for i in list:
    print(i)

#######################################################################################
# 10.11
list = [1,2,3,4,5]
for i in range(len(list)):
    list[i]+=1
print(list)

#######################################################################################
# 10.12
list1 = [1,2,3,4]
list2 = [5,6,7,8]
list1+=list2
print(list1)

#######################################################################################
# 10.13
list = [1,2,3,4,5]
print(list[4])
del list[4]
print(list[3])
del list[3]
print(list)


#######################################################################################
# 10.14
list = [1,2,3,4,5]
if 1 in list:
    print(str(1) + ' is in the list')
else:
    print(str(1) + ' is not in the list')

if 6 in list:
    print(str(6) + ' is in the list')
else:
    print(str(6) + ' is not in the list')
