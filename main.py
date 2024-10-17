import tweepy
import schedule
import time
from datetime import datetime, date, timedelta
import pytz
from json import dumps

# Correctly set your credentials here:
TWITTER_API_KEY = 'eZI0pLxtG9J0UMrUBnoIJYKuk'  # Replace with your actual Consumer Key
TWITTER_API_SECRET_KEY = 'ufFQQMedJ4bzSF1IBhvrT1tFBnmuygXevo6knr9vRDfPkO5Ika'  # Replace with your actual Consumer Secret
TWITTER_ACCESS_TOKEN = '1729497285011415040-WYgSgE3j5OF6bf1PnAwg0m7AidB4Rf'  # Replace with your actual Access Token
TWITTER_ACCESS_TOKEN_SECRET = 'G3PRHlFzaKT33mS7Irvb0chw25Od1FyXaB9hYzEUN8E2T'  # Replace with your actual Access Token Secret


# Create tweepy client
client = tweepy.Client(consumer_key=TWITTER_API_KEY,
                       consumer_secret=TWITTER_API_SECRET_KEY,
                       access_token=TWITTER_ACCESS_TOKEN,
                       access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

# Define IST timezone
ist = pytz.timezone('Asia/Kolkata')

# Function to calculate days countdown and tweet
def tweet_countdown():
    target_date = date(2025, 3, 28)  # Set your countdown target date
    days_left = target_date - date.today()

    # Convert days remaining to a string
    cd = dumps(days_left.days, default=str)

    try:
        response = client.create_tweet(text=f"{cd} days left for #HHVM")
        print(f"Tweet successful! Tweet ID: {response.data['id']}")
    except Exception as e:
        print(f"Error while tweeting: {e}")

# Schedule the tweet to run every day at 12:00 PM IST
def schedule_tweets():
    while True:
        # Get the current time in IST
        now = datetime.now(ist)
        # Check if it's exactly 12:00 PM IST
        if now.hour == 00 and now.minute == 00:
            tweet_countdown()
            time.sleep(60)  # Prevent multiple tweets at the same minute
        time.sleep(30)  # Check again every 30 seconds

# Run the scheduling function
if __name__ == "__main__":
    schedule_tweets()
