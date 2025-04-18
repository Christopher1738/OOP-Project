from pet import Pet

def main():
    print("""
   ___      _ _          _   _     
  / _ \___ | (_)_ __ ___| |_| |__  
 / /_)/ _ \| | | '__/ _ \ __| '_ \ 
/ ___/ (_) | | | | |  __/ |_| | | |
\/    \___/|_|_|_|  \___|\__|_| |_|
    """)
    print("Welcome to Pet Simulator!")
    
    name = input("\nName your pet: ").strip()
    species = input("Species (dog/cat/rabbit/bird): ").strip().lower()
    pet = Pet(name, species or "dog")
    
    while True:
        print("\nMAIN MENU")
        print("1. Feed")
        print("2. Sleep")
        print("3. Play")
        print("4. Train")
        print("5. View Tricks")
        print("6. Check Status")
        print("7. Quit")
        
        choice = input("Choose (1-7): ")
        
        if choice == "1":
            food = input(f"Food type ({pet.favorite_food} is favorite): ")
            pet.eat(food if food else None)
        elif choice == "2":
            pet.sleep()
        elif choice == "3":
            game = input("Game (fetch/chase/hide and seek): ").lower()
            pet.play(game if game in ["fetch", "chase", "hide and seek"] else "fetch")
        elif choice == "4":
            trick = input("Trick to teach: ")
            pet.train(trick)
        elif choice == "5":
            pet.show_tricks()
        elif choice == "6":
            pet.get_status()
        elif choice == "7":
            print(f"Goodbye! {pet.name} will miss you!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()