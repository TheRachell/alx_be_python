task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

match priority:
    case "high" | "medium" | "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
            print("Invalid input for time-bound. Please enter 'yes' or 'no'.")
    case _:
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
