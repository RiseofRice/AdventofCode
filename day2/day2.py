def is_invalid_id(num):
    """
    Checks if a number is a 'doubled pattern'.
    """
    s = str(num)
    n = len(s)
    
    # Check if the number length is even
    if n % 2 != 0:
        return False
    
    half = n // 2
    return s[:half] == s[half:]


def solve_day2(input_string):
    ranges = input_string.strip().split(',')
    total_sum = 0
    found_count = 0

    print("Starting calculation...\n")

    for range_str in ranges:
        if not range_str:
            continue
        start_str, end_str = range_str.split('-')
        start = int(start_str)
        end = int(end_str)

        # Pre-calculate string representations to avoid repeated conversions
        for num in range(start, end + 1):
            s = str(num)
            n = len(s)
            
            # Inline the check to avoid function call overhead
            if n % 2 == 0:
                half = n // 2
                if s[:half] == s[half:]:
                    total_sum += num
                    found_count += 1
                
        print(f"Finished: {start}-{end} (total of {found_count} invalid IDs so far)")

    print("\n" + "="*50)
    print(f"All ranges searched!")
    print(f"Number of invalid IDs: {found_count}")
    print(f"Sum of all invalid IDs: {total_sum}")
    print("="*50)
    return total_sum

def read_input():
    with open("day2input.txt") as f:
        return f.read()

if __name__ == "__main__":
    puzzle_input = read_input()
    result = solve_day2(puzzle_input)
    print(f"\n{result}")