# 🍕 PizzaBot - Kira Pizzeria Virtual Assistant

A friendly AI-powered chatbot for Kira Pizzeria that helps customers choose the perfect pizza and provides personalized recommendations.

## 🌟 Features

- **Pizza Recommendations**: Get personalized pizza suggestions based on your preferences
- **Dietary Considerations**: Accommodates various dietary needs and restrictions
- **Menu Guidance**: Helps with ingredients, sizes, and pricing information
- **Complementary Suggestions**: Recommends sides and drinks to complete your order
- **Focused Conversations**: Keeps discussions pizza-focused for the best customer experience
- **Retry Logic**: Built-in error handling with automatic retries for reliable service

## 🛠️ Technology Stack

- **Python 3.7+**
- **Google Gemini 2.0 Flash** - AI model for natural language processing
- **python-dotenv** - Environment variable management
- **google-genai** - Google's Generative AI SDK

## 📋 Prerequisites

- Python 3.7 or higher
- Google Cloud account with Gemini API access
- API key for Google Gemini

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/pizzabot.git
   cd pizzabot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

4. **Run the application**
   ```bash
   python pizzabot.py
   ```

## 📦 Dependencies

Create a `requirements.txt` file with:
```
google-genai
python-dotenv
```

## 💬 Usage

1. Start the application by running `python pizzabot.py`
2. Type your pizza-related questions or preferences
3. Get personalized recommendations from the virtual assistant
4. Type `exit` or `quit` to end the conversation


## 🎯 Key Functionality

### Conversation Management
- Maintains chat history for contextual responses
- Politely redirects off-topic conversations back to pizza

### Error Handling
- Automatic retry mechanism for API failures
- Graceful fallback messages when service is unavailable

### Customer Service Focus
- Enthusiastic and helpful responses
- Clear, concise communication
- Personalized recommendations

## 🔒 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google Gemini API key | Yes |

## 🤖 AI Behavior

The bot is programmed to:
- Act as a friendly pizzeria staff member
- Provide helpful pizza recommendations
- Suggest complementary items
- Maintain focus on pizza-related conversations
- Never break character or mention being an AI

---

**Made with ❤️ for Kira Pizzeria** 🍕
