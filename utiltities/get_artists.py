#get artists from chords files from dropbox
import os

source_dir = '/Users/larrysamuels/Dropbox/Chords'
dest_dir = '/Users/larrySamuels/music_site'
dest_file = 'songs_artists_list.txt'

files_found = []
f_out = open(dest_file,'w')
for filename in os.listdir(source_dir):
# open the file, read the first line, put into a temporary file
   if not (filename.startswith('.')):
      print str(filename)
      full_name = os.path.join(source_dir, filename)
      f_in = open(full_name, 'r')
      line = f_in.readline()
      f_in.close()      
      f_out.write(line)
 