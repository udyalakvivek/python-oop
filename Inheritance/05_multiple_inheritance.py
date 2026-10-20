# Independent Parent Class 1: Core domain function handling emails
class EmailChannel:
    def __init__(self, channel_name):
        self.channel_name = channel_name

    def send_email(self, recipient, message):
        return f"Email sent via {self.channel_name} to {recipient}: {message}"

# Independent Parent Class 2: Mixin class designed solely for data auditing
class AuditLogger:
    def __init__(self):
        self.logs = []  # Log list initialization

    def log_event(self, entry):
        self.logs.append(entry)
        print(f"[AUDIT LOG REGISTERED]: {entry}")

# Child Class: Multiple Inheritance (Inheriting from BOTH distinct classes)
class SecureCorporateEmail(EmailChannel, AuditLogger):
    def __init__(self, channel_name):
        # Dono independent parents ke constructors ko explicitly initialize kiya
        EmailChannel.__init__(self, channel_name)
        AuditLogger.__init__(self)

    def dispatch_secure_payload(self, company_email, report_data):
        # Class 1 ka method call kiya email bhejne ke liye
        status = self.send_email(company_email, f"Encrypted Data: {report_data}")
        # Class 2 ka method call kiya transparency audit log ke liye
        self.log_event(f"Confidential file sent to {company_email}")
        return status

# ---- Execution / Testing File 4 ----
secure_corp = SecureCorporateEmail("Internal_Exchange_Server")
print(secure_corp.dispatch_secure_payload("ceo@company.com", "Q4_Profit_Report.pdf"))
# Console Prints: [AUDIT LOG REGISTERED]: Confidential file sent to ceo@company.com
# Returns: Email sent via Internal_Exchange_Server to ceo@company.com: Encrypted Data: Q4_Profit_Report.pdf


# Car example :

class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

class Battery:
    def battery_info(self):
        return "This is Battery info!"

class Engine:
    def engine_info(self):
        return "This is engine info!"



class ElectricCarTwo(Car,Battery,Engine):
    pass

obj1 = ElectricCarTwo("Tata","Punch")
print(obj1.battery_info())
print(obj1.engine_info())
