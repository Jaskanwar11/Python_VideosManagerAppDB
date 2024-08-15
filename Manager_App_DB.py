import sqlite3

con = sqlite3.connect('Youtube_videos.db')
cursor = con.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS Videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
        ) 
''')


def list_all_videos():
    cursor.execute("SELECT * FROM Videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO  Videos (name, time) VALUES (?, ?) ", (name, time))
    con.commit()

def update_video(Video_Id, name, time):
    cursor.execute("UPDATE Videos SET name = ?, time = ? WHERE id = ?", (name, time, Video_Id))
    con.commit()

def delete_video(Video_Id):
    cursor.execute("DELETE FROM Videos WHERE id = ?", (Video_Id,))
    con.commit()

def main():
    while True:
        print("_"*70)
        print("\nYoutube Manager App")
        print("1: List all youtube videos")
        print("2: Add a youtube video")
        print("3: Update a youtube video")
        print("4. Delete a youtube video")
        print("5: Exit the app!")
        choice = input("Choose a number: ")
        print("_"*70)
        print("")
        

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter Video Name: ")
                time = input("Enter Video time: ")
                add_video(name, time)
            case '3':
                video_Id = input("Enter video id: ")
                name = input("New Video Name: ")
                time = input("New Video time: ")
                update_video(video_Id, name, time)
            case '4':
                video_Id = input("Enter video id: ")
                delete_video(video_Id)
            case '5':
                break
            case _:
                print("Invalid choice!")
    
    con.close()

if __name__ == "__main__":
    main()