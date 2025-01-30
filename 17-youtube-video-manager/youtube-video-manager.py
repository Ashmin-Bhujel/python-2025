# YouTube Video Manager
import os, json

# Constant
FILE_NAME = "data.json"


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


# Load data helper
def load_data_helper():
    try:
        with open(FILE_NAME, "r") as data_file:
            return json.load(data_file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# Save data helper
def save_data_helper(data):
    try:
        with open(FILE_NAME, "w") as data_file:
            json.dump(data, data_file, indent=2)
    except IOError:
        print("\nError while saving data.")


# Functionalities
# List videos
def list_videos(data, show_title=True):
    if show_title:
        clear_screen_helper()
        print(f"\n{'*' * 20} All Videos {'*' * 20}\n")

    if not data:
        print("No video data available!")
    else:
        for index, video in enumerate(data, start=1):
            print(f"[{index}] {video["name"]}, Duration: {video["duration"]}")

    if show_title:
        blank_input_helper()


# Add video
def add_video(data):
    clear_screen_helper()
    print(f"\n{'*' * 20} Add a Video {'*' * 20}\n")

    video_name = input("Enter video name: ")
    video_duration = input("Enter video duration: ")

    if not invalid_data_helper(video_name, video_duration):
        video = {
            "name": video_name,
            "duration": video_duration,
        }

        data.append(video)
        save_data_helper(data)

        print(f"\n{'*' * 20} After Changes {'*' * 20}\n")
        list_videos(data, show_title=False)
        print("\nNew video added successfully.")
    else:
        print("\nInvalid data!")

    blank_input_helper()


# Update video
def update_video(data):
    clear_screen_helper()
    print(f"\n{'*' * 20} Update a Video Data {'*' * 20}\n")

    list_videos(data, show_title=False)

    index = 0
    try:
        index = int(input("\nEnter index of video to be updated: "))
    except ValueError:
        print("\nPlease enter a number!")

    if 1 <= index <= len(data):
        new_name = input("\nEnter new name: ")
        new_duration = input("Enter new duration: ")

        if not invalid_data_helper(new_name, new_duration):
            new_video = {
                "name": new_name,
                "duration": new_duration,
            }
            data[index - 1] = new_video

            save_data_helper(data)

            print(f"\n{'*' * 20} After Changes {'*' * 20}\n")
            list_videos(data, show_title=False)
            print("\nVideo updated successfully.")
        else:
            print("\nInvalid data!")
    else:
        print("\nInvalid video index!")

    blank_input_helper()


# Delete video
def delete_video(data):
    clear_screen_helper()
    print(f"\n{'*' * 20} Delete a Video Data {'*' * 20}\n")

    list_videos(data, show_title=False)

    index = 0
    try:
        index = int(input("\nEnter index of video to be deleted: "))
    except ValueError:
        print("\nPlease enter a number!")

    if 1 <= index <= len(data):
        confirm = (
            input(
                f'\nAre you sure you want to delete "{data[index - 1]["name"]}" video data? (y/n): '
            )
            .strip()
            .lower()
        )

        if confirm == "y":
            del data[index - 1]

            save_data_helper(data)

            print(f"\n{'*' * 20} After Changes {'*' * 20}\n")
            list_videos(data, show_title=False)
            print("\nVideo deleted successfully.")
        else:
            print("\nDeletion cancelled.")
    else:
        print("\nInvalid video index!")

    blank_input_helper()


# Main
def main():
    data = load_data_helper()

    while True:
        clear_screen_helper()
        print(f"\n{'*' * 20} YouTube Video Manager {'*' * 20}\n")
        print("[1] List all videos")
        print("[2] Add a video")
        print("[3] Update a video data")
        print("[4] Delete a video")
        print("[5] Exit the program")
        user_choice = input("\nEnter your choice: ")

        match user_choice:
            case "1":
                list_videos(data)
            case "2":
                add_video(data)
            case "3":
                update_video(data)
            case "4":
                delete_video(data)
            case "5":
                print("\nExiting the program.")
                break
            case _:
                print("\nInvalid choice!")
                blank_input_helper()


# Initializing program
if __name__ == "__main__":
    main()
