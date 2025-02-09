import requests
import logging

def post_to_social_media(content, platform):
    try:
        if platform.lower() == "twitter":
            # Example: Post to Twitter API
            # Replace with actual API endpoint and authentication
            response = requests.post(
                "https://api.twitter.com/2/tweets",
                json={"text": content},
                headers={"Authorization": "Bearer YOUR_TWITTER_API_KEY"}
            )
            if response.status_code == 201:
                logging.info(f"Posted to Twitter: {content}")
            else:
                logging.error(f"Twitter API error: {response.text}")

        elif platform.lower() == "facebook":
            # Example: Post to Facebook API
            # Replace with actual API endpoint and authentication
            response = requests.post(
                "https://graph.facebook.com/v12.0/me/feed",
                data={"message": content, "access_token": "YOUR_FACEBOOK_ACCESS_TOKEN"}
            )
            if response.status_code == 200:
                logging.info(f"Posted to Facebook: {content}")
            else:
                logging.error(f"Facebook API error: {response.text}")

        else:
            logging.error(f"Unsupported platform: {platform}")
            raise ValueError("Unsupported platform")

    except Exception as e:
        logging.error(f"API error: {e}")
        raise