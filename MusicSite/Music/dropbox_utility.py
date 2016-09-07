#dropbox_utility,py
from models import DropBoxAccount, Song
import dropbox
from dropbox.client import DropboxClient

def GenerateAccessToken():
    #see if any entries in DropBoxAccount
    if DropBoxAccount.objects.count() == 0:
       # create an enry
       dba = DropBoxAccount(app_key = '8a1wet1kfcj85xx', app_secret = 'fjxnzf2g9aevmeq', access_token = '')
       dba.save()
       return
    else:
       dba = DropBoxAccount.objects.get(pk=1)
       if dba.access_token == '':
          # entry created, but no access code
          return PromptForAccessCode()
       else:
          #we have an access code, use it
          return

def PromptForAccessCode():
   dba = DropBoxAccount.objects.get(pk=1)
   # Have the user sign in and authorize this token
   flow = dropbox.client.DropboxOAuth2FlowNoRedirect(dba.app_key, dba,app_secret)
   authorize_url = flow.start()
   print '1. Go to: ' + authorize_url
   print '2. Click "Allow" (you might have to log in first)'
   print '3. Copy the authorization code.'
   code = raw_input("Enter the authorization code here: ").strip() 
   # This will fail if the user enters an invalid authorization code
   token, user_id = flow.finish(code)
   print 'token is ' + token
   dba.acces_code = token
   dba.save()

def list_files(client, files=None, cursor=None):
   #get all files from drop box client
   if files is None:
      files = {}
   has_more = True
   while has_more:
      result = client.delta(cursor)
      cursor = result['cursor']
      has_more = result['has_more']
      for lowercase_path, metadata in result['entries']:
         if metadata is not None:
            files[lowercase_path] = metadata
         else:
            # no metadata indicates a deletion
            # remove if present
            files.pop(lowercase_path, None)
        # in case this was a directory, delete everything under it
      for other in files.keys():
         if other.startswith(lowercase_path + '/'):
            del files[other]
   return files, cursor

def GetFilesInDir(dir_name):
   #given directory in drop box, return list of all file names, including path
   dba = DropBoxAccount.objects.get(pk=1)
   token = dba.access_token
   client = dropbox.client.DropboxClient(token)
   files, cursor = list_files(DropboxClient(token))
   file_list = []
   for item in files.items():
      f = item[0]
      if f.startswith(dir_name):
          file_list.append(f)
          print f
   return file_list

def GetTextFileContent(file_id):
   #return string representation of file stored on dropbox
   try:
      song = Song.objects.get(pk=file_id)
      file_name = song.file_name
      print 'GetTextFileContent ' + file_name
      dba = DropBoxAccount.objects.get(pk=1)
      token = dba.access_token
      print 'GetTextFileContent token ' + token
      client =  client = dropbox.client.DropboxClient(token)
      f, metadata = client.get_file_and_metadata(file_name)
      return str(f.read())
   except:
      print 'GetTextFileContent ' + str(file_id) + ' Error'
      return 'No Content'

   