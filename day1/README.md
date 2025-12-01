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
