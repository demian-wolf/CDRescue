from engine import CopyFileTask
import os


for file in (os.path.join(root, name) for root, dirs, files in os.walk("F:\\") for name in files):
        task = CopyFileTask(file, "D:\\output" + file[2:])
        print(task.in_fobj.name)
        task.start()
