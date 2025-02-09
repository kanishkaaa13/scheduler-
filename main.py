import scheduler
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='logs/scheduler.log', level=logging.INFO, format='%(asctime)s - %(message)s')

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