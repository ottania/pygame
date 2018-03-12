class Song(object):

	def __init__(self, song, artist, path):
		self.song_name = song
		self.artist_name = artist
		self.file_path = path

	def set_song(self, song):
		self.song_name = song
		return self.song_name

	def get_song(self):
		return self.song_name

	def set_artist(self, artist):
		self.artist_name = artist
		return self.artist_name	

	def get_artist(self):
		return self.artist_name	

	def set_path(self, path):
		self.file_path = path
		return self.file_path	

	def get_path(self):
		return self.file_path		
