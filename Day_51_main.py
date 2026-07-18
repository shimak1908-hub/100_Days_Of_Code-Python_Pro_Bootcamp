import tweepy
import random
import time

# --- CONFIGURATION SETTINGS ---
# Replace these strings with your actual developer keys from the portal
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ACCESS_TOKEN_SECRET = "YOUR_ACCESS_TOKEN_SECRET"

# Customize your target ISP handle and status variations
ISP_HANDLE = "@YourISPHandle"  # e.g., @Xfinity, @Spectrum, @ATT

# A list of text variants to make your automated messages sound more organic
COMPLAINT_TEMPLATES = [
    f"Hey {ISP_HANDLE}, my connection has been dropping out completely for the past hour. Is there an outage in my area?",
    f"Is anyone else experiencing high latency and packet loss on {ISP_HANDLE} right now? Hard to get any work done.",
    f"Fix the stability please {ISP_HANDLE}. Speeds are drastically below what I am paying for today.",
    f"Extremely unstable network today {ISP_HANDLE}. Can we get an update on system maintenance?"
]


def initialize_x_client():
    """Authenticates using X API v2 credentials."""
    try:
        client = tweepy.Client(
            consumer_key=API_KEY,
            consumer_secret=API_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )
        print("[System] X API Client authenticated successfully.")
        return client
    except Exception as e:
        print(f"[Error] Authentication failed: {e}")
        return None


def post_automated_tweet(client):
    """Selects a random complaint template and posts it."""
    # Select a random text variation to prevent 'duplicate status' API blocks
    message = random.choice(COMPLAINT_TEMPLATES)

    # Optional: Append a timestamp or a random digit to make every tweet 100% unique
    timestamp = time.strftime("%H:%M")
    final_tweet = f"{message} [Status Log: {timestamp}]"

    try:
        print(f"[Action] Attempting to tweet: \"{final_tweet}\"")
        response = client.create_tweet(text=final_tweet)
        print(f"[Success] Tweet posted successfully! Tweet ID: {response.data['id']}")
    except Exception as e:
        print(f"[Error] Failed to post tweet: {e}")


if __name__ == "__main__":
    # 1. Initialize the communication bridge
    x_client = initialize_x_client()

    if x_client:
        # 2. Fire the automation
        post_automated_tweet(x_client)