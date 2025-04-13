from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Configure Gemini API
GOOGLE_API_KEY = "AIzaSyBvORqc_Oq8FFJUTcc692h-1eB95Qb-y24"  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_packing_list(destination, duration, season):
    prompt = f"""Generate a detailed packing list for a trip to {destination} during {season} for {duration} days.
    Include essential items, clothing, toiletries, electronics, and any special items needed for this destination.
    Format the response in a clear, organized list with categories."""
    
    response = model.generate_content(prompt)
    return response.text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if "packing list" in user_message.lower():
        # Extract destination, duration, and season from user message
        # This is a simple implementation - you might want to make it more robust
        destination = "your destination"  # Extract from user message
        duration = "7"  # Default duration
        season = "summer"  # Default season
        
        response = generate_packing_list(destination, duration, season)
    else:
        # For general questions
        response = model.generate_content(user_message).text
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True) 