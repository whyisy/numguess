from random import shuffle, choice

# Set result dictionary
result = {
        'stay_to_win': 0,
        'move_to_win': 0,
}
#Create doors with 0s and 1.
doors = [0,0,1] # 0: goat, 1: sports car

# Let User decide to running number
iter_num = int(input("Enter some num(100-10000): "))

# Start iteration
for _ in range(iter_num):
    # Shuffle doors
    shuffle(doors)
    #print(doors)
    # Choose 1 random door
    user_choice = choice(doors)
    #print(user_choice)
    # Count Winning possibility
    if user_choice==0:
        result['move_to_win'] += 1
    else:
        result['stay_to_win'] += 1

print("{} times run: stay-{stay_to_win} switch-{move_to_win}".format(iter_num, **result))
