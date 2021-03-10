import webbrowser

class Playlist:
	def __init__(self,name,description,rating,videos):
		self.name = name
		self.description = description
		self.rating = rating
		self.videos = videos

class Video:
	def __init__(self,title,link):
		self.title = title
		self.link = link

	def open(self):
		webbrowser.open(self.link)

def select(promt):
	choice = input(promt)
	while not choice.isdigit():
		choice = input(promt)
	choice = int(choice)
	return choice

def select_in_range(promt,min,max):
	choice = input(promt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max:
		choice = input(promt)
	choice = int(choice)
	return choice

def read_playlist():
	name = input("Enter name playlist: ") + "\n"
	description = input("Enter description playlist: ") + "\n"
	rating = select_in_range("Enter rating playlist: ",1,5)
	rating = str(rating) + "\n"
	videos = read_videos()
	playlist = Playlist(name,description,rating,videos)
	return playlist

def read_playlists():
	playlists = []
	total = select("Enter total playlist: ")
	for i in range(total):
		print("Enter information playlist: " ,i+1)
		playlist = read_playlist()
		playlists.append(playlist)
	return playlists

def read_video():
	title = input("Enter title video: ") + "\n"
	link = input("Enter link video: ") + "\n"
	video = Video(title,link)
	return video

def read_videos():
	videos = []
	total = select("Enter total video: ")
	for i in range(total):
		print("Enter information video: ", i+1)
		video = read_video()
		videos.append(video)
	return videos

def write_video_to_txt(video,file):
	file.write(video.title)
	file.write(video.link)

def write_videos_to_txt(videos, file):
	total = len(videos)
	file.write(str(total) + "\n")
	for i in range(total):
		write_video_to_txt(videos[i],file)

def write_playlist_to_txt(playlist,file):
	file.write(playlist.name)
	file.write(playlist.description)
	file.write(playlist.rating) 
	write_videos_to_txt(playlist.videos, file)

def write_playlists_to_txt(playlists):
	total = len(playlists)
	with open("data.txt", "w") as file:
		file.write(str(total) + "\n")
		for i in range(total):
			write_playlist_to_txt(playlists[i],file)

def read_video_from_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title,link)
	return video

def read_videos_from_txt(file):
	videos = []
	total = file.readline()
	for i in range(int(total)):
		video = read_video_from_txt(file)
		videos.append(video)
	return videos

def read_playlist_from_txt(file):
	name = file.readline()
	description = file.readline()
	rating = file.readline()
	videos = read_videos_from_txt(file)
	playlist = Playlist(name,description,rating,videos)
	return playlist

def read_playlists_from_txt():
	playlists = []
	with open("data.txt", "r") as file:
		total = file.readline()
		for i in range(int(total)):
			playlist = read_playlist_from_txt(file)
			playlists.append(playlist)
	return playlists

def print_video(video):
	print("Video title: ", video.title, end="")
	print("Video link: ", video.link, end="")

def print_videos(videos):
	total = len(videos)
	for i in range(total):
		print("Video: ", i+1)
		print_video(videos[i]) 

def print_playlist(playlist):
	print("Playlist name: " + playlist.name, end="")
	print("Playlist description: " + playlist.description, end="")
	print("Playlist Rating: " + playlist.rating, end="")
	print_videos(playlist.videos)

def print_playlists(playlists):
	total =  len(playlists)
	for i in range(total):
		print("----------------------")
		print("Playlist: ", i+1)
		print_playlist(playlists[i])
		print("----------------------")

def select_playlist(playlists):
	print_playlists(playlists)
	total = len(playlists)
	choice = select_in_range("Choose playlist(1-" + str(total) + "): ", 1, total)
	playlist = playlists[choice-1]
	return playlist

def select_video(videos):
 	total = len(videos)
 	choice = select_in_range("Enter video:(1-" + str(total) + "): ", 1, total)
 	video = videos[choice-1]
 	return video

def play_video(playlists):
	playlist = select_playlist(playlists)
	print_playlist(playlist)
	video = select_video(playlist.videos)
	video.open()

def add_video(playlists):
	playlist = select_playlist(playlists)
	print("Writing information new video")
	title = input("Video total: " ) + "\n"
	link = input("Video link: ") + "\n"
	video = Video(title,link)
	playlist.videos.append(video)
	print("Add video Successfuly!")
	return playlists

def remove_video(playlists):
	playlist = select_playlist(playlists)
	print_playlist(playlist)
	video = select_video(playlist.videos)
	playlist.videos.remove(video)
	print("Remove video Successfuly")
	return playlists

def update_playlists(playlists):
	playlist = select_playlist(playlists)
	print("Writing new information Playlist: ")
	name = input("New name Playlist: ") + "\n"
	description = input("New description Playlist: ") + "\n"
	rating = select_in_range("New rating Playlist", 1,5)
	playlist = Playlist(name,description,rating,playlist.videos)
	return playlists

def add_playlist(playlists):
	playlist = read_playlist()
	playlists.append(playlist)
	print("Add Playlist Successfuly! ")
	return playlists

def remove_playlist(playlists):
	playlist = select_playlist(playlists)
	playlists.remove(playlist)
	print("Remove Playlist Successfuly! ")
	return playlists

def show_menu():
	print("---------------------------")
	print("|Option 1: Creat Playlists |")
	print("|Option 2: Show a Playlists|")
	print("|Option 3: Play a video    |")
	print("|Option 4: Add a video     |")
	print("|Option 5: Remove a video  |")
	print("|Option 6: Update Playlist |")
	print("|Option 7: Add Playlist    |")
	print("|Option 8: Remove Playlist |")
	print("|Option 9: Save and Exit   |")
	print("---------------------------")

def main():
	try:
		playlists = read_playlists_from_txt()
		print("Load Successfuly Playlist")

	except:
		print("Wellcome new user")
		print("Creat Playlist: ")
		playlists = read_playlists()

	while True:
		show_menu()
		choice = select_in_range("Choice Option:", 1,9)
		if choice == 1:
			playlists = read_playlists()
			input("Press Enter to continue! ")
		elif choice == 2:
			print_playlists(playlists)
			input("Press Enter to continue! ")
		elif choice == 3:
			play_video(playlists)
			input("Press Enter to continue! ")
		elif choice == 4:
			playlists = add_video(playlists)
			input("Press Enter to continue! ")
		elif choice == 5:
			playlists = remove_video(playlists)
			input("Press Enter to continue! ")
		elif choice == 6:
			playlists = update_playlists(playlists)
			input("Press Enter to continue! ")
		elif choice == 7:
			playlists = add_playlist(playlists)
			input("Press Enter to continue! ")
		elif choice == 8:
			playlists = remove_playlist(playlists)
			input("Press Enter to continue! ")
		elif choice == 9:
			write_playlists_to_txt(playlists)
			break
main()
