# chatbot.py
from data import PRODUCT_CATALOG

def chatbot_response(user_input):
    # Convert the user input to lowercase for easier matching
    user_input = user_input.lower()

    # If the user is asking for the price of a product
    if "price" in user_input:
        # Check for specific products
        for product in PRODUCT_CATALOG:
            if product.lower() in user_input:
                price = PRODUCT_CATALOG[product]["price"]
                stock = PRODUCT_CATALOG[product]["stock"]
                return f"Sure! 1 {product} costs ${price} each. Your total is ${price}. Remaining stock: {stock - 1}."

    # If the user is trying to buy a product
    elif "buy" in user_input or "order" in user_input:
        for product in PRODUCT_CATALOG:
            if product.lower() in user_input:
                quantity = int([word for word in user_input.split() if word.isdigit()][0])
                price = PRODUCT_CATALOG[product]["price"]
                stock = PRODUCT_CATALOG[product]["stock"]
                if quantity <= stock:
                    total_price = quantity * price
                    return f"You have successfully ordered {quantity} {product}. Your total is ${total_price}. Remaining stock: {stock - quantity}."
                else:
                    return f"Sorry, we only have {stock} {product} in stock."

    # Default response if the chatbot doesn't understand
    return "Sorry, I didn't understand that. Can you ask about a product or place an order?"
