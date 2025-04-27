def AND_OR_Gate():
    while True:
        print("\nWelcome to the System!")
        print("1. Office Door Access (AND Gate)")
        print("2. Street Lights Control (OR Gate)")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "3":
            print("\nExiting system. Goodbye!")
            break

        if choice == "1":  # AND Gate Simulation
            id_card = input("Valid Employee ID? (yes/no): ").lower()
            fingerprint = input("Fingerprint Match? (yes/no): ").lower()

            if id_card == "yes" and fingerprint == "yes":
                print("\nAccess Granted. Welcome!")
            else:
                print("\nAccess Denied. Both conditions must be true.")

        elif choice == "2":  # OR Gate Simulation
            night_time = input("Is it night time? (yes/no): ").lower()
            motion_detected = input("Motion detected? (yes/no): ").lower()

            if night_time == "yes" or motion_detected == "yes":
                print("\nStreet lights ON.")
            else:
                print("\nStreet lights OFF.")

        else:
            print("\nInvalid choice. Please try again.")

AND_OR_Gate()


# import random 

# goal_state = [ [1,2,3], [4,5,6], [7,8,0] ]

# def generate_puzzle():
#     nums = [0,1,2,3,4,5,6,7,8]
#     random.shuffle(nums)
#     return [nums[:3], nums[3:6], nums[6:9]]


# def find_zero(state):
#     for i in range(3):
#         for j in range(3):
#              if state[i][j] == 0:
#                 return i,j


# def print_puzzle(state):
#     for row in state:
#         print("".join(str(num) if num != 0 else "_" for num in row))
#     print()

# def move(state,direction):
#     i,j = find_zero(state)

#     new_state = [row[:] for row in state]

#     if direction == "up" and i > 0:
#         new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]
#     elif direction == "down" and i < 2:
#         new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]
#     elif direction == "left" and j > 0:
#         new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
#     elif direction == "right" and j < 2 :
#         new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
#     else :
#         print("Invalid move!")
#     return new_state

# puzzle = generate_puzzle()

# while puzzle != goal_state:
#     print_puzzle(puzzle)
#     move_direction = input("Move (up/down/left/right): ").strip().lower()
#     puzzle = move(puzzle,move_direction)

# print_puzzle(puzzle)
# print('Congratulation! You solved it!')

# *** Task 2 ***
# cities = {
#     "Murree": ["Islamabad"],
#     "Islamabad": ["Murree", "Rawalpindi"],
#     "Rawalpindi": ["Islamabad", "Kallar Kahar"],
#     "Kallar Kahar": ["Rawalpindi", "Chakwal"],
#     "Chakwal": ["Kallar Kahar", "Sargodha"],
#     "Sargodha": ["Chakwal", "Faisalabad"],
#     "Faisalabad": ["Sargodha", "Lahore"],
#     "Lahore": ["Faisalabad", "Multan"],
#     "Multan": ["Lahore", "Sukkur"],
#     "Sukkur": ["Multan", "Hyderabad"],
#     "Hyderabad": ["Sukkur", "Karachi"],
#     "Karachi": []
# }

# current_city = "Lahore"
# goal_city = "Karachi"

# print("Welcome to the city path finder game!")
# print(f"You are starting in {current_city}. Try to reach {goal_city}.\n")


# while current_city != goal_city:
#     print(f"Ypu are currently in {current_city}")
#     print(f"Possible cities to move to : {', '.join(cities[current_city])}")

#     move = input("Where would you likke to move? ").strip()

#     if move in cities[current_city]:
#         current_city = move
#         print(f"Moving to {current_city}... \n")
#     else:
#         print("You can only move to cities directly connected to your current city. \n")

# print(f'Congratulation! You reached {goal_city}!')