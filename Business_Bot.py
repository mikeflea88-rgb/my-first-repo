print("=== CEO BUSINESS BOT v1.0 ===")
print("Bot is online. Type 'quit' to stop.\n")

def reply(message):
    message = message.lower() # make it not case sensitive
    
    if "price" in message or "cost" in message:
        return "Our products start from $50. DM us for the full catalog 💼"
    elif "hello" in message or "hi" in message:
        return "Hello! Welcome to CEO Store. How can I help you today? 😊"
    elif "delivery" in message or "shipping" in message:
        return "We deliver nationwide in Ghana within 2-3 days. Delivery fee: $5"
    elif "thank" in message:
        return "You're welcome! Come again soon 🙏"
    else:
        return "Sorry, I didn't get that. You can ask about: price, delivery, or products."

# Main Loop
while True:
    user_input = input("Customer: ")
    if user_input.lower() == "quit":
        print("Bot: Closing shop. Goodbye!")
        break
    
    bot_reply = reply(user_input)
    print(f"Bot: {bot_reply}\n")
