weather = input("Enter the weather condition (sunny, rainy, cold): ").lower()

if weather == "sunny":
    print("It's a great day! Wear sunglasses and sunscreen.")
elif weather == "rainy":
    print("Don't forget your umbrella!")
elif weather == "cold":
    print("Make sure to bundle up and wear a coat.")
else:
    print("Sorry, I didn't understand that. Please enter 'sunny', 'rainy', or 'cold'.")

