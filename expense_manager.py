def expenses():
    expense_list = []

    while True:
        print("\n1.Add expense")
        print("2.Exit")

        choice = input("Enter choice:")

        if choice == "1":
            try:
                amount = float(input("Enter the amount:"))
            except ValueError:
                print("Please enter valid number")
                continue

            category = input("Enter the category:")
            note = input("Enter the note:")

            expense = {"amount":amount,
                       "category":category,
                       "note":note
                      }
            expense_list.append(expense)
            
        elif choice == "2":
            break

        else:
            print("Invalid choice. Please enter 1 or 2")

    total = 0
    
    print("\nAll Expenses:")
    for exp in expense_list:
        print(f"₹{exp['amount']} | {exp['category']} | {exp['note']}")
        total += exp['amount']

    print(f"Number of expenses: {len(expense_list)}")
    print(f"Total amount spent:₹{total:.2f}")

expenses()
