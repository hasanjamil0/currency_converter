import requests

# ANSI Color codes
G = "\033[92m"  # GREEN
Y = "\033[93m"  # YELLOW
B = "\033[1m"   # BOLD
RS = "\033[0m"  # RESET

def convert_currency(amount, from_curr, to_curr):
    # This is the free API URL (No API key needed for this simple project)
    url = f"https://api.exchangerate-api.com/v4/latest/{from_curr.upper()}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if to_curr.upper() in data["rates"]:
            rate = data["rates"][to_curr.upper()]
            converted_amount = amount * rate
            return converted_amount, rate
        else:
            return None, None
            
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None, None

print("\n" + B + "--- REAL-TIME CURRENCY CONVERTER ---" + RS)

while True:
    try:
        print("\n(Example: USD, EUR, GBP, BDT, etc.)")
        from_curr = input("Convert FROM (or 'exit'): ")
        
        if from_curr.lower() == 'exit':
            print("Goodbye!")
            break
            
        to_curr = input("Convert TO: ")
        amount = float(input("Amount to convert: "))
        
        result, rate = convert_currency(amount, from_curr, to_curr)
        
        if result is not None:
            print(f"\n{G}{amount} {from_curr.upper()} = {result:.2f} {to_curr.upper()}{RS}")
            print(f"{Y}Exchange rate: 1 {from_curr.upper()} = {rate:.4f} {to_curr.upper()}{RS}")
        else:
            print("Invalid currency code. Please try again.")
            
    except ValueError:
        print("Please enter a valid numeric amount.")
