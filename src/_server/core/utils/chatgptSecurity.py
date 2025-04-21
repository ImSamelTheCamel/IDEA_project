import re

inappropriate_keywords = [
    # Illegal activities
    "phishing", "bomb", "illegal", "hack", "fraud", "scam", "identity theft", "malware", "ransomware",
    "virus", "trojan", "spyware", "crack", "ddos", "exploit", "hacker", "cyberattack", "pharming",
    "data breach", "brute force", "cracking", "keylogger", "backdoor", "fraudulent", "blackhat",

    # Violence and harm
    "violence", "kill", "murder", "assault", "terrorism", "bombing", "suicide", "self-harm", "injury",
    "stabbing", "shooting", "kidnapping", "torture", "rape", "harassment", "abuse", "domestic violence",
    "hate crime", "racism", "xenophobia", "homophobia", "misogyny", "sexism", "bullying", "discrimination",
    
    # Sensitive personal information
    "social security number", "credit card number", "bank account", "password", "login credentials", 
    "pin code", "security question", "address", "phone number", "email address", "passport", "driver's license",

    # Malicious activity
    "pharming", "cryptojacking", "carding", "skimming", "money laundering", "human trafficking", "drug trafficking",
    "weapon", "explosive", "biohazard", "chemical attack", "bio weapon",

    # Inappropriate requests or content
    "nude", "porn", "sexual", "explicit", "lewd", "gore", "gruesome", "snuff", "torture", "rape fantasy", "child pornography",
    
    # Harmful behaviors
    "addiction", "substance abuse", "overdose", "eating disorder", "bulimia", "anorexia", "self-harm", "cutting", "suicide pact"
]


def is_inappropriate_input(user_message):
    for keyword in inappropriate_keywords:
        if re.search(r'\b' + re.escape(keyword) + r'\b', user_message, re.IGNORECASE):
            return True
    return False

def is_inappropriate_output(response):
    for phrase in inappropriate_keywords:
        if re.search(r'\b' + re.escape(phrase) + r'\b', response, re.IGNORECASE):
            return True
    return False
