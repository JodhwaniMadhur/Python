from twilio.rest import Client

def tw(current_date_time,count):
    account_sid = 'AC7deb13150cc40f69cf77eaac2375625d'
    auth_token = '19b5d10dbce5dd88362494987e0eb646'
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="This is an automated scheduled message from Hourly File Duplicate Scanner carried out on date "+current_date_time+"and the number of duplicate files detected and deleted are "+str(count), from_='+18432024886', to='+919767065760')
    print(message.sid)