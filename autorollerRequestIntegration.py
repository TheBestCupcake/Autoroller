import requests

def sendToDiscord(url, message, channelID):
    payloadJSON = {
        "channelID": channelID,
        "message": message
    }
    
    response = requests.post(url, json=payloadJSON)
    
    if response.status_code == 200:
        print('Message sent successfully!')
    else:
        print('Failed to send message:', response.json())
    
