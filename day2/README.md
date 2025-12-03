## Day 2

### Problem Description

Day 2 involves identifying "invalid IDs" from ranges of numbers. An invalid ID is a number that follows a "doubled pattern" – where the first half of the digits is exactly the same as the second half (e.g., `1212`, `123123`, `5050`).

Given a series of numeric ranges, we need to find all numbers that match this pattern and calculate their sum.

### Solution Approach

1. **Input Parsing**: The input consists of comma-separated ranges in the format `start-end` (e.g., `100-200,500-600`).
2. **Pattern Detection**: For each number in the ranges:
   - Convert the number to a string
   - Check if the string length is even (a requirement for the doubled pattern)
   - Split the string in half and compare the first half to the second half
   - If they match, the number is an "invalid ID"
3. **Goal**: Sum all numbers that match the doubled pattern across all ranges.

### Key Concepts

- **String Manipulation**: Converting numbers to strings and splitting them for pattern matching
- **Range Processing**: Parsing and iterating through multiple numeric ranges from the input
- **Pattern Matching**: Identifying when the first half of a number's digits equals the second half

### Algorithm Details

The `is_invalid_id` function checks if a number follows the doubled pattern:

```python
def is_invalid_id(num):
    s = str(num)
    n = len(s)
    
    # Check if the number length is even
    if n % 2 != 0:
        return False
    
    half = n // 2
    return s[:half] == s[half:]
```

For example:
- `1212` → `"12"` == `"12"` → **True** (invalid ID)
- `123123` → `"123"` == `"123"` → **True** (invalid ID)
- `12345` → odd length → **False** (valid ID)
- `1234` → `"12"` != `"34"` → **False** (valid ID)

### Example

Given the range `1000-1100`:
- `1010` is an invalid ID (`"10"` == `"10"`)
- Other numbers in this range either have odd lengths or non-matching halves

### Files

- `day2.py`: Solution implementation
- `day2input.txt`: Puzzle input containing comma-separated ranges
