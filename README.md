# Advent of Code 2025

A collection of solutions for [Advent of Code 2025](https://adventofcode.com/) challenges.

## Day 1

### Problem Description

Day 1 involves simulating a circular position tracker. Given a series of movement instructions, we need to track a position on a circular track of 100 positions (0-99) and count how many times the position lands exactly on 0.

### Solution Approach

1. **Starting Position**: The position starts at 50 on a circular track of 100 positions.
2. **Movement Instructions**: Each instruction consists of:
   - A direction: `R` (right/clockwise) or `L` (left/counter-clockwise)
   - A number of steps to move
3. **Position Calculation**: The position wraps around using modulo 100 arithmetic:
   - Moving right: `position = (position + steps) % 100`
   - Moving left: `position = (position - steps) % 100` (Python's modulo handles negative numbers correctly)
4. **Goal**: Count how many times the position equals 0 after processing an instruction.

### Key Concepts

- **Modular Arithmetic**: Used to handle the circular nature of the track
- **File Parsing**: Reading and parsing movement instructions from an input file

### Files

- `day1/day1.py`: Solution implementation
- `day1/day1input.txt`: Puzzle input

## Day 2

### Problem Description

Day 2 involves identifying "invalid IDs" from ranges of numbers. An invalid ID is a number that follows a "doubled pattern" – where the first half of the digits is exactly the same as the second half (e.g., `1212`, `123123`, `5050`).

### Solution Approach

1. **Input Parsing**: The input consists of comma-separated ranges (e.g., `100-200,500-600`).
2. **Pattern Detection**: For each number in the ranges:
   - Convert the number to a string
   - Check if the length is even (required for a doubled pattern)
   - Compare the first half of the digits to the second half
3. **Goal**: Sum all numbers that match the doubled pattern across all ranges.

### Key Concepts

- **String Manipulation**: Splitting numbers into halves for pattern matching
- **Range Processing**: Iterating through multiple numeric ranges efficiently

### Files

- `day2/day2.py`: Solution implementation
- `day2/day2input.txt`: Puzzle input
