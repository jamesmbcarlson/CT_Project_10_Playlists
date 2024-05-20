global_song_id = 0

# nodes for the doubly linked list hold song information as well as next and prev pointers
class SongNode:
    def __init__(self, title, artist, album, genre):
        # set unique song id
        global global_song_id
        self.song_id = global_song_id
        global_song_id += 1

        # set song info with parameters
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre

        # nodes for doubly linked list
        self.next = None
        self.prev = None

    def __str__(self):
        return f"ID #{self.song_id}\n{self.title} by {self.artist}\nAlbum: {self.album}\nGenre: {self.genre}\n"


# doubly linked list of songs
class SongsList:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.start = None
        self.current = None


    def add_song(self, title, artist, album, genre):
        '''Add new song to playlist.'''

        # Create new node for song in linked list
        new_song = SongNode(title, artist, album, genre)

        # If the playlist is empty, mark the new song as the start of the playlist
        if self.start is None:
            self.start = new_song
            
        # otherwise, add the new song to the end of the playlist
        else:
            node = self.start
            while node.next is not None:
                node = node.next
            node.next = new_song
            new_song.prev = node


    def remove_song(self, song_id):
        '''Remove song from playlist using song_id.'''

        # check for empty playlist
        if self.start is None:
            print(f'The playlist "{self.name}" is empty\n')
            return False
        
        # if the song to be removed is the start of the playlist, check for "next" song to make playlist start
        if self.start.song_id == song_id:
            self.start = self.start.next
            if self.start:
                self.start.prev = None
            return True
        
        # otherwise, search for list for song to remove and remove it, if it is found
        current_node = self.start
        while current_node:
            if current_node.song_id == song_id:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                return True
            current_node = current_node.next

        # song not found in playlist
        print(f'Song ID #{song_id} not found in playlist "{self.name}" playlist.\n')
        return False


    def play_next(self):
        '''Play the next song in the playlist.'''

        # if nothing is playing, begin playlist
        if self.current is None:
            self.current = self.start
        
        # otherwise, go to next song node
        else:
            self.current = self.current.next

        # if a song exists at new position, play the song
        if self.current is not None:
            print(f"Now Playing: {self.current.title} by {self.current.artist}")

        # otherwise...
        else:
            print(f"The playlist has finished!\n")


    def play_prev(self):
        '''Play the previous song in the playlist.'''

        # check if we can go back in playlist
        if self.current is None:
            print(f'At the beginning of playlist "{self.name}"\n')

        # go to previous song node
        else:
            self.current = self.current.prev
            if self.current is not None:
                song = self.current.song
                print(f"Playing Previous Song: {self.current.title} by {self.current.artist}")

            # we are back at the beginning of the playlist
            else:
                print(f'At the beginning of playlist "{self.name}"\n')

    def search_songs(self, search_key, property="song_id"):
        '''Search for song in linked list by 'search_key' of type 'property'.'''

        # start at beginning and search through list by search key
        search_node = self.start
        while search_node:
            check_property = getattr(search_node, property)
            if check_property == search_key:
                return search_node
            search_node = search_node.next
        
        # search_key not found
        return None
    
    def print_songs(self):
        '''Print all songs in linked list.'''

        # add all songs to list to return
        if self.start is None:
            return None
        return_list = []
        print_node = self.start
        while print_node:
            return_list.append(
                {
                    "Song ID" : print_node.song_id,
                    "Title" : print_node.title,
                    "Artist" : print_node.artist,
                    "Album" : print_node.album,
                    "Genre" : print_node.genre
                }
            )
            print_node = print_node.next
        return return_list