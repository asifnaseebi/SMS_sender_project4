from twilio.rest import Client

SID = "AC82f3030d02646110c3c0ef5b330a86c6"
AUTH_TOKEN = "290623e43dbb0a021426907ca18b43ec"

Client = Client(SID, AUTH_TOKEN)

message = input("Type the message you want to send: ")
Client.messages.create(body=message,
                       from_='+13203178435',
                       to='+923495329829')
