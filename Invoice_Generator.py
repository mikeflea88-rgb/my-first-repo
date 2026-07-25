from datetime import date

print("=== CEO INVOICE GENERATOR v1.0 ===")

customer = input("Customer Name: ")
item = input("Item/Service: ")
amount = input("Amount GHS: ")

today = date.today()

print("\n==============================")
print("         INVOICE")
print("      CEO KOFI SERVICES")
print("==============================")
print(f"Date: {today}")
print(f"To: {customer}")
print(f"Item: {item}")
print(f"Amount: GHS {amount}")
print("==============================")
print("Thank you for your business!")
print("WhatsApp: 05XXXXXXXX")
print("==============================")

save = input("\nSave this invoice? y/n: ")
if save == 'y':
    file = open(f"Invoice_{customer}.txt", "w")
    file.write(f"Invoice for {customer}\nItem: {item}\nAmount: GHS {amount}\nDate: {today}")
    file.close()
    print("Saved as Invoice_"+customer+".txt")
