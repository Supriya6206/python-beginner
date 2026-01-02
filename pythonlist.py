
print("=== LIST OPERATIONS ===")
fruits_list = ["apple", "banana", "orange", "apple", "mango", "banana", "grape"]
print(f"Original list: {fruits_list}")
print(f"Length of list: {len(fruits_list)}")
print(f"First fruit: {fruits_list[0]}")
print(f"Last fruit: {fruits_list[-1]}")

# Add items to list
fruits_list.append("kiwi")
print(f"After adding kiwi: {fruits_list}")

# Using Sets - removes duplicates and unordered
print("\n=== SET OPERATIONS ===")
fruits_set = set(fruits_list)
print(f"Converted to set (duplicates removed): {fruits_set}")
print(f"Length of set: {len(fruits_set)}")

# Set operations with two sets
set_a = {"apple", "banana", "orange", "mango"}
set_b = {"orange", "grape", "kiwi", "mango"}

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")

# Union - all unique elements from both sets
print(f"Union (A | B): {set_a | set_b}")

# Intersection - common elements in both sets
print(f"Intersection (A & B): {set_a & set_b}")

# Difference - elements in A but not in B
print(f"Difference (A - B): {set_a - set_b}")

# Symmetric Difference - elements in either A or B but not both
print(f"Symmetric Difference (A ^ B): {set_a ^ set_b}")

# Practical Example: Finding unique visitors
print("\n=== PRACTICAL EXAMPLE ===")
daily_visitors = ["John", "Sarah", "Mike", "John", "Emma", "Sarah", "John", "David"]
print(f"Daily visitors log: {daily_visitors}")
print(f"Total visits: {len(daily_visitors)}")

unique_visitors = set(daily_visitors)
print(f"Unique visitors: {unique_visitors}")
print(f"Number of unique visitors: {len(unique_visitors)}")

# Convert back to sorted list
sorted_visitors = sorted(list(unique_visitors))
print(f"Sorted unique visitors list: {sorted_visitors}")
