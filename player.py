import pygame
pygame.init()
import library as library


song_library = library.Library()


def print_menu():
	print("pyTunes")
	print("1. View your library")
	print("2. Add a song to your library")
	print("3. Play a song")
	print("4. Exit")

print_menu()
choice = int(input("What would you like to do? (1-4): "))
while choice != 4:
	if choice == 1:
		song_library.display_library()
		print_menu()
		choice = int(input("What would you like to do? (1-4): "))
	elif choice == 2:
		ask_name = input("What is the song name? ")
		ask_artist = input("Who is " + ask_name + "'s artist? ")
		ask_path = input("Enter the file path of " + ask_name + " by " + ask_artist + ": ")
		song_library.add_song(ask_name.upper(), ask_artist.upper(), ask_path)
		print_menu()
		choice = int(input("What would you like to do? (1-4): "))
	elif choice == 3:
		if song_library.is_empty() == True:
			print("Library is empty.")
			print_menu()
			choice = int(input("What would you like to do? (1-4): "))
		else:			
			song_library.display_library()
			play = input("Which song do you want to play?: ")
			while song_library.search(play.upper()) == False:
				play = input("You don't have that song. Which song do you want to play?: ")
			value = song_library.get_song(play.upper())
			path = value.get_path()

			def menu(paused):
				if paused == True:
					print("1. Unpause")
				else:
					print("1. Pause")
				print("2. Restart")	
				print("3. Stop")

			def get_choice():
				choice = int(input("What do you want to do? (1-3): "))	
				return choice

			player = pygame.mixer.music

			player.load(path)	
			player.play()

			paused = False
			while player.get_busy():
				menu(paused)
				choice = get_choice()

				if choice == 2:
					player.rewind()
				elif choice == 3:
					player.stop()
				elif paused:
					paused = False
					player.unpause()
				elif choice == 1 and not(paused):
					paused = True
					player.pause()
			print_menu()
			choice = int(input("What would you like to do? (1-4): "))
	else:
		choice = int(input("Not a valid selection. What would you like to do? (1-4): "))




				