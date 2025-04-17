from urllib.parse import urlparse

suspicious_keywords = ['free', 'login', 'verify', 'update', 'password', 'security']

def check_url(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.lower()
        path = parsed_url.path.lower()
        
        # Heuristic: check if too many keywords appear in domain + path
        combined = domain + path
        hits = [kw for kw in suspicious_keywords if kw in combined]
        
        if len(hits) >= 2:
            return "Phishing link detected!"
        else:
            return "Safe link."
    except Exception as e:
        return f"Error analyzing link: {str(e)}"