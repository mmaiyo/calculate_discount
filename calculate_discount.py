def calculate_discount():
    # Prompt the user for input
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    if discount_percent >= 20:
        discounted_price = original_price - (original_price * discount_percent / 100)
        return discounted_price, original_price
    else:
        return original_price, original_price

# Call the function and print the result
final_price, original_price = calculate_discount()
if final_price != original_price:
    print("Final price after applying the discount:", final_price)
else:
    print("No discount applied. Original price:", final_price)
