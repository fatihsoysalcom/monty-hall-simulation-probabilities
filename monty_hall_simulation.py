import random

def simulate_monty_hall(num_trials, switch_strategy):
    """
    Simulates the Monty Hall problem for a given number of trials and strategy.

    Args:
        num_trials (int): The number of times to run the simulation.
        switch_strategy (bool): True if the player switches doors, False if they stick.

    Returns:
        int: The number of wins.
    """
    wins = 0
    for _ in range(num_trials):
        # 1. Place the car behind a random door (0, 1, or 2)
        car_door = random.randint(0, 2)
        
        # 2. Player makes an initial choice
        player_initial_choice = random.randint(0, 2)
        
        # 3. Monty opens a goat door
        # Monty must open a door that is not the player's initial choice
        # AND not the car door.
        
        # Find available doors for Monty to open
        available_doors_for_monty = [i for i in range(3) if i != player_initial_choice and i != car_door]
        
        # Monty opens one of the available goat doors. If player picked car, Monty has 2 choices.
        # If player picked goat, Monty has only 1 choice (the other goat door).
        monty_opened_door = random.choice(available_doors_for_monty)
        
        # 4. Player decides to stick or switch
        player_final_choice = player_initial_choice # Default: stick strategy
        if switch_strategy:
            # If switching, the player chooses the *other* unopened door.
            # This door is neither the initial choice nor the one Monty opened.
            for door in range(3):
                if door != player_initial_choice and door != monty_opened_door:
                    player_final_choice = door # The player switches to this door
                    break
            # This is the core logic illustrating the switching advantage:
            # The initial choice has a 1/3 chance of being correct. The other two doors
            # collectively have a 2/3 chance. When Monty reveals a goat from the other two,
            # the remaining unopened door (the switch option) consolidates that 2/3 probability.
            
        # 5. Check if the player won
        if player_final_choice == car_door:
            wins += 1
            
    return wins

if __name__ == "__main__":
    num_trials = 10000 # Number of simulations to run

    print(f"Running {num_trials} simulations of the Monty Hall problem...\n")

    # Simulate sticking strategy
    wins_stick = simulate_monty_hall(num_trials, False)
    win_percentage_stick = (wins_stick / num_trials) * 100
    print(f"Strategy: STICKING with initial choice")
    print(f"Wins: {wins_stick} out of {num_trials}")
    print(f"Win Percentage: {win_percentage_stick:.2f}%\n") # Expected ~33.33%

    # Simulate switching strategy
    wins_switch = simulate_monty_hall(num_trials, True)
    win_percentage_switch = (wins_switch / num_trials) * 100
    print(f"Strategy: SWITCHING to the other unopened door")
    print(f"Wins: {wins_switch} out of {num_trials}")
    print(f"Win Percentage: {win_percentage_switch:.2f}%\n") # Expected ~66.67%

    print("Conclusion: Switching doors significantly increases the probability of winning.")
