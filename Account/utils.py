import random

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_sms(phone, code):
    print(f"[DEBUG] Sending OTP {code} to phone {phone}")
    # برای تولید واقعی می‌تونی به سرویس‌هایی مثل کاوه‌نگار یا Twilio متصل شی
