import json
import os




def load_history():
    try:
        with open("fizzbuzz_history.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_history():
    with open("fizzbuzz_history.json", "w") as f:
        json.dump(count_list, f)


count_list = load_history()
achievement_list = []

def achievements():
    if count_list.count('FizzBuzz') >= 10 and "10 FIZZBUZZ" not in achievement_list :
        achievement_list.append("10 FIZZBUZZ")
    if count_list.count('Buzz') >= 5 and "5 BUZZ" not in achievement_list:
        achievement_list.append("5 BUZZ")


while True:
    print("\n=== FizzBuzz Menu ===")
    print("1. Choose range (first & last)")
    print("2. Choose last number only")
    print("3. Exit")
    print("4. View statistics")
    print("5. Clear stats")
    print("6. Save data")
    print("7. Load data")
    user_input = input("Enter choice: ")

    def FizzBuzz(user_number2, divider1, divider2, user_number1=1):
        # divider 1 == Fizz and divider 2 == Buzz, both is Fizzbuzz
        for n in range(user_number1, user_number2):
            if n % divider1 == 0 and n % divider2 == 0:
                print("FizzBuzz")
                count_list.append("FizzBuzz")
            elif n % divider1 == 0:
                print("Fizz")
                count_list.append("Fizz")
            elif n % divider2 == 0:
                print("Buzz")
                count_list.append("Buzz")
            else:
                print(f"{n}")
                count_list.append("Number")

        achievements()

    #handles the input for the game
    if user_input == "1":
        user_input_number1 = int(input("input your first number: "))
        user_input_number2 = int(input("input your last number: "))
        user_input_divider1 = int(input("What should Fizz divide by: "))
        user_input_divider2 = int(input("What should Buzz divide by: "))
        FizzBuzz(user_input_number2, user_input_divider1, user_input_divider2, user_input_number1)

    elif user_input == "2":
        user_input_number = int(input("input your last number: "))
        user_input_divider1 = int(input("What should Fizz divide by: "))
        user_input_divider2 = int(input("What should Buzz divide by: "))
        FizzBuzz(user_input_number, user_input_divider1, user_input_divider2)
    elif user_input == "3":
        break

    # check your stats
    elif user_input == "4":

        total = int(count_list.count("Fizz")) + int(count_list.count("Buzz")) + int(count_list.count("FizzBuzz") + int(count_list.count("Number")))
        if total != 0:

            print("=== STATS ===")
            print(f"Total numbers: {total}")
            print(f"Total Achievements: {len(achievement_list)}")
            achievemnt_display = ", ".join(achievement_list)


            fizz_bar = '#' * (count_list.count('Fizz') // 2)
            number_bar = '#' * (count_list.count('Number') // 2)
            Buzz_bar = '#' * (count_list.count('Buzz') // 2)
            FizzBuzz_bar = '#' * (count_list.count('FizzBuzz') // 2)

            print(f"Fizz:  [{fizz_bar}] [{count_list.count('Fizz')}] {(count_list.count('Fizz') / total) * 100:.2f}%")
            print(f"Normal Numbers: [{number_bar}] [{count_list.count('Number')}] {(count_list.count('Number') / total) * 100:.2f}%")
            print(f"Buzz: [{Buzz_bar}] [{count_list.count('Buzz')}] {(count_list.count('Buzz') / total) * 100:.2f}%")
            print(f"FizzBuzz: [{FizzBuzz_bar}] [{count_list.count('FizzBuzz')}] {(count_list.count('FizzBuzz') / total) * 100:.2f}%")
            print(f"Achievements: {achievemnt_display}")

        else:
            print("No stats found")

    # clear your stats
    elif user_input == "5":
        count_list.clear()
        try:
            os.remove("fizzbuzz_history.json")
            print("Stats deleted!")
        except FileNotFoundError:
            print("No saved data found")


    elif user_input == "6":
        save_history()


    elif user_input == "7":
        load_history()
        print(f"Data loaded! {len(count_list)} entries found.")

    else:
        print("Invalid argument")



