from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "***Your Account SID***"
# Your Auth Token from twilio.com/console
auth_token  = "***Your Account Token***"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="***Receiver Number***", 
   from_='***Bought Number From Twilio***',
# Message to Send    
    body="Hello from Python!")

print(message.sid)
