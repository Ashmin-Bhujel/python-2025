# Video Manager with SQLite3
import sqlite3, os

# Constant
DB_FILE = "data.db"
TABLE_NAME = "videos"


# Helpers
# Clear screen helper
def clear_screen_helper():
    os.system("cls" if os.name == "nt" else "clear")


# Blank input helper
def blank_input_helper():
    input("\nPress enter to continue.")


# Invalid data helper
def invalid_data_helper(name, duration):
    return not name.strip() or not duration.strip()


# ID validator
def id_validator(id):
    try:
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT id FROM {TABLE_NAME} WHERE id = ?",
                (id,),
            )
            result = cursor.fetchone()
            return True if result != None and id in result else False
    except (ConnectionError, sqlite3.OperationalError):
        print("\nFailed to validate ID!")
        return False


# Fetch one row helper
def fetch_one_row_helper(id):
    try:
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            cursor.execute(
                f"SELECT * FROM {TABLE_NAME} WHERE id = ?",
                (id,),
            )
            return cursor.fetchone()
    except (ConnectionError, sqlite3.OperationalError):
        print("\nFailed to validate ID!")
        return tuple()


# Load data helper
def load_data_helper():
    try:
        with sqlite3.connect(DB_FILE) as connection:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {TABLE_NAME}")
            return cursor.fetchall()
    except (ConnectionError, sqlite3.OperationalError):
        print("\nFailed to load data!")


# Functionalities
# List videos
def list_videos(show_title=True):
    if show_title:
        clear_screen_helper()
        print(f"\n{'*' * 20} All Videos {'*' * 20}\n")

    data = load_data_helper()

    if not data:
        print("No video data available!")
    else:
        for video in data:
            print(f"[{video[0]}] {video[1]}, Duration: {video[2]}")

    if show_title:
        blank_input_helper()


# Add video
def add_video():
    clear_screen_helper()
    print(f"\n{'*' * 20} Add a Video {'*' * 20}\n")

    video_name = input("Enter video name: ")
    video_duration = input("Enter video duration: ")

    if not invalid_data_helper(video_name, video_duration):
        try:
            with sqlite3.connect(DB_FILE) as connection:
                connection.cursor().execute(
                    f"INSERT INTO {TABLE_NAME} (name, duration) VALUES (?, ?)",
                    (video_name, video_duration),
                )
                connection.commit()
        except (ConnectionError, sqlite3.OperationalError):
            print("\nFailed to add video!")

        print(f"\n{'*' * 20} After Changes {'*' * 20}\n")
        list_videos(show_title=False)
        print("\nNew video added successfully.")
    else:
        print("\nInvalid data!")

    blank_input_helper()


# Update video
def update_video():
    clear_screen_helper()
    print(f"\n{'*' * 20} Update a Video {'*' * 20}\n")

    list_videos(show_title=False)

    id = 0
    try:
        id = int(input("\nEnter ID of video to be updated: "))
    except ValueError:
        print("\nPlease enter a number!")

    if id_validator(id):
        new_name = input("\nEnter new name: ")
        new_duration = input("Enter new duration: ")

        if not invalid_data_helper(new_name, new_duration):
            try:
                with sqlite3.connect(DB_FILE) as connection:
                    connection.cursor().execute(
                        f"UPDATE {TABLE_NAME} SET name = ?, duration = ? WHERE id = ?",
                        (new_name, new_duration, id),
                    )
                    connection.commit()
            except (ConnectionError, sqlite3.OperationalError):
                print("\nFailed to update video!")

            print(f"\n{'*' * 20} After Changes {'*' * 20}\n")
            list_videos(show_title=False)
            print("\nVideo updated successfully.")
        else:
            print("\nInvalid data!")
    else:
        print("\nInvalid video ID!")

    blank_input_helper()


# Delete video
def delete_video():
    clear_screen_helper()
    print(f"\n{'*' * 20} Delete a Video {'*' * 20}\n")

    list_videos(show_title=False)

    id = 0
    try:
        id = int(input("\nEnter ID of video to be deleted: "))
    except ValueError:
        print("\nPlease enter a number!")

    if id_validator(id):
        video_name = fetch_one_row_helper(id)[1]
        confirm = (
            input(f'\nAre you sure you want to delete "{video_name}" video? [y/n]: ')
            .strip()
            .lower()
        )

        if confirm == "y":
            try:
                with sqlite3.connect(DB_FILE) as connection:
                    connection.cursor().execute(
                        f"DELETE FROM {TABLE_NAME} WHERE id = ?",
                        (id,),
                    )
                    connection.commit()
            except (ConnectionError, sqlite3.OperationalError):
                print("\nFailed to delete video!")

            print(f"\n{'*' * 20} After Changes {'*' * 20}\n")
            list_videos(show_title=False)
            print("\nVideo deleted successfully.")
        else:
            print("\nVideo Deletion cancelled!")
    else:
        print("\nInvalid video ID!")

    blank_input_helper()


# Main
def main():
    # Create videos table if not exists already
    try:
        with sqlite3.connect(DB_FILE) as connection:
            connection.cursor().execute(
                f"""
                    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        duration TEXT NOT NULL
                    )
                """
            )
    except (ConnectionError, sqlite3.OperationalError):
        print(f"\nFailed to create {TABLE_NAME} table!")

    while True:
        clear_screen_helper()
        print(f"\n{'*' * 20} Video Manager {'*' * 20}\n")
        print("[1] List all videos")
        print("[2] Add a video")
        print("[3] Update a video")
        print("[4] Delete a video")
        print("[5] Exit the program")
        user_choice = input("\nEnter your choice: ")

        match user_choice:
            case "1":
                list_videos()
            case "2":
                add_video()
            case "3":
                update_video()
            case "4":
                delete_video()
            case "5":
                print("\nExiting the program.")
                break
            case _:
                print("\nInvalid choice!")
                blank_input_helper()


# Initializing program
if __name__ == "__main__":
    main()
