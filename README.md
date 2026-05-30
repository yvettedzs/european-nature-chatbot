# 🌿 European Nature Tourism Chatbot

A CLI chatbot that recommends hidden natural gems across Europe,
responding in the local language of each country.

## Built With
- Python
- Anthropic Claude API (claude-haiku-4-5)
- python-dotenv

## Features
- Conversational memory across multiple turns
- Responds in the official language of the recommended country
- Avoids tourist hotspots — recommends genuine hidden gems
- Secure API key management via .env

## How to Run
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `.\venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Add your Anthropic API key to a `.env` file:
   `ANTHROPIC_API_KEY=your-key-here`
6. Run: `python chatbot.py`

## Example Output
You: Where should I go in Slovenia?
Bot: Triglavski narodni park, nedotaknjena gorska narava.

You: How about France?
Bot: Gorges du Tarn, joyau caché du sud-ouest.