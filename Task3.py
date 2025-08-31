# ATM Machine Simulation

# Fixed PIN
PIN = "1234"

# Starting balance
balance = 1000.0   # you can set any starting balance

# Ask for PIN
entered_pin = input("Enter your ATM PIN: ")

if entered_pin == PIN:
    print("✅ PIN accepted. Welcome to the ATM!\n")
    
    while True:
        # Show menu
        print("===== 🏧 ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print(f"💰 Your current balance is: {balance:.2f}\n")
        
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"✅ {amount:.2f} deposited successfully!")
            print(f"💰 New balance: {balance:.2f}\n")
        
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"✅ {amount:.2f} withdrawn successfully!")
                print(f"💰 New balance: {balance:.2f}\n")
            else:
                print("❌ Insufficient balance!\n")
        
        elif choice == "4":
            print("👋 Thank you for using the ATM. Goodbye!")
            break
        
        else:
            print("⚠️ Invalid choice. Please try again.\n")

else:
    print("❌ Incorrect PIN. Access denied.")
