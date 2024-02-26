class Chocolate:
    def __init__(self, weight, price, type):
        # Initialize a Chocolate object with weight, price, and type attributes
        self.weight = weight
        self.price = price
        self.type = type

    def __str__(self):
        # String representation of Chocolate object
        return f"Chocolate(type='{self.type}', weight={self.weight}, price={self.price})"

def compare_chocolates(chocolate):
    # Comparison function for sorting chocolates by price
    return chocolate.price

def merge_sort(arr):
    """Merge sort algorithm to sort chocolates based on price."""
    if len(arr) <= 1:  # Base case: if the list has 1 or 0 elements, it's already sorted
        return arr

    mid = len(arr) // 2  # Find the middle index of the list
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half of the list
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half of the list

    return merge(left_half, right_half)  # Merge the sorted halves

def merge(left, right):
    """Merge two sorted lists into a single sorted list."""
    merged = []  # Initialize an empty list to store the merged result
    left_index = right_index = 0  # Initialize indices for left and right lists

    # Iterate until one of the lists is exhausted
    while left_index < len(left) and right_index < len(right):
        # Compare elements from both lists and append the smaller one to the merged list
        if compare_chocolates(left[left_index]) < compare_chocolates(right[right_index]):
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left and right lists
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged  # Return the merged list

def distribute_chocolates_iterative(chocolates, students):
    """Distribute chocolates to students iteratively."""
    # Sort chocolates based on price using merge sort
    chocolates_sorted = merge_sort(chocolates)

    # Create an empty dictionary to store distribution of chocolates to students
    distribution = {}

    # Iterate over each student and assign them a chocolate
    for i in range(len(students)):
        distribution[students[i]] = chocolates_sorted[i]

    return distribution

def distribute_chocolates_recursive(chocolates, students):
    """Distribute chocolates to students recursively."""
    # Base case: if no chocolates or no students, return empty distribution
    if not chocolates or not students:
        return {}

    # Sort chocolates based on price using merge sort
    chocolates_sorted = merge_sort(chocolates)

    # Create an empty dictionary to store distribution of chocolates to students
    distribution = {}

    # Assign the first chocolate to the first student
    distribution[students[0]] = chocolates_sorted[0]

    # Recursively distribute remaining chocolates to remaining students
    remaining_distribution = distribute_chocolates_recursive(chocolates_sorted[1:], students[1:])

    # Merge the remaining distribution with the current distribution
    distribution.update(remaining_distribution)

    return distribution

# Sorting chocolates by weight and price after distribution
def sort_chocolates_by_weight(chocolates):
    def get_weight(chocolate):
        return chocolate.weight
    return sorted(chocolates, key=get_weight)

def sort_chocolates_by_price(chocolates):
    def get_price(chocolate):
        return chocolate.price
    return sorted(chocolates, key=get_price)

# Function to search for a specific chocolate by price or weight
def search_chocolate(chocolates, key, value):
    """Search for a chocolate with specified price or weight."""
    for chocolate in chocolates:
        if key == 'price' and chocolate.price == value:
            return chocolate
        elif key == 'weight' and chocolate.weight == value:
            return chocolate
    return None

chocolates = [Chocolate(10, 5, 'dark'), Chocolate(15, 7, 'milk'), Chocolate(8, 3, 'white'), Chocolate(12, 6, 'coconut'), Chocolate(18, 8, 'caramel'), Chocolate(9, 4, 'hazelnut'), Chocolate(20, 10, 'white'), Chocolate(7, 2, 'dark'), Chocolate(14, 5, 'milk'), Chocolate(11, 7, 'coconut')]

# Test Case for searching for a chocolate by price or weight
print("\nSearch for a chocolate by price or weight:")
searched_chocolate = search_chocolate(chocolates, 'price', 6)
if searched_chocolate:
    print("Found chocolate:", searched_chocolate)
else:
    print("Chocolate not found.")

print("\nSearch for a chocolate by price:")
searched_chocolate = search_chocolate(chocolates, 'price', 3)
if searched_chocolate:
    print("Found chocolate:", searched_chocolate)
else:
    print("Chocolate not found.")

print("\nSearch for a chocolate by weight:")
searched_chocolate = search_chocolate(chocolates, 'weight', 15)
if searched_chocolate:
    print("Found chocolate:", searched_chocolate)
else:
    print("Chocolate not found.")

print("\nSearch for a chocolate that doesn't exist (eg. price=20):")
searched_chocolate = search_chocolate(chocolates, 'price', 20)
if searched_chocolate:
    print("Found chocolate:", searched_chocolate)
else:
    print("Chocolate not found.")