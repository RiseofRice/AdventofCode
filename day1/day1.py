instructions = []
def gettingData(type=list):
    with open("day1input.txt") as f:
        data = f.read().splitlines()
        instructions.extend(data)
        return instructions

def solvingDay1():
    position = 50
    count = 0

    instructions = gettingData()
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        
        if direction == 'R':
            position = (position + steps) % 100
        elif direction == 'L':
            position = (position - steps) % 100
        

        if position == 0:
            count += 1
    
    print(count)

solvingDay1()




