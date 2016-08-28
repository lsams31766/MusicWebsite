#get list of chords files from dropbox
from os import walk

source_dir = '/Users/larrysamuels/Dropbox/Chords'
dest_dir = '/Users/larrySamuels/music_site'
dest_file = 'songs_list.txt'

files_found = []
for (dirpath, dirnames, filenames) in walk(source_dir):
    files_found.extend(filenames)
    break

#save the file list, skip files that start with '.'
#also remove the .txt at the end
f_out = open(dest_file, 'w')
for file in files_found:
   if not (file.startswith('.')):
      fixed_file = file.replace('.txt','')
      f_out.write(str(fixed_file))
      f_out.write('\n')
   #print str(file)
