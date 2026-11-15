# MIKE GEE TECHNOLOGIES - BUSINESS BOT v2.0
# For LAMI Fashion + TERROX Shop - Accra, Ghana

print("="*50)
print("  MIKE GEE BUSINESS BOT v2.0 - ONLINE")
print("  LAMI Fashion | TERROX Shop | Accra")
print("  Type 'exit' or 'quit' to stop")
print("="*50)
print("Bot: Hello! Welcome to LAMI Fashion. Ask me about price, delivery, or products!")

while True:
    msg = input("\nCustomer: ").strip().lower()

    if msg in ["exit", "quit", "bye", "0"]:
        print("Bot: Thank you! Come again. WhatsApp us: 0544555016")
        break

    # GREETING
    elif any(w in msg for w in ["hello", "hi", "hey", "good morning", "good afternoon", "salam"]):
        print("Bot: Hello Boss! Welcome to LAMI Fashion. How can I help you today?")
        print("     You can ask: price, kaba, delivery, whatsapp")

    # PRICE - KABA & SLIT
    elif any(w in msg for w in ["how much", "price", "cost", "kaba", "slit", "cloth", "dress", "product"]):
        print("Bot: Here are our prices:")
        print("     👗 Kaba & Slit (Full) - GHS 250")
        print("     👗 Slit Only - GHS 120")
        print("     👗 Kaba Only - GHS 150")
        print("     📦 TERROX Package - GHS 300")
        print("     Type 'order' to order now!")

    # DELIVERY
    elif any(w in msg for w in ["delivery", "deliver", "ship", "location", "where", "accra"]):
        print("Bot: Delivery Info:")
        print("     📍 Accra - GHS 20 (Same day)")
        print("     📍 Outside Accra - GHS 35 (1-2 days)")
        print("     📍 Pickup FREE - Accra, Osu")
        print("     Type 'order' to order!")

    # ORDER
    elif any(w in msg for w in ["order", "buy", "want", "i need", "book"]):
        print("Bot: Great! To order, WhatsApp us now:")
        print("     📱 WhatsApp: https://wa.me/233544555016")
        print("     Tell us: Your Name + What you want + Your Size")
        print("     Example: 'Hi, I want Kaba & Slit, Size M, Accra'")

    # WHATSAPP / CONTACT
    elif any(w in msg for w in ["whatsapp", "number", "contact", "call", "phone"]):
        print("Bot: Contact us:")
        print("     📱 WhatsApp: 0544555016")
        print("     🔗 Link: https://wa.me/233544555016")

    # SIZE
    elif any(w in msg for w in ["size", "medium", "large", "small", "xl", "measurement"]):
        print("Bot: We have sizes S, M, L, XL, XXL.")
        print("     We also sew to your exact measurement - FREE!")
        print("     Send your measurement on WhatsApp.")

    # THANKS
    elif any(w in msg for w in ["thank", "thanks", "ok", "okay", "nice", "good"]):
        print("Bot: You are welcome! CEO Mike Gee says thank you for supporting LAMI! 🙏")
        print("     Type 'order' to buy now, or 'price' to see prices.")

    # FALLBACK - NOW E NO GO SAY "I DIDN'T GET THAT" AGAIN
    else:
        print("Bot: I hear you! I can help with:")
        print("     1. Type 'price' - to see Kaba prices")
        print("     2. Type 'delivery' - delivery cost")
        print("     3. Type 'order' - to order now")
        print("     4. Type 'whatsapp' - our number")
