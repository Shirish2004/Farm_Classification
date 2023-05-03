"""
Creating Dataset: All the files for different clip were named the same so first step was to rename files followed
by creating images and their respective labels  
"""
import os 
new_name_prefix = 'image'
i=11903
folder_path=f"D:/SEM6/ArtificialIntelligence/Project/clip13"
for filename in os.listdir(folder_path):
        if filename.endswith('.tif'):
            new_filename = f'{new_name_prefix}{i}.jpg'
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            i += 1
print(i)