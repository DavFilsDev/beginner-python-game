# Introduction
name = input("Hey, what's your name? ")
print(f"\nHello {name}, welcome to my adventure game!")
print("You'll make choices that will determine your fate...\n")

# Ask if player wants to play
should_play = input("Do you want to play? (yes/no) ").lower()

if should_play in ["yes", "y", "oui", "o"]:  # Keeping some French alternatives for compatibility
    print("\nGreat, let's begin the adventure!")
    
    # First choice: direction
    direction = input("\nYou're at a crossroads. Do you want to go left or right? (left/right) ").lower()
    
    if direction == "left":
        # Left scenario
        print("\nYou chose to go left...")
        print("You arrive at a dark cave.")
        
        cave_choice = input("Do you want to enter the cave or continue on the path? (enter/continue) ").lower()
        
        if cave_choice == "enter":
            print("\nYou enter the cave and find a treasure chest!")
            print("But beware, there's a riddle to solve to open it.")
            
            riddle = input("\nWhat has cities but no houses, forests but no trees, rivers but no water? ")
            if riddle.lower() == "a map":
                print("\nCongratulations! You solved the riddle and won the treasure!")
                print("🎉 You won the game! 🎉")
            else:
                print("\nWrong answer! The chest disappears as if by magic...")
                print("Game over. Try again!")
        else:
            print("\nYou continue on your path but get lost in the forest.")
            print("After hours of walking, you finally find the exit. This ends your adventure.")
    
    elif direction == "right":
        # Right scenario
        print("\nYou chose to go right...")
        print("You arrive at a river with an old wooden bridge.")
        
        bridge_choice = input("Do you want to cross the bridge or swim? (cross/swim) ").lower()
        
        if bridge_choice == "swim":
            print("\nYou decide to swim...")
            print("Unfortunately, the water is freezing and the current too strong.")
            print("You're swept away by the waves. Game over.")
        else:
            print("\nYou carefully cross the creaky bridge.")
            print("On the other side, you meet a mysterious merchant.")
            
            merchant = input("He offers to sell you a potion for 10 gold coins. Do you accept? (yes/no) ").lower()
            
            if merchant in ["yes", "y", "oui", "o"]:
                print("\nThe potion gives you superhuman strength!")
                print("You continue your path and easily defeat the monster guarding the treasure.")
                print("💎 Congratulations, you won the game! 💎")
            else:
                print("\nYou politely refuse and continue your journey.")
                print("Further ahead, you find a magic sword on the ground.")
                print("With this weapon, you defeat the treasure guardian and win the game!")
                print("⚔️ Well done! ⚔️")
    
    else:
        print("\nYou hesitate for too long...")
        print("A bear attacks you from behind. Game over.")

else:
    print("\nToo bad, maybe next time...")
    print("Goodbye!")

# Ending message
print("\nThanks for playing, see you next time for new adventures!")