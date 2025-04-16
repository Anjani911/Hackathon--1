# detector.py
def check_url(url):
    if "free" in url or "login" in url or "verify" in url:
        return "Phishing link detected!"
    return "Safe link."

