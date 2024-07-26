Bill = float(input("what was the total bill? $"))
Tips = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
People = int(input("How many people to split the bill?"))

Percent = Tips / 100
Pay_Tips = Bill * Percent
Total = Bill + Pay_Tips
Bill_per_person = Total / People

Result = "{:.2f}".format(Bill_per_person)

print(f"Each person should pay: ${Result}")