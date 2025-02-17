#list = [1, 2,3]
#list2 =[i for i in list]
#list2.append(4)
#print(list)
#print(list2)
# def square_sum(list1):
# # 	total = 0
# # 	square = 1
# # 	for i in list1:
# # 		#print(i)
# # 		square =i * i
# # 		total += square
# # 	return total
	
# print(square_sum([1,2]))
# def square_sum(list1):
#     list2 = sum([i*i for i in list1])
#     return list2
	
# print(square_sum([1,2]))

# remove duplicate lists
# def remove_duplicates(list1):
#     # return list(set(list1))
#     result = []
#     for item in list1:
#         if item not in result:
#             result.append(item)
#     return result


# remve_duplicates = remove_duplicates([1,2,1,3,2,4,5])
# print(remve_duplicates)

# # have_common_members
# def have_common_members(list1,list2):
#     for item1 in list1:
#         for item2 in list2:
#             if item1 == item2:
#                 return True
#     return False
#     # return not set(list1).isdisjoint(set(list2))
# print(have_common_members(['apple','lion','xamda','orange'], ['cananaas','bur','moos','orange']))
# print(have_common_members(['apple','lion','xamda'], ['cananaas','bur','moos','orange']))
