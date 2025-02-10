from api_integration import post_to_social_media
from database import save_post, get_scheduled_posts, delete_post
import schedule
import time
from datetime import datetime
import threading
import logging

def schedule_post(content, platform, schedule_time):
    try:
        scheduled_time = datetime.strptime(schedule_time, "%Y-%m-%d %H:%M")
        save_post(content, platform, scheduled_time)
        schedule.every().day.at(scheduled_time.strftime("%H:%M")).do(
            post_to_social_media, content=content, platform=platform
        )
        logging.info(f"Scheduled post: {content} for {platform} at {schedule_time}")
        print("Post scheduled successfully!")
    except Exception as e:
        logging.error(f"Error scheduling post: {e}")
        print("Invalid date/time format or other error. Please try again.")

def view_scheduled_posts():
    posts = get_scheduled_posts()
    if not posts:
        print("No scheduled posts.")
    else:
        for post in posts:
            print(f"ID: {post[0]}, Content: {post[1]}, Platform: {post[2]}, Time: {post[3]}")

def post_now(content, platform):
    try:
        post_to_social_media(content, platform)
        logging.info(f"Posted immediately: {content} to {platform}")
        print("Post published successfully!")
    except Exception as e:
        logging.error(f"Error posting: {e}")
        print("Failed to post. Please check your API keys or network connection.")

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start the scheduler in a separate thread
threading.Thread(target=run_scheduler, daemon=True).start()