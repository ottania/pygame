import song as song

class Library(object):

	def __init__(self):
		self.songs = {}
		
	def display_library(self):
		print("Here are all your songs:")
		for songs, value in self.songs.items():
			print(songs, value.get_artist())

	def get_song(self, song_name):
		return self.songs[song_name]

	def search(self, song_name):
		if song_name in self.songs:
			return True
		else:
			return False
				
	def add_song(self, song_name, artist_name, path):
		new_song = song.Song(song_name, artist_name, path)
		self.songs[song_name] = new_song

	def is_empty(self):
		if self.songs:
			return False
		else:
			return True	