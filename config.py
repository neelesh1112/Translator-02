import os

# Configuration for the application

# OpenAI API key (you should set this as an environment variable for security)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-3C0Bkv6mkqF90loRkvgK1JdAMBRE1z68LM93m1NHJrT3BlbkFJEmCr5Tm6sThrCnpcGo9E1mNMq8VpOYqK66ciLTduQA")

# Function to validate if API key is present
def check_config():
    if not OPENAI_API_KEY or OPENAI_API_KEY == "your-default-api-key":
        raise ValueError("Please set the OPENAI_API_KEY in your environment or config.py file")

# Call this function at the start of your application to ensure everything is configured
check_config()
