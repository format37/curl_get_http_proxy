from fastapi import FastAPI, HTTPException
import requests
import configparser
from pydantic import BaseModel

app = FastAPI()

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')
bot_token = config['telegram']['bot_token']
chat_id = config['telegram']['chat_id']
telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

class Message(BaseModel):
    message: str

@app.get("/send_message")
def send_message(message: str = 'No message provided'):
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(telegram_url, data=payload)
    
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail=f"Error: {response.text}")

    return {"detail": "Message sent successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
