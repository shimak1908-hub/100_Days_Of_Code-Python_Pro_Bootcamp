import yfinance as yf
from twilio.rest import Client

# --- TWILIO CONFIGURATION ---
TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "YOUR_TWILIO_PHONE_NUMBER"  # Sent FROM this Twilio number
RECIPIENT_PHONE_NUMBER = "YOUR_PERSONAL_PHONE_NUMBER"  # Sent TO this number

# --- STOCK WATCHLIST ---
# Add any tickers you want to monitor (e.g., AAPL, TSLA, GOOG, MSFT)
WATCHLIST = ["AAPL", "TSLA", "GOOG"]


def get_stock_updates(tickers):
    """Fetches real-time price changes for a list of stock tickers."""
    update_lines = ["📈 Stock Market Update:"]

    for symbol in tickers:
        try:
            # Fetch the most recent 2 days of market data to compare close prices
            ticker = yf.Ticker(symbol)
            history = ticker.history(period="2d")

            if len(history) < 2:
                continue

            # Get yesterday's close and today's latest price
            previous_close = history['Close'].iloc[0]
            current_price = history['Close'].iloc[1]

            # Calculate dollar and percentage variance
            price_change = current_price - previous_close
            percent_change = (price_change / previous_close) * 100

            # Assign a visual direction indicator
            direction_emoji = "🟢 +" if price_change >= 0 else "🔴 "

            update_lines.append(
                f"{symbol}: ${current_price:.2f} ({direction_emoji}{percent_change:.2f}%)"
            )
        except Exception as error:
            print(f"Error gathering data for {symbol}: {error}")

    # Combine into a single text body text block
    return "\n".join(update_lines) if len(update_lines) > 1 else None


def send_sms(message_body):
    """Triggers the Twilio REST API client to send out the message block."""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=RECIPIENT_PHONE_NUMBER
        )
        print(f"SMS successfully sent! Message SID: {message.sid}")
    except Exception as error:
        print(f"Failed to dispatch SMS through Twilio: {error}")


if __name__ == "__main__":
    print("Fetching live stock summaries...")
    market_report = get_stock_updates(WATCHLIST)

    if market_report:
        print("\n--- Outgoing SMS Preview ---")
        print(market_report)
        print("----------------------------\n")

        print("Sending message...")
        send_sms(market_report)
    else:
        print("No valid stock data was retrieved. SMS transmission canceled.")