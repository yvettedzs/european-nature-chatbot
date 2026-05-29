import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

system_prompt = (
    "You are an expert on European tourism with special knowledge of "
    "places in nature such as natural parks, lakes and viewpoints. "
    "You only recommend hidden gems that are not tourist hotspots. "
    "Your entire response must be written exclusively in the official "
    "language of the country you are recommending. "
    "Never use English in your response, not even partially. "
    "Keep your response under 7 words. "
    "Example for France: 'Gorges du Verdon, beauté sauvage et cristalline.' "
    "Example for Slovenia: 'Triglavski narodni park, nedotaknjena gorska narava.' "
    "Follow this exact pattern for every response."
    "Never break character or explain your responses under any circumstances."
)

messages = []

print("European Nature Bot — type 'quit' to exit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=50,
        temperature=0.0,
        system=system_prompt,
        messages=messages
    )

    reply = response.content[0].text
    print(f"Bot: {reply}\n")

    messages.append({"role": "assistant", "content": reply})
    
print("\n--- Message History ---")
for m in messages:
    print(f"{m['role'].upper()}: {m['content']}")
print("------------------------\n")