def calculate_daily_sales(sales):
    return sum(sales)

def filter_sales(sales, threshold=100):
    return [sale for sale in sales if sale >= threshold]

def apply_discount(sales, discount=0.1):
    return [round(sale * (1 - discount), 2) for sale in sales]

if __name__ == "__main__":
    sample_sales = [50, 100, 200, 75, 150]
    
    filtered = filter_sales(sample_sales, threshold=100)
    print("Filtered Sales:", filtered)
    print("Total Filtered Sales:", calculate_daily_sales(filtered))
    
    discounted = apply_discount(filtered, discount=0.2)
    print("Discounted Sales after Filtering:", discounted)
    print("Total Discounted Filtered Sales:", calculate_daily_sales(discounted))

