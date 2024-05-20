## Project: Playlist Management API


Author: James Carlson

This project was built as an assignment for Coding Temple.

---

<br>This application simulates a collection of playlists and the songs they store. I began this application with a comment block analyzing which data structures would be most effective for storing, adding to, and searching for songs. Ultimately, I chose a dictionary of doubly linked lists to represent each playlist, with songs as nodes.

This application includes several endpoints for managing playlists and songs:

#### <b>Playlist Endpionts</b>
- <b>Create Playlist</b> <em> /playlist/create</em> - Create an empty playlist with a `name` and `description`. `playlist_id` is automatically assigned.
- <b>Get Playlist</b> <em>/playlist/\<int:playlist_id\></em> - Fetch playlist by `playlist_id`.
- <b>Update Playlist</b> <em>/playlist/update/\<int:playlist_id\></em> - Update `name` and `description` for playlist at `playlist_id`.
- <b>Delete Playlist</b> <em>/playlist/delete/\<int:playlist_id\></em> - Remove playlist from collection using `playlist_id`.
#### <b>Song Endpoints</b>
- <b>Add Song</b> <em>/playlist/\<int:playlist_id\>/add_song</em> - Add a song with `title`, `artist`, `album`, and `genre` to the playlist with `playlist_id`. `song_id` is automatically assigned.
- <b>Remove Song</b> <em>/playlist/\<int:playlist_id\>/remove_song/\<int:song_id\></em> - Remove song with `song_id` from `playlist_id`.
- <b>Search Song</b> <em>/playlist/\<int:playlist_id\>/search?search={search}&property={property}</em> - Search for matching song within playlist at `playlist_id`, using search parameters `search` (the search term) and `property` (the song attribute to search).

<br>Thank you for reviewing my code!