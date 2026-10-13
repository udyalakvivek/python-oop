# Base Class (Iske paas base attributes hain)
class NotificationChannel:
    def __init__(self, channel_name):
        self.channel_name = channel_name

# Intermediate Class (Inherits from NotificationChannel)
class SMSChannel(NotificationChannel):
    def __init__(self, channel_name, provider_api_key):
        super().__init__(channel_name)
        self.provider_api_key = provider_api_key

# Final Subclass: Multilevel Inheritance (Inherits from SMSChannel)
class PromotionalSMS(SMSChannel):
    def __init__(self, channel_name, provider_api_key, opt_out_link):
        # Apne immediate parent (SMSChannel) ke init ko trigger kiya
        super().__init__(channel_name, provider_api_key)
        self.opt_out_link = opt_out_link  # Extra property marketing ke liye

    def send_promo(self, phone_number, deal_text):
        # Dono super classes ke attributes yahan accessible hain
        full_msg = f"{deal_text} Click to stop: {self.opt_out_link}"
        return f"[PROMO SMS - {self.channel_name}] Sent to {phone_number}: {full_msg}"

# ---- Execution / Testing File 2 ----
promo_service = PromotionalSMS("BulkSMS_Net", "api_key_xyz", "unsub.me/99")
print(promo_service.send_promo("+91999999", "Get 50% Off Today!"))
# Output: [PROMO SMS - BulkSMS_Net] Sent to +91999999: Get 50% Off Today! Click to stop: unsub.me/99
