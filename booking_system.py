print("Welcome to YouTube Creator Award 2025!")
print("We are pleased to have you, would you like to buy a ticket? (Y/N)")
y_n_ticket = input()

# Ticket prices
adult_price = 67.99
child_price = 37.00

if y_n_ticket == "Y" or y_n_ticket == "y":
    print("Great, let's go through the process.")

    print("How many adults?")
    adult_num = float(input())

    print("How many children?")
    child_num = float(input())

    total = adult_price * adult_num + child_price * child_num
    print(f"Thank you, your ticket total is £{total}")

elif y_n_ticket == "N" or y_n_ticket == "n":
    print("Alright thank you.")
    total = 0   # no ticket so total starts at 0

else:
    exit()

# MERCH
black_youtube_shirt = 10.99 
white_youtube_shirt = 25.00 
green_youtube_shirt = 38.99
christmas_speciel_mystery = 45.99
google_logo_t_shirt = 56.67
google_collab_with_samsung_shirt = 67.60

print("Would you like to buy our new Merches today? (Y/N)")
merch_yes_no = input()

if merch_yes_no == "Y" or merch_yes_no == "y":

    print("A) Black YouTube shirt")
    print("B) White YouTube shirt")
    print("C) Green YouTube shirt")
    print("D) Christmas Special Mystery")
    print("E) Google Logo T-Shirt")
    print("F) Google x Samsung shirt")

    merch_ans = input()

    if merch_ans == "A" or merch_ans == "a":
        price = black_youtube_shirt
    elif merch_ans == "B" or merch_ans == "b":
        price = white_youtube_shirt
    elif merch_ans == "C" or merch_ans == "c":
        price = green_youtube_shirt
    elif merch_ans == "D" or merch_ans == "d":
        price = christmas_speciel_mystery
    elif merch_ans == "E" or merch_ans == "e":
        price = google_logo_t_shirt
    elif merch_ans == "F" or merch_ans == "f":
        price = google_collab_with_samsung_shirt
    else:
        print("Invalid option.")
        exit()

    print("How many of that item?")
    quantity = float(input())

    merch_total = price * quantity
    total = total + merch_total

    print(f"Merch total is £{merch_total}")

print(f"\nYour FINAL total is £{total}")
print("Thank you!")


