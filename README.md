

```markdown
# Farmers App

## Technologies Used
- **Flask**: A micro web framework for Python.
- **OpenWeather API**: For weather data retrieval.
- **Google Translator API**: For language translation capabilities.
- **JavaScript**: For client-side scripting.

## Project Description
Farmers App is designed to assist farmers by providing real-time market prices for crops, weather updates, and soil health recommendations. The app aims to empower farmers with essential information to make informed decisions for better productivity and profitability.

## API References
- **OpenWeather API**: [OpenWeather API Documentation](https://openweathermap.org/api)
  - To use this API, sign up and obtain your API key [here](https://home.openweathermap.org/users/sign_up).
  
- **Google Translator API**: [Google Cloud Translation API Documentation](https://cloud.google.com/translate/docs)
  - You can access the API by creating a project in the Google Cloud Console and enabling the Translation API. Obtain your API key from [here](https://cloud.google.com/docs/authentication/getting-started).

## Demo Video
[Watch the demo video of Farmers App on YouTube](https://youtu.be/MzJy50wTdws?si=gruaZEp6XVHb_6W9)

## Installation and Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/farmers-app.git
   cd farmers-app
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your API keys**:
   - Create a `.env` file in the root of the project and add your API keys:
     ```
     OPENWEATHER_API_KEY=your_openweather_api_key
     GOOGLE_TRANSLATOR_API_KEY=your_google_translator_api_key
     ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser and go to**: `http://127.0.0.1:5000`

## Deployment Link
You can access the live version of Farmers App here: [https://youtu.be/MzJy50wTdws?si=gruaZEp6XVHb_6W9]

## Future Scope
- Implement user authentication for personalized experiences.
- Integrate additional APIs for market trends and soil analysis.
- Expand the app to support more languages for broader accessibility.
- Add features for crop recommendations based on local climate and soil data.
- Enhancing Chatbots

