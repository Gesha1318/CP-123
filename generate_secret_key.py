#!/usr/bin/env python3
"""
Generate a secure Django secret key.
"""

import secrets
import string

def generate_secret_key(length=50):
    """Generate a secure secret key for Django."""
    # Use a mix of letters, digits, and special characters
    alphabet = string.ascii_letters + string.digits + string.punctuation
    # Remove characters that might cause issues in environment variables
    alphabet = alphabet.replace("'", "").replace('"', "").replace('\\', "")
    
    # Generate the secret key
    secret_key = ''.join(secrets.choice(alphabet) for _ in range(length))
    return secret_key

if __name__ == "__main__":
    secret_key = generate_secret_key()
    print("Generated Django Secret Key:")
    print(f"SECRET_KEY={secret_key}")
    print("\nAdd this to your .env file or environment variables.")
    print("For production, make sure to keep this key secure and never commit it to version control.")