import os
import shutil

origin = './origin'
target = './target'

if not os.path.exists(target):
    os.makedirs(target)

ext_photo = ['.jpg', '.jpeg']

for filename in os.listdir(origin):
    name, ext = os.path.splitext(filename)


    if ext.lower() in ext_photo:
        old_filepath = os.path.join(origin, filename)
        new_filepath = os.path.join(target, filename)

        shutil.move(old_filepath, new_filepath)
        print(f"Berhasil Memindahkan: {filename}")

print("Proses Selesai")

