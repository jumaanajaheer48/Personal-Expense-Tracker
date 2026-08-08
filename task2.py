import os
DATA_FILE = "expenses.txt"
def load_total_expense():
   
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                content = file.read().strip()
                return float(content) if content else 0.0
        except ValueError:
            return 0.0
    return 0.0

def save_total_expense(amount):
    with open(DATA_FILE, "w") as file:
        file.write(str(amount))

def main():
    
    total_expense = load_total_expense()

    print("---  EXPENSE TRACKER SYSTEM  ---")
    if total_expense > 0:
        print(f"Previous Total Found: ${total_expense:.2f}")
    print("Enter your expense amounts below.")
    print("Type 'quit' or 'exit' when you are done.\n")

    while True:
        user_input = input("Enter expense amount (or 'quit' to exit): ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print("\n[+] Calculation Ended.")
            break
        
        try:
            expense = float(user_input)
            
            if expense < 0:
                print("Negative amounts are not allowed. Please enter a valid positive expense.\n")
                continue
                
           
            total_expense += expense
            
            
            save_total_expense(total_expense)
            
            print(f"Added: ${expense:.2f} | Current Total: ${total_expense:.2f}\n")
            
        except ValueError:
            print("Invalid Input! Please enter numbers only (e.g., 100, 50.50).\n")

   
    print("-" * 40)
    print(f"FINAL TOTAL SPENT: ${total_expense:.2f}")
    print("-" * 40)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n Program stopped by user.")