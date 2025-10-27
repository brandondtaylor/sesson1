#!/usr/bin/env python3
"""
ENCHANTED FOREST QUEST
A Text Adventure Game for Learning Python Fundamentals

This game demonstrates:
- Variables (player stats, inventory)
- If/else statements (decision branching)
- Loops (main game loop)
- Input/output (player interaction)
"""

# ============================================================================
# GAME SETUP - Initialize all variables at the start
# ============================================================================

# Player stats - these variables track the player's condition
health = 100
max_health = 100

# Inventory - list to store items the player collects
inventory = []

# Game state flags
game_running = True
has_magic_sword = False
has_healing_potion = False
has_ancient_key = False
forest_guardian_friend = False

# ============================================================================
# INTRODUCTION
# ============================================================================

print("=" * 60)
print("    ENCHANTED FOREST QUEST")
print("=" * 60)
print()
print("You awaken in a mystical forest shrouded in mist.")
print("Ancient trees tower above you, their branches whispering secrets.")
print("A narrow path winds ahead, and you sense magic in the air...")
print()
print(f"Your Health: {health}/{max_health}")
print()
input("Press Enter to begin your adventure...")
print()

# ============================================================================
# MAIN GAME LOOP - The game continues while game_running is True
# ============================================================================

while game_running:

    # ========================================================================
    # FIRST DECISION POINT - The Forest Entrance
    # ========================================================================

    print("-" * 60)
    print("THE FOREST ENTRANCE")
    print("-" * 60)
    print("You stand at a fork in the path.")
    print("To the LEFT, you hear the sound of rushing water.")
    print("To the RIGHT, you see strange glowing mushrooms.")
    print("STRAIGHT AHEAD, an old wooden sign points to 'Ancient Ruins'")
    print()
    print(f"Your Health: {health}/{max_health}")
    print(f"Your Inventory: {inventory if inventory else 'Empty'}")
    print()
    print("What do you do?")
    print("  1. Go LEFT toward the water")
    print("  2. Go RIGHT toward the glowing mushrooms")
    print("  3. Go STRAIGHT to the Ancient Ruins")
    print()

    # Get player choice and validate input
    choice1 = input("Enter your choice (1, 2, or 3): ").strip()
    print()

    # ========================================================================
    # BRANCHING PATH 1 - The Waterfall (LEFT)
    # ========================================================================

    if choice1 == "1":
        print("You follow the sound of water and discover a beautiful waterfall.")
        print("Behind the cascading water, you spot a hidden cave entrance!")
        print()
        print("What do you do?")
        print("  1. Enter the cave behind the waterfall")
        print("  2. Drink from the crystal-clear pool")
        print("  3. Return to the fork")
        print()

        choice2 = input("Enter your choice (1, 2, or 3): ").strip()
        print()

        if choice2 == "1":
            print("You step through the waterfall into the secret cave.")
            print("Inside, you find a MAGIC SWORD embedded in a stone!")
            print("With great effort, you pull it free!")
            print()
            inventory.append("Magic Sword")
            has_magic_sword = True
            print(f"*** Magic Sword added to inventory! ***")
            print()

        elif choice2 == "2":
            print("You drink from the magical pool.")
            print("The water sparkles as it touches your lips!")
            health = min(max_health, health + 30)
            print(f"*** You feel refreshed! Health restored to {health}/{max_health} ***")
            print()

        else:
            print("You decide to return to the fork in the path.")
            print()

    # ========================================================================
    # BRANCHING PATH 2 - The Mushroom Grove (RIGHT)
    # ========================================================================

    elif choice1 == "2":
        print("You approach the glowing mushrooms carefully.")
        print("They pulse with an otherworldly light.")
        print("A tiny FOREST SPRITE appears, hovering above the mushrooms!")
        print()
        print("The sprite says: 'Answer my riddle, and I shall grant you a gift!'")
        print()
        print("RIDDLE: 'I have no voice, but I can tell you stories.")
        print("         I have no hands, but I turn pages.")
        print("         What am I?'")
        print()
        print("  1. A book")
        print("  2. The wind")
        print("  3. A ghost")
        print()

        choice2 = input("Enter your choice (1, 2, or 3): ").strip()
        print()

        if choice2 == "1":
            print("CORRECT! The sprite claps with joy!")
            print("The sprite gives you a HEALING POTION!")
            print()
            inventory.append("Healing Potion")
            has_healing_potion = True
            print(f"*** Healing Potion added to inventory! ***")
            print()

        else:
            print("INCORRECT! The sprite frowns sadly.")
            print("The mushrooms release a cloud of spores!")
            health -= 20
            print(f"*** You take 20 damage! Health: {health}/{max_health} ***")
            print()

            # Check if player health drops too low
            if health <= 0:
                print("=" * 60)
                print("GAME OVER - The spores were too toxic!")
                print("=" * 60)
                print("You collapse in the mushroom grove, defeated by the forest's magic.")
                print()
                print("THE END")
                game_running = False
                break

    # ========================================================================
    # BRANCHING PATH 3 - The Ancient Ruins (STRAIGHT)
    # ========================================================================

    elif choice1 == "3":
        print("You follow the old wooden sign to the Ancient Ruins.")
        print("Crumbling stone pillars rise from the earth, covered in vines.")
        print("In the center, you see a locked stone door with mysterious symbols.")
        print()
        print("What do you do?")
        print("  1. Search the ruins for clues")
        print("  2. Try to force the door open")
        print("  3. Return to the fork")
        print()

        choice2 = input("Enter your choice (1, 2, or 3): ").strip()
        print()

        if choice2 == "1":
            print("You carefully search through the ruins.")
            print("Hidden beneath a collapsed pillar, you find an ANCIENT KEY!")
            print()
            inventory.append("Ancient Key")
            has_ancient_key = True
            print(f"*** Ancient Key added to inventory! ***")
            print()

        elif choice2 == "2":
            print("You push against the heavy stone door with all your might!")
            print("It doesn't budge, and you hurt yourself in the process.")
            health -= 15
            print(f"*** You take 15 damage! Health: {health}/{max_health} ***")
            print()

        else:
            print("You decide to return to the fork in the path.")
            print()

    else:
        print("Invalid choice. Please try again.")
        print()
        continue

    # ========================================================================
    # SECOND DECISION POINT - Deeper Into the Forest
    # ========================================================================

    print("-" * 60)
    print("DEEPER INTO THE ENCHANTED FOREST")
    print("-" * 60)
    print("After exploring, you venture deeper into the forest.")
    print("The trees grow thicker, and the air grows colder.")
    print("Suddenly, a massive FOREST GUARDIAN appears!")
    print()
    print("The Guardian, a creature of bark and leaves, blocks your path.")
    print()
    print(f"Your Health: {health}/{max_health}")
    print(f"Your Inventory: {inventory if inventory else 'Empty'}")
    print()
    print("What do you do?")
    print("  1. Attack the Guardian")
    print("  2. Try to befriend the Guardian")
    print("  3. Run away")
    print()

    choice3 = input("Enter your choice (1, 2, or 3): ").strip()
    print()

    # ========================================================================
    # COMBAT PATH - Attack the Guardian
    # ========================================================================

    if choice3 == "1":
        if has_magic_sword:
            print("You draw the MAGIC SWORD!")
            print("The blade glows with ancient power!")
            print("The Guardian recognizes the legendary weapon and bows respectfully.")
            print("'You are worthy,' it says. 'Pass, brave adventurer.'")
            forest_guardian_friend = True
            print()

        else:
            print("You attempt to fight the Guardian with your bare hands!")
            print("The Guardian is too powerful!")
            health -= 40
            print(f"*** The Guardian strikes you! You take 40 damage! ***")
            print(f"*** Health: {health}/{max_health} ***")
            print()

            if health <= 0:
                print("=" * 60)
                print("GAME OVER - Defeated by the Forest Guardian!")
                print("=" * 60)
                print("You fought bravely, but the Guardian was too strong.")
                print("The forest reclaims your body as you fall...")
                print()
                print("THE END")
                game_running = False
                break

            print("Badly wounded, you flee deeper into the forest!")
            print()

    # ========================================================================
    # FRIENDSHIP PATH - Befriend the Guardian
    # ========================================================================

    elif choice3 == "2":
        print("You raise your hands peacefully and speak to the Guardian:")
        print("'I mean no harm. I seek only to pass through your forest.'")
        print()
        print("The Guardian studies you carefully...")

        if len(inventory) >= 2:
            print("The Guardian sees your collection of magical items.")
            print("'You have been blessed by the forest,' it says warmly.")
            print("'You may pass, friend of nature.'")
            forest_guardian_friend = True
            print()

        else:
            print("The Guardian is skeptical of your intentions.")
            print("'You have not proven yourself to the forest.'")
            print("The Guardian lets you pass, but remains wary.")
            print()

    # ========================================================================
    # FLEE PATH - Run Away
    # ========================================================================

    elif choice3 == "3":
        print("You turn and run as fast as you can!")
        print("The Guardian doesn't pursue, but you trip and fall in your haste.")
        health -= 10
        print(f"*** You take 10 damage! Health: {health}/{max_health} ***")
        print()

        if has_healing_potion:
            print("You remember the HEALING POTION in your inventory!")
            print("Do you want to use it?")
            print("  1. Yes, drink the potion")
            print("  2. No, save it for later")
            print()

            potion_choice = input("Enter your choice (1 or 2): ").strip()
            print()

            if potion_choice == "1":
                health = min(max_health, health + 50)
                inventory.remove("Healing Potion")
                has_healing_potion = False
                print("You drink the HEALING POTION!")
                print(f"*** Health restored to {health}/{max_health}! ***")
                print()

    else:
        print("Invalid choice. The Guardian watches you with confusion.")
        print()

    # ========================================================================
    # FINAL DECISION POINT - The Heart of the Forest
    # ========================================================================

    print("-" * 60)
    print("THE HEART OF THE ENCHANTED FOREST")
    print("-" * 60)
    print("You finally reach the heart of the forest.")
    print("Before you stands an enormous ancient tree, glowing with magical energy.")
    print("A locked door is carved into its trunk.")
    print()
    print(f"Your Health: {health}/{max_health}")
    print(f"Your Inventory: {inventory if inventory else 'Empty'}")
    print()

    # ========================================================================
    # ENDING CONDITIONS - Different outcomes based on player's journey
    # ========================================================================

    # BEST ENDING - Player has the Ancient Key
    if has_ancient_key:
        print("You pull out the ANCIENT KEY you found in the ruins!")
        print("It fits perfectly into the lock on the tree door!")
        print()
        print("The door swings open, revealing a chamber filled with golden light.")
        print("Inside, you find the legendary TREASURE OF THE FOREST!")
        print()
        print("=" * 60)
        print("VICTORY - THE PERFECT ENDING!")
        print("=" * 60)
        print("You have discovered the forest's greatest secret!")
        print("The enchanted forest accepts you as its champion!")
        print()
        if forest_guardian_friend:
            print("The Forest Guardian appears and congratulates you:")
            print("'You have proven yourself wise and brave!'")
            print()
        print("You emerge from the forest forever changed, carrying")
        print("the treasure and the forest's blessing.")
        print()
        print("CONGRATULATIONS! You achieved the BEST ENDING!")
        print("=" * 60)
        game_running = False
        break

    # GOOD ENDING - Player befriended the Guardian or has magic items
    elif forest_guardian_friend or len(inventory) >= 2:
        print("Although you don't have the key to open the door,")
        print("the ancient tree recognizes your pure heart and courage.")
        print()
        print("The tree speaks to you in a voice like rustling leaves:")
        print("'You have shown respect to the forest and its guardians.'")
        print()
        print("The tree grants you a magical gift - a seed of wisdom!")
        print()
        print("=" * 60)
        print("VICTORY - THE GOOD ENDING!")
        print("=" * 60)
        print("You return home with the magical seed.")
        print("When planted, it will grow into a tree that grants")
        print("protection and prosperity to your village!")
        print()
        print("You have earned the forest's friendship!")
        print("CONGRATULATIONS!")
        print("=" * 60)
        game_running = False
        break

    # ALTERNATE ENDING - Player survived but didn't excel
    elif health > 30:
        print("You stand before the great tree, but lack the key to enter.")
        print("You've survived the forest's challenges, but the greatest")
        print("secrets remain hidden from you.")
        print()
        print("=" * 60)
        print("ENDING - THE SURVIVOR'S PATH")
        print("=" * 60)
        print("You make your way out of the enchanted forest alive.")
        print("Though you didn't find the treasure, you gained valuable")
        print("experience and lived to tell the tale!")
        print()
        print("Perhaps next time you'll explore more thoroughly...")
        print("THE END")
        print("=" * 60)
        game_running = False
        break

    # BAD ENDING - Player's health is too low
    else:
        print("You collapse before the ancient tree, too weak to continue.")
        print()
        print("=" * 60)
        print("GAME OVER - THE WEAK ENDING")
        print("=" * 60)
        print("Your injuries were too severe.")
        print("The forest gently carries you back to the entrance,")
        print("where you awaken hours later, defeated but alive.")
        print()
        print("Better luck next time, adventurer!")
        print("THE END")
        print("=" * 60)
        game_running = False
        break

# ============================================================================
# END OF GAME
# ============================================================================

print()
print("Thank you for playing ENCHANTED FOREST QUEST!")
print("This game demonstrated:")
print("  - Variables (health, inventory, game flags)")
print("  - If/else statements (decision branching)")
print("  - Loops (main game loop)")
print("  - Input/output (player choices)")
print()
print("Try playing again and making different choices!")
