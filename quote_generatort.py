import random

def get_random_quote():
    quotes = [
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Do one thing every day that scares you. – Eleanor Roosevelt",
        "The future belongs to those who prepare for it today. – Malcolm X",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill"
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print("\n🌟 Your Inspirational Quote of the Day 🌟\n")
    print(get_random_quote())
