print("=== CEO AI ASSISTANT v1.0 ===")
print("I am your personal AI. Type 'exit' to quit.\n")

memory = {} # This is where the AI remembers things

def ai_brain(user_input):
    user_input = user_input.lower()
    
    # Memory
    if "my name is" in user_input:
        name = user_input.split("my name is")[1].strip()
        memory['name'] = name
        return f"Nice to meet you, {name}! I will remember that."
    
    if "what is my name" in user_input:
        if 'name' in memory:
            return f"Your name is {memory['name']} CEO!"
        else:
            return "I don't know your name yet. Tell me 'my name is...' "
    
    # Knowledge Base
    if "hello" in user_input or "hi" in user_input:
        return "Hello CEO! How can I help you build wealth today?"
    elif "business idea" in user_input:
        return "Here are 3 ideas: 1. Phone accessories 2. Food delivery 3. Social media management for shops"
    elif "motivation" in user_input:
        return "Keep building CEO. In 1 year you will thank yourself for starting today."
    elif "how to make money" in user_input:
        return "Skill + Problem + Audience = Money. You are learning the 'Skill' part right now."
    
    else:
        return "I'm still learning. Ask me about: business ideas, motivation, or your name."

# Main Loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("AI: Goodbye CEO. Keep building!")
        break
    
    response = ai_brain(user_input)
    print(f"AI: {response}\n")
