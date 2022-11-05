import glob
import os
import shutil


files = sorted([file for file in glob.glob('zip/*.zip')])
for file in files:
    shutil.unpack_archive(file, 'tmpdir')
    inner_files = [f for f in glob.glob('tmpdir/*/*/*')]
    for fin in inner_files:
        time_dir, fname = fin.split('/')[2:]
        time_dir = f"data/{time_dir}"
        import os
        os.makedirs(time_dir, exist_ok=True)
        shutil.move(fin, f"{time_dir}/{fname}")
