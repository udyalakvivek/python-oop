# ==========================================
# PARENT CLASS: Core infrastructure for notifications
# ==========================================
class NotificationChannel:
    def __init__(self, channel_name):
        self.channel_name = channel_name  # Public: Channel ka naam (e.g., 'SMS')
        self._enabled = True             # Protected: Internal system control flag

# ==========================================
# CHILD CLASS: Single Inheritance implementation
# ==========================================
class SMSChannel(NotificationChannel):
    def __init__(self, channel_name, provider_api_key):
        super().__init__(channel_name)       # Parent class ke constructor ko call kiya
        self.__api_key = provider_api_key  # Private: Secure telecom credential API key

    def send_sms(self, phone_number, message):
        # Protected variable '_enabled' ko child class use kar sakti hai
        if self._enabled:
            return f"[SMS via {self.channel_name}] Sent to {phone_number}: {message}"
        return "Channel is temporarily disabled."


sms_service = SMSChannel("Twilio_Gateway", "secret_key_123")
print(sms_service.send_sms("+123456789", "Your OTP is 4821"))
# Output: [SMS via Twilio_Gateway] Sent to +123456789: Your OTP is 4821
