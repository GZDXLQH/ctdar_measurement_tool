# for x in range(10):
#     for y in range(10):
#         print(x*y)
#         if x*y > 50:
#             break
#     else:
#         continue    # only executed if the inner loop DID NOT break
#     break    # only executed if the inner loop DID break


# # a = [1, 1, 3, 1, 5, 1, 1, 1, 1]
# a = [1, 3, 1, 1]
# b = [1, 1, 3, 1, 1, 1, 1]
# index = 0
# for aa in a:
#     for bb in b:
#         print(index)
#         index += 1
#         if aa == 3:
#             print("found")
#             break
#     else:
#         continue


my_list = [1, 3, 4, 5, 7, 8, 2, 11, 19]
for c, value in enumerate(my_list, 0):
    # print(c, value)
    print(value)

