print("Welcome to the PPP Converter")
Dollars = int(input("Enter Dollars: \n$ "))
PPP = Dollars * 22.42
New_PPP = round(PPP, 2)
print(f"The Purchasing Power Parity in INR would be: {New_PPP}")
input("Press Enter to exit...")
