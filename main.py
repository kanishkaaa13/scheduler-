import os
import logging
import scheduler
from datetime import datetime

# Create the logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Configure logging
logging.basicConfig(
    filename='logs/scheduler.log',  # Log file path
    level=logging.INFO,             # Log level (INFO, DEBUG, ERROR, etc.)
    format='%(asctime)s - %(message)s'  # Log message format
)

def main():
    print("Social Media Content Scheduler")
    while True:
        print("\n1. Schedule Post\n2. View Scheduled Posts\n3. Post Now\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            content = input("Enter post content: ")
            platform = input("Enter platform (e.g., Twitter, Facebook): ")
            schedule_time = input("Enter schedule time (YYYY-MM-DD HH:MM): ")
            scheduler.schedule_post(content, platform, schedule_time)

        elif choice == '2':
            scheduler.view_scheduled_posts()

        elif choice == '3':
            content = input("Enter post content: ")
            platform = input("Enter platform (e.g., Twitter, Facebook): ")
            scheduler.post_now(content, platform)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()