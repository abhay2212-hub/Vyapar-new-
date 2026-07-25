import os, shutil

root_dir = 'c:/Users/hp/OneDrive/Desktop/vasroventures.com'
sub_dir = os.path.join(root_dir, 'vasroventures.com')

# Move all items from sub_dir up into root_dir
for item in os.listdir(sub_dir):
    src_path = os.path.join(sub_dir, item)
    dst_path = os.path.join(root_dir, item)

    if os.path.isdir(src_path):
        if os.path.exists(dst_path):
            shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
            shutil.rmtree(src_path)
        else:
            shutil.move(src_path, dst_path)
    else:
        if os.path.exists(dst_path):
            os.remove(dst_path)
        shutil.move(src_path, dst_path)

print("Moved all website files and directories to the repository root.")

# Remove empty sub_dir
try:
    os.rmdir(sub_dir)
    print("Removed empty vasroventures.com subfolder.")
except Exception as e:
    print("Subfolder note:", e)
