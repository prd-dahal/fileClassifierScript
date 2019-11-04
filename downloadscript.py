
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
#make folders if doesn't exist
try:
	for i in folders:
		os.mkdir(i)
except:
	pass
#goes through all the file names that is in the directory i.e os.listdir() lists all the file in the current directory

for i in (os.listdir()):
	#splits filename and extnsion of each file 
	filename,file_extension=os.path.splitext(i)
	#shutil.move(source,destination)
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
