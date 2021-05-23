from twilio.rest import Client

def tw(current_date_time,count):
    account_sid = 'Your_Twilio_SID'
    auth_token = 'Your_Twilio_Token'
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="This is an automated scheduled message from Hourly File Duplicate Scanner carried out on date "+current_date_time+"and the number of duplicate files detected and deleted are "+str(count), from_='Your_Twilio_Phone Number', to='Senders_Phone_Number')
    print(message.sid)