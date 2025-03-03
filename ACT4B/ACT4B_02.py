import csv

def load_exchange_rates(file_path):
    exchange_rates = {}
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                try:
                    exchange_rates[row[0].strip().upper()] = float(row[2].strip())
                except ValueError:
                    continue
    except FileNotFoundError:
        print("Error: Currency file not found.")
        return {}
    return exchange_rates

def convert_currency(amount, currency_code, exchange_rates):
    return amount * exchange_rates[currency_code] if currency_code in exchange_rates else None

def main():
    file_path = "ACT4B/currency.csv"  
    exchange_rates = load_exchange_rates(file_path)
    
    if not exchange_rates:
        return
    
    try:
        usd_amount = float(input("How much dollar do you have? ").strip())
        currency_code = input("What currency you want to have? ").strip().upper()
        
        converted_amount = convert_currency(usd_amount, currency_code, exchange_rates)
        
        if converted_amount is not None:
            print(f"\nDollar: {usd_amount} USD")
            print(f"{currency_code}: {converted_amount:.6f}")
        else:
            print("Sorry, currency code not found.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for dollars.")

if __name__ == "__main__":
    main()