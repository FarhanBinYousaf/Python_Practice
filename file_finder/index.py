import os, shutil
dict_extensions  = {
    'audio_extensions' : ('.mp3','.m4a','.wav','.flac'),
    'video_extentions' : ('.mp4','.mkv','.MKV','.flv','mpeg'),
    'documents_extenstions' : ('.docx','.doc','.txt','.pdf'),
    'CyberImage_extenstions' : ('.png','.jpg'),
}
folderpath = input("Etner Folder Path: ")
def file_finder(folder_path,file_extensions):
    files = []
    for file in os.listdir(folder_path):
        for extention in file_extensions:
            if file.endswith(extention):
                files.append(file)
    return files

for extension_type , extentsion_tuple in dict_extensions.items():
    folder_name = extension_type.split('_')[0] + 'Files'
    folder_path_2 = os.path.join(folderpath,folder_name)
    os.mkdir(folder_path_2)
    for item in file_finder(folderpath,extentsion_tuple):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_path_2,item)
        shutil.move(item_path,item_new_path)
