from twilio.rest import Client

def send_sms(phone_number, message):
    account_sid = 'ACf0e79877ab0370da0849709efeeae91b'
    auth_token = '9d523990f70ea123b133d4d0efeac7ac'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_='+996999654566',
        to=phone_number
    )
    return message.sid
