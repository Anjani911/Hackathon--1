# detector.py
def is_phishing(url):
    # Placeholder logic - replace with your real model or rules
    if "free" in url or "login" in url or "verify" in url:
        return "Phishing link detected!"
    return "Safe link."
