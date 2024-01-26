from flask import Flask, request
import requests
import configparser

app = Flask(__name__)

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')
bot_token = config['telegram']['bot_token']
chat_id = config['telegram']['chat_id']
telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

@app.route('/send_message', methods=['GET'])
def send_message():
    message = request.args.get('message', 'No message provided')
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(telegram_url, data=payload)
    return response.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
