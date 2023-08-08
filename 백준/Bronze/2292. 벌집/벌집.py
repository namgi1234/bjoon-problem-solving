n = int(input())
num_of_house = 1
count = 1

# while True:
#     if n < num_of_house:
#         print(count)
#         break
#     else:
#         num_of_house += 6 * count
#         count += 1
while n > num_of_house:
    num_of_house += 6*count
    count +=1
print(count)