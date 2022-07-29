import os,shutil,time
dir_path = input('enter download folder path')



def make_directories():
  dir_names = os.listdir(dir_path)
  if 'jpg' not in dir_names:
    os.mkdir(dir_path+'/jpg')
  elif 'zip' not in dir_names:
    os.mkdir(dir_path+'/zip')
  elif 'jpg' not in dir_names:
    os.mkdir(dir_path+'/jpg')
  elif 'jpeg' not in dir_names:
    os.mkdir(dir_path+'/jpeg')
  elif 'mp4' not in dir_names:
    os.mkdir(dir_path+'/mp4')
  elif 'html' not in dir_names:
    os.mkdir(dir_path+'/html')
make_directories()





def file_manager(source_file_path,destination_file_path):
  source_file = source_file_path
  destination_file = destination_file_path
  file_names = os.listdir(source_file)
  for files in file_names:
    if os.path.join(source_file,files).endswith('.jpeg'):
      try:
        shutil.move(os.path.join(source_file,files),os.path.join(destination_file,'jpeg'))
      except:
        pass

    if os.path.join(source_file,files).endswith('.pdf'):
      shutil.move(os.path.join(source_file,files),os.path.join(destination_file,'pdf'))
    if os.path.join(source_file,files).endswith('.zip'):
      try:
          shutil.move(os.path.join(source_file,files),os.path.join(destination_file,'zip'))
      except:
        pass
    if os.path.join(source_file,files).endswith('.html'):
      shutil.move(os.path.join(source_file,files),os.path.join(destination_file,'html'))
    if os.path.join(source_file,files).endswith('.jpg'):
      shutil.move(os.path.join(source_file,files),os.path.join(destination_file,'jpg'))

path_to_watch = "Downloads"
print('Your folder path is"',path_to_watch)
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  if added:
    time.sleep(1)
    file_manager('Downloads','Downloads')
                
  else:
    before = after











