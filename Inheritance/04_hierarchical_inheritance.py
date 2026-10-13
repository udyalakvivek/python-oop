# Base Parent Class (Common foundation for all channels)
class NotificationChannel:
    def __init__(self, channel_name):
        self.channel_name = channel_name

# Child Branch A: Specific to SMS operations
class SMSChannel(NotificationChannel):
    def send_sms(self, phone, message):
        return f"[SMS Engine: {self.channel_name}] Dispatching to {phone}: {message}"

# Child Branch B: Hierarchical Sibling (Same parent, completely different logic)
class EmailChannel(NotificationChannel):
    def __init__(self, channel_name, smtp_server):
        super().__init__(channel_name)  # Base constructor setup
        self.smtp_server = smtp_server  # Unique attribute for email routing

    def send_email(self, email_address, message):
        return f"[Email Engine: {self.smtp_server}] Dispatching to {email_address}: {message}"

# ---- Execution / Testing File 3 ----
sms_engine = SMSChannel("Nexmo_SMS")
email_engine = EmailChannel("SendGrid_Mail", "smtp.sendgrid.net")

print(sms_engine.send_sms("+11223344", "Hello via text"))
# Output: [SMS Engine: Nexmo_SMS] Dispatching to +11223344: Hello via text

print(email_engine.send_email("user@test.com", "Hello via mail"))
# Output: [Email Engine: smtp.sendgrid.net] Dispatching to user@test.com: Hello via mail
