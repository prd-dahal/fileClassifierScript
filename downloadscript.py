import os

import shutil
documents=['.txt','.doc','.xlsx','.pdf','.pptx','.docx','.odp','.ppt','.crt','.rtf','.torrent']
code=['.c','.cpp']
software=['.exe','.run','.iso','.apk','.EXE']
zip=['.rar','.zip','.cab']
multimedia=['.mp3','.mp4','.mkv','.m4v','.avi']
photos=['.jpeg','.jpg','.png']
path=os.getcwd()
#making the folders in the path
folders=['documents','code','software','zip','multimedia','photos']
try:
	for i in folders:
		os.mkdir(i)
except:
	pass
for i in (os.listdir()):
	filename,file_extension=os.path.splitext(i)
	if(file_extension in documents):
		shutil.move(path+'\\'+i,path+'\\documents\\')
	if(file_extension in code):
		shutil.move(path+'\\'+i,path+'\\code\\')
	if(file_extension in software):
		shutil.move(path+'\\'+i,path+'\\software\\')
	if(file_extension in zip):
		shutil.move(path+'\\'+i,path+'\\zip\\')
	if(file_extension in photos):
		shutil.move(path+'\\'+i,path+'\\photos\\')
	if(file_extension in multimedia):
		shutil.move(path+'\\'+i,path+'\\multimedia\\')
