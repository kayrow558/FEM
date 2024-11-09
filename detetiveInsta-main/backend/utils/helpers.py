import os
import time

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def rename_profile_pics():
    # Substitua 'profile_images' pelo caminho correto para sua pasta de imagens
    base_dir = 'profile_images'

    
    for root, dirs, files in os.walk(base_dir):
        for file_name in files:
            if '_profile_pic' in file_name:
                original_path = os.path.join(root, file_name)
                new_path = os.path.join(root, 'profile_pic.jpg')
                time.sleep(4)
                if os.path.exists(new_path):
                    os.remove(new_path)
                    time.sleep(3)
                os.rename(original_path, new_path)