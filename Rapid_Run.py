import random
import copy

# The list to carry all the dictionaries
horses = []

# Declaring global variables
winning_horses = []
selected_horses = {}
first_run = True
race_simulated = False

# Below function performs sorting in the horses list
def bubble_sort(horses):
    # The total number of horses in the list
    n = len(horses)
    
    # Goes through all the elements in the list
    for i in range(n - 1):
        # Last i elements are already in losses, so we don't need to check them
        for j in range(0, n - i - 1):
            # Converting 'id' to integers to perform numerical comparison
            if int(horses[j]['id']) > int(horses[j + 1]['id']):
                # The horses are swapped if they are in the wrong order
                horses[j], horses[j + 1] = horses[j + 1], horses[j]

# Below function adds a new horse to the list
def add_horse(horses):
    # To check whether the race has already started
    progress = input("\nEnter whether the race has 'STARTED' or 'NOT' : ").upper()

    # Checks whether there are invalid input
    if progress not in ['STARTED', 'NOT']:
        print("\nInvalid input. Please enter 'STARTED' or 'NOT'.\n")
        print("--------------------------------------------------------------------")
        return

    # Cannot add horse details if the race has started
    if progress == 'STARTED':
        print("\nCannot add horse details after the race has started.\n")
        print("--------------------------------------------------------------------")
        return

    # Prompt statements to get the user input
    while True:
        try:
            print("\n--------------------------------------------------------------------")
            id = input("Enter horse ID    : ")
            
            # To check if the id has digits or an error will be raised
            if not id.isdigit():
                raise ValueError("Invalid ID. Please enter a valid numeric ID.")

            # To check whether the horse id already exists
            if any(horse['id'] == id for horse in horses):
                raise ValueError("This ID already exists. Please use a different ID.")

            name = input("Enter horse name  : ")
            jockey = input("Enter jockey name : ")

            # Checks if the horse age has two digits
            while True:
                age = input("Enter horse age   : ")
                if age.isdigit() and 0 < int(age) < 31:
                    break
                else:
                    print("\nInvalid age. Please enter a valid positive integer for age.")

            breed = input("Enter horse breed : ")
            race_record = input("Enter race record : ")

            print("Enter horse group")
            group = input("(A, B, C, or D)   : ").upper()
            # Validation for the group input
            while group not in ['A', 'B', 'C', 'D']:
                print("\nInvalid group. Please enter A, B, C, or D.")
                group = input("Enter horse group : ").upper()

            # The new horse details are added to the list
            horses.append({
                'id': id,
                'name': name,
                'jockey': jockey,
                'age': age,
                'breed': breed,
                'race_record': race_record,
                'group': group
            })

            # To display the success in adding the new details
            print("--------------------------------------------------------------------")
            print("\nHorse added successfully.\n")
            print("--------------------------------------------------------------------")
            break

        # if the user provides invalid input
        except ValueError as e:
            print(f"\n{e}")

# Below function updates an existing horse
def update_horse(horses):
    progress = input("\nEnter whether the race has 'STARTED' or 'NOT' : ").upper()

    if progress not in ['STARTED', 'NOT']:
        print("\nInvalid input. Please enter 'STARTED' or 'NOT'.\n")
        print("--------------------------------------------------------------------")
        return

    # Cannot update horse details if the race has started
    if progress == 'STARTED':
        print("\nCannot update horse details after the race has started.\n")
        print("--------------------------------------------------------------------")
        return

    print("\n--------------------------------------------------------------------")
    # Prompt statement to get the id to be updated
    id = input("Enter the ID of the horse to update : ")

    # The user input id is compared with the ones in the list
    for horse in horses:
        if horse['id'] == id:
            # Prompt statements to enter the updated details
            horse['name'] = input("\nEnter new horse name  : ")
            horse['jockey'] = input("Enter new jockey name : ")

            while True:
                age = input("Enter new horse age   : ")
                if age.isdigit() and 0 < int(age) < 31:
                    horse['age'] = age
                    break
                else:
                    print("\nInvalid age. Please enter a valid positive integer for age.")

            horse['breed'] = input("Enter new horse breed : ")
            horse['race_record'] = input("Enter new race record : ")

            print("Enter new horse group")
            horse['group'] = input("(A, B, C, or D)       : ").upper()
            while horse['group'] not in ['A', 'B', 'C', 'D']:
                print("\nInvalid group. Please enter A, B, C, or D.")
                horse['group'] = input("Enter new horse group : ").upper()

            # To display the success in updating the details
            print("--------------------------------------------------------------------")
            print("\nHorse updated successfully.\n")
            print("--------------------------------------------------------------------")
            return
    else:
        # Error message to be shown if the user input id is not found
        print("\nHorse not found with the provided ID.")
        print("\n--------------------------------------------------------------------")

# Below function deletes an existing horse
def delete_horse(horses):
    progress = input("\nEnter whether the race has 'STARTED' or 'NOT' : ").upper()

    if progress not in ['STARTED', 'NOT']:
        print("\nInvalid input. Please enter 'STARTED' or 'NOT'.\n")
        print("--------------------------------------------------------------------")
        return

    # Cannot delete horse details if the race has started
    if progress == 'STARTED':
        print("\nCannot delete horse details after the race has started.\n")
        print("--------------------------------------------------------------------")
        return

    print("\n--------------------------------------------------------------------")
    # Prompt statement to get the id to be deleted
    id = input("\nEnter the ID of the horse to delete : ")
    
    # Goes through the list to find the horse with the provided id
    for i, horse in enumerate(horses):
        if horse['id'] == id:
            # Deletes the horse from the list
            del horses[i]
            
            # To display the success in deleting the details
            print("\n--------------------------------------------------------------------")
            print("\nHorse deleted successfully.\n")
            print("--------------------------------------------------------------------")
            return
    
    # Error message if horse not found in list
    print("\nHorse not found.")
    print("\n--------------------------------------------------------------------")

# Below function displays all the horses in the list
def view_horses(horses):
    # Displaying a table header for horse details
    print("\n=======================================================================================================")
    print("                                          HORSE DETAILS TABLE")
    print("=======================================================================================================")
    print("{:<10} {:<20} {:<20} {:<5} {:<15} {:<20} {:<5}".format(
        "ID", "Name", "Jockey", "Age", "Breed", "Race Record", "Group"))
    print("─" * 103)

    # The horses are sorted using the previously defined bubble sort function
    bubble_sort(horses)

    # The details of each horse is displayed using the sorted order
    for horse in horses:
        print("{:<10} {:<20} {:<20} {:<5} {:<15} {:<20}   {:<7}".format(
            horse['id'],
            horse['name'],
            horse['jockey'],
            horse['age'],
            horse['breed'],
            horse['race_record'],
            horse['group']
        ))
        print("─" * 103)
    print("\n--------------------------------------------------------------------")

# Below function saves the horse details to a text file
def save_to_text_file(horses):
    with open('horse_details.txt', 'w', encoding='utf-8') as file:
        file.write("=============================================================================================\n")
        file.write("                                    HORSE DETAILS TABLE\n")
        file.write("=============================================================================================\n\n")

        # The horses are sorted using Bubble Sort based on both the group and the ID
        def bubble_sort_by_group_and_id(horses):
            n = len(horses)
            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if (horses[j]['group'], int(horses[j]['id'])) > (horses[j + 1]['group'], int(horses[j + 1]['id'])):
                        horses[j], horses[j + 1] = horses[j + 1], horses[j]

        bubble_sort_by_group_and_id(horses)

        # The horses are grouped according to their group
        grouped_horses = {}
        for horse in horses:
            group = horse['group']
            if group not in grouped_horses:
                grouped_horses[group] = []
            grouped_horses[group].append(horse)

        # Function which performs bubble sort within each group
        def bubble_sort_within_group(grouped_horses):
            for horses_in_group in grouped_horses.values():
                n = len(horses_in_group)
                for i in range(n - 1):
                    for j in range(0, n - i - 1):
                        if int(horses_in_group[j]['id']) > int(horses_in_group[j + 1]['id']):
                            horses_in_group[j], horses_in_group[j + 1] = horses_in_group[j + 1], horses_in_group[j]

        # Bubble sort is performed within each group based on the ID
        bubble_sort_within_group(grouped_horses)

        # The groups are written to the file
        for group, horses_in_group in grouped_horses.items():
            file.write(f"{' ' * 38}{'=' * 14}\n{' ' * 41}Group {group}\n{' ' * 38}{'=' * 14}\n\n")
            
            # Header for each group is written
            file.write("{:<10} {:<20} {:<20} {:<5} {:<15} {:<20}\n".format(
                "ID",
                "Name",
                "Jockey",
                "Age",
                "Breed",
                "Race Record",
                "Group"
            ))
            file.write("─" * 92 + '\n')

            # In each group, the horses are written in the sorted order based on the ID
            for horse in horses_in_group:
                file.write("{:<10} {:<20} {:<20} {:<5} {:<15} {:<20}\n".format(
                    horse['id'],
                    horse['name'],
                    horse['jockey'],
                    horse['age'],
                    horse['breed'],
                    horse['race_record'],
                    horse['group']
                ))
                file.write("─" * 92 + '\n')

            file.write("\n")
    print("\n--------------------------------------------------------------------")

# Below function randomly selects four horses, one from each group
def select_four_horses(horses):
    global selected_horses  # Accessing the global variable
    selected_horses = {}

    grouped_horses = {}
    for horse in horses:
        group = horse['group']
        if group not in grouped_horses:
            grouped_horses[group] = []
        grouped_horses[group].append(horse)

    # To check if each group has at least one horse
    groups_with_horses = [group for group, horses_in_group in grouped_horses.items() if horses_in_group]
    empty_groups = [group for group in ['A', 'B', 'C', 'D'] if group not in groups_with_horses]

    # Checks if there are at least four groups with horses
    if len(groups_with_horses) >= 4:
        # One horse from each group is selected randomly
        for group, horses_in_group in grouped_horses.items():
            if horses_in_group:
                selected_horses[group] = random.choice(horses_in_group)

        return selected_horses, grouped_horses, empty_groups

    if empty_groups:
        if len(empty_groups) == 1:
            print()
        else:
            print()

    return {}, grouped_horses, empty_groups  # Returns an additional flag to indicating an error

# Below function displays the selected horses
def display_selected_horses(selected_horses):
    print("\n--------------------------------------------------------------------")
    print("\nSelected Horses from Each Group\n")
    print("{:<7} {:<10} {:<20} {:<20} {:<5} {:<15} {:<20}".format("Group", "ID", "Horse Name", "Jockey", "Age", "Breed", "Race Record"))
    print("─" * 103)

    # To perform sorting, selected horses are transferred to a list
    selected_horses_list = list(selected_horses.values())

    # The selected horses are sorted by group using bubble sort
    n = len(selected_horses_list)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if selected_horses_list[j]['group'] > selected_horses_list[j + 1]['group']:
                selected_horses_list[j], selected_horses_list[j + 1] = selected_horses_list[j + 1], selected_horses_list[j]

    # Information about each selected horse is displayed
    for group, horse in selected_horses.items():
        print("  {:<5} {:<10} {:<20} {:<20} {:<5} {:<15} {:<20}".format(
            group,
            horse['id'],
            horse['name'],
            horse['jockey'],
            horse['age'],
            horse['breed'],
            horse['race_record']
        ))

# Below function simulates a horse race and gives the winning horses
def simulate_race(selected_horses):
    global winning_horses, race_simulated
    print("\n--------------------------------------------------------------------")
    print("\nWinning Horses\n")

    # Making a copy of the selected horses to avoid modifying the original dictionary
    shuffled_horses = copy.deepcopy(list(selected_horses.values()))
    random.shuffle(shuffled_horses)

    for horse in shuffled_horses:
        # Generating a random race time for each selected horse
        horse['race_time'] = random.randint(0, 90)

    # Bubble Sort is performed, based on race times
    n = len(shuffled_horses)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if shuffled_horses[j]['race_time'] > shuffled_horses[j + 1]['race_time']:
                shuffled_horses[j], shuffled_horses[j + 1] = shuffled_horses[j + 1], shuffled_horses[j]

    # The winning horses are displayed in the desired format
    print("{:<6} {:<7} {:<7} {:<20} {:<3}".format("Rank", "Group", "ID", "Horse Name", "Time"))
    print("---------------------------------------------------")

    for i, horse in enumerate(shuffled_horses[:3]):
        rank_suffix = "st" if i == 0 else "nd" if i == 1 else "rd" if i == 2 else "th"
        rank = f"{i + 1}{rank_suffix}"
        print("{:<8} {:<5} {:<7} {:<20} {:<3}s".format
        (rank, horse['group'], horse['id'], horse['name'], horse['race_time']))

    # Setting race_simulated to 'True'
    race_simulated = True

    # Returns the sorted list of the winning horses
    return shuffled_horses

# Below function visualizes the winning horses based on their race times
def visualize_winning_horses(winning_horses):
    print("\n--------------------------------------------------------------------")
    print("\nVisualizing Winning Horses\n")

    # The winning horses are sorted based on their race times using Bubble Sort
    n = len(winning_horses)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if winning_horses[j]['race_time'] > winning_horses[j + 1]['race_time']:
                winning_horses[j], winning_horses[j + 1] = winning_horses[j + 1], winning_horses[j]

    # Visualizing the top 3 winning horses with stars by getting from the race times
    for i, horse in enumerate(winning_horses[:3]):
        stars = '*' * (int(horse.get('race_time', 0)) // 10)

        # Determining the positions
        losses = f"{i + 1}st" if i == 0 else f"{i + 1}nd" if i == 1 else f"{i + 1}rd"

        # Displaying the visualizing of the winning horses
        print(f"{horse['id']}  {horse['name']:<20} {stars:<10} {horse.get('race_time', 0)}s  ({losses} Place)")

# Below function displays the main menu
def menu():
    global selected_horses, winning_horses, first_run, race_simulated  # Accessing the global variables

    if first_run:
        print("====================================================================")
        print("                   WELCOME JAMES, TO RAPID RUN")
        print("====================================================================")
        first_run = False  # The flag is set to 'False' after the first run

    print("                        HORSE DETAILS MENU")  # Print statement of the menu
    print("--------------------------------------------------------------------\n")
    print("1) TYPE AHD - ADDING HORSE DETAILS                               ")
    print("2) TYPE UHD - UPDATE HORSE DETAILS                            ")
    print("3) TYPE DHD - DELETING HORSE DETAILS                             ")
    print("4) TYPE VHD - VIEWING THE REGISTERED HORSES DETAILS TABLE        ")
    print("5) TYPE SHD - SAVE THE HORSE DETAILS TO THE TEXT FILE            ")
    print("6) TYPE SDD - SELECTING FOUR HORSES RANDOMLY FOR THE MAJOR ROUND ")
    print("7) TYPE WHD - DISPLAYING THE WINNING HORSE DETAILS               ")
    print("8) TYPE VWH - VISUALIZING THE TIME OF THE WINNING HORSES         ")
    print("9) TYPE ESC - EXIT THE PROGRAM                                    ")
    print("\n--------------------------------------------------------------------\n")

    # According to the user's choice, corresponding actions will be executed
    decision = input("Please enter your decision : ").upper()

    if decision == 'AHD':
        add_horse(horses)
        save_to_text_file(horses)
        menu()
    elif decision == 'UHD':
        update_horse(horses)
        save_to_text_file(horses)
        menu()
    elif decision == 'DHD':
        delete_horse(horses)
        save_to_text_file(horses)
        menu()
    elif decision == 'VHD':
        view_horses(horses)
        menu()
    elif decision == 'SHD':
        save_to_text_file(horses)
        race_simulated = True  # The flag is set, to indicate the race has been simulated
        print("\nHorse details saved to text file.")
        print("\n--------------------------------------------------------------------")
        menu()
    elif decision == 'SDD':
        if not race_simulated:
            print("\nPlease run SHD first to save the text file.")
        else:
            # Calls the function select_four_horses and checks whether it is successful
            selected_horses, grouped_horses, empty_groups = select_four_horses(horses)
            # Checks whether if the selection was successful before displaying selected horses
            if selected_horses:
                display_selected_horses(selected_horses)
            else:
                # To handle the case when there is an error in horse selection
                print("Can't select horses. Each group must have at least one horse.")
                if empty_groups:
                    if len(empty_groups) == 1:
                        print("\nGroup without horses :", empty_groups[0])
                    else:
                        print("\nGroups without horses :", ', '.join(empty_groups))
                print("\nPlease run AHD to add horse details.")
        print("\n--------------------------------------------------------------------")
        menu()
    elif decision == 'WHD':
        if not selected_horses:
            print("\nPlease run SDD to select horses first.")
            print("\n--------------------------------------------------------------------")
        else:
            winning_horses = simulate_race(selected_horses)  # The winning horses is saved globally
            print("\n--------------------------------------------------------------------")
        menu()
    elif decision == 'VWH':
        if not winning_horses:
            print("\nPlease run WHD to simulate the race first.")
            print("\n--------------------------------------------------------------------")
        else:
            visualize_winning_horses(winning_horses)  # The winning horses is passed to the visualization function
            print("\n--------------------------------------------------------------------")
        menu()
    elif decision == 'ESC':
        print("\n====================================================================")
        print("                        Exiting The Program")
        print("====================================================================")
    else:
        print("\nInvalid input. Please enter a valid option.")
        print("\n--------------------------------------------------------------------")
        menu()

# The program is started by calling the menu function
menu()