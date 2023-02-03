from twilio.rest import Client
import credentials

client = Client(credentials.account_sid, credentials.auth_token)

call = client.messages.create(
    #to = credentials.to,
    to = "+447795208585",
    from_ = credentials.from_,
    body = "Test message"
)
