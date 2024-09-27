# def Average(lst): 
#     return sum(lst) / len(lst) 

# # Driver Code 
# lst = [15, 9, 55, 41, 35, 20, 62, 49] 
# average = Average(lst) 

# # Printing average of the list 
# print("Average of the list =", round(average, 2)) 

numbers = input("Enter numbers separated by spaces: ")
number_list = [float(n) for n in numbers.split()]

average = sum(number_list) / len(number_list)
largest = max(number_list)
smallest = min(number_list)

print(f"The average is: {average}")
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")