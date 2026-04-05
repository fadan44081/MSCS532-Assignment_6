import random
import time


# ============================================================
# RANDOMIZED QUICKSELECT (EXPECTED O(n))
# ============================================================

def randomized_quickselect(arr, k):
    """
    Returns the k-th smallest element using Randomized Quickselect.

    Parameters:
        arr (list): Input list of numbers
        k (int): 1-based index of the desired element

    Returns:
        int/float: The k-th smallest element

    Raises:
        ValueError: If the array is empty or k is out of bounds
    """

    # Check whether the input array is empty
    if not arr:
        raise ValueError("Array must not be empty.")

    # Check whether k is valid
    if k < 1 or k > len(arr):
        raise ValueError("k is out of bounds.")

    # Call the recursive helper function
    return quickselect(arr, k)


def quickselect(arr, k):
    """
    Recursive helper function for Randomized Quickselect.

    Parameters:
        arr (list): Current subarray being processed
        k (int): 1-based index of the desired smallest element

    Returns:
        int/float: The k-th smallest element
    """

    # Base case: if there is only one element, return it
    if len(arr) == 1:
        return arr[0]

    # Choose a random pivot from the array
    pivot = random.choice(arr)

    # Partition the array into three groups:
    # values smaller than pivot, equal to pivot, and greater than pivot
    lows = [x for x in arr if x < pivot]
    pivots = [x for x in arr if x == pivot]
    highs = [x for x in arr if x > pivot]

    # If the k-th smallest element is in the lower partition, recurse there
    if k <= len(lows):
        return quickselect(lows, k)

    # If k falls inside the pivot group, the pivot is the answer
    elif k <= len(lows) + len(pivots):
        return pivot

    # Otherwise, recurse into the higher partition with adjusted k
    else:
        new_k = k - len(lows) - len(pivots)
        return quickselect(highs, new_k)


# ============================================================
# DETERMINISTIC SELECTION (MEDIAN OF MEDIANS) — WORST-CASE O(n)
# ============================================================

def deterministic_select(arr, k):
    """
    Returns the k-th smallest element using the deterministic
    Median of Medians selection algorithm.

    Parameters:
        arr (list): Input list of numbers
        k (int): 1-based index of the desired element

    Returns:
        int/float: The k-th smallest element

    Raises:
        ValueError: If the array is empty or k is out of bounds
    """

    # Check whether the input array is empty
    if not arr:
        raise ValueError("Array must not be empty.")

    # Check whether k is valid
    if k < 1 or k > len(arr):
        raise ValueError("k is out of bounds.")

    # Call the recursive helper function
    return median_of_medians_select(arr, k)


def median_of_medians_select(arr, k):
    """
    Recursive helper function for deterministic selection.

    This function chooses a pivot using the Median of Medians strategy,
    which guarantees good enough partitions to achieve worst-case O(n).

    Parameters:
        arr (list): Current subarray being processed
        k (int): 1-based index of the desired smallest element

    Returns:
        int/float: The k-th smallest element
    """

    # Base case:
    # If the array is small, sort it directly and return the answer
    if len(arr) <= 5:
        sorted_arr = sorted(arr)
        return sorted_arr[k - 1]

    # Divide the array into groups of at most 5 elements
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Find the median of each group
    medians = []
    for group in groups:
        sorted_group = sorted(group)
        median = sorted_group[len(sorted_group) // 2]
        medians.append(median)

    # Recursively find the median of the medians
    pivot = median_of_medians_select(medians, (len(medians) + 1) // 2)

    # Partition the array around the chosen pivot
    lows = [x for x in arr if x < pivot]
    pivots = [x for x in arr if x == pivot]
    highs = [x for x in arr if x > pivot]

    # Recurse into the correct partition
    if k <= len(lows):
        return median_of_medians_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        new_k = k - len(lows) - len(pivots)
        return median_of_medians_select(highs, new_k)


# ============================================================
# EMPIRICAL ANALYSIS HELPER FUNCTIONS
# ============================================================

def generate_test_array(size, distribution_type):
    """
    Generates a test array based on the requested distribution.

    Parameters:
        size (int): Number of elements in the array
        distribution_type (str): 'random', 'sorted', or 'reverse'

    Returns:
        list: Generated array
    """

    # Generate a random array with values in a fixed range
    if distribution_type == "random":
        return [random.randint(1, 100000) for _ in range(size)]

    # Generate an already sorted array
    elif distribution_type == "sorted":
        return list(range(1, size + 1))

    # Generate a reverse-sorted array
    elif distribution_type == "reverse":
        return list(range(size, 0, -1))

    # Reject invalid distribution names
    else:
        raise ValueError("Invalid distribution type. Use 'random', 'sorted', or 'reverse'.")


def measure_execution_time(algorithm, arr, k, trials=5):
    """
    Measures the average execution time of a selection algorithm.

    Parameters:
        algorithm (function): Selection algorithm to test
        arr (list): Input array
        k (int): 1-based order statistic to find
        trials (int): Number of repeated runs

    Returns:
        float: Average execution time in seconds
    """

    total_time = 0.0

    # Run the algorithm multiple times for a more reliable average
    for _ in range(trials):
        # Make a copy so each trial uses the same input
        arr_copy = arr.copy()

        # Start timing
        start_time = time.perf_counter()

        # Run the algorithm
        algorithm(arr_copy, k)

        # End timing
        end_time = time.perf_counter()

        # Add elapsed time to the total
        total_time += (end_time - start_time)

    # Return the average time
    return total_time / trials


def run_empirical_analysis():
    """
    Runs an empirical comparison between Randomized Quickselect
    and Deterministic Selection on different array sizes
    and input distributions.
    """

    # Input sizes to test
    sizes = [100, 1000, 5000, 10000]

    # Types of input distributions to test
    distributions = ["random", "sorted", "reverse"]

    # Number of repeated runs per test
    trials = 5

    print("\n=== EMPIRICAL ANALYSIS ===")
    print(f"{'Size':<10}{'Distribution':<15}{'Quickselect (s)':<20}{'Deterministic (s)':<20}")

    # Test every size against every distribution
    for size in sizes:
        for distribution in distributions:
            # Generate the test array
            arr = generate_test_array(size, distribution)

            # Choose the median position using 1-based indexing
            k = (len(arr) + 1) // 2

            # Measure average execution time for Randomized Quickselect
            quickselect_time = measure_execution_time(
                randomized_quickselect, arr, k, trials
            )

            # Measure average execution time for Deterministic Selection
            deterministic_time = measure_execution_time(
                deterministic_select, arr, k, trials
            )

            # Print the results in aligned columns
            print(f"{size:<10}{distribution:<15}{quickselect_time:<20.6f}{deterministic_time:<20.6f}")


# ============================================================
# TESTING SECTION
# ============================================================

if __name__ == "__main__":
    # Fix the random seed for reproducibility
    random.seed(42)

    # -------------------------------
    # Correctness tests: Quickselect
    # -------------------------------
    print("=== RANDOMIZED QUICKSELECT TESTS ===")

    # Test array with distinct values
    test_array = [7, 2, 9, 4, 1, 6, 3, 8, 5]
    print("Original array:", test_array)

    # Test every order statistic from 1 to n
    for k in range(1, len(test_array) + 1):
        result = randomized_quickselect(test_array, k)
        print(f"{k}-th smallest element: {result}")

    # Test array containing duplicate values
    duplicate_array = [4, 2, 5, 2, 8, 2, 9, 1]
    print("\nArray with duplicates:", duplicate_array)

    # Test every order statistic from 1 to n
    for k in range(1, len(duplicate_array) + 1):
        result = randomized_quickselect(duplicate_array, k)
        print(f"{k}-th smallest element: {result}")

    # -----------------------------------
    # Correctness tests: Deterministic
    # -----------------------------------
    print("\n=== DETERMINISTIC SELECTION TESTS ===")

    print("Original array:", test_array)

    # Test every order statistic from 1 to n
    for k in range(1, len(test_array) + 1):
        result = deterministic_select(test_array, k)
        print(f"{k}-th smallest element: {result}")

    print("\nArray with duplicates:", duplicate_array)

    # Test every order statistic from 1 to n
    for k in range(1, len(duplicate_array) + 1):
        result = deterministic_select(duplicate_array, k)
        print(f"{k}-th smallest element: {result}")

    # -------------------------------
    # Empirical analysis
    # -------------------------------
    run_empirical_analysis()