# (C) Demian Wolf, 2020


import os
import sys


class CopyFileTask:
    def __init__(self, in_file, out_file, bytes_queue=None):

        self.in_fobj = open(in_file, "rb")
        self.out_fobj = open(out_file, "wb")
        
        self.stopped = True
        self.bytes_queue = bytes_queue if bytes_queue else [(pos, 1024) for pos in range(0, os.path.getsize(in_file), 1024)]  # TODO: will it skip the last byte?

    def start(self):
        self.stopped = False
        while not self.stopped:
            pos, step = self.bytes_queue.pop(0)
            print(f"{self.in_fobj.name} Reading bytes from {pos} to {pos + step}", end="\r")

            self.in_fobj.seek(pos)
            self.out_fobj.seek(pos)
            try:
                self.out_fobj.write(self.in_fobj.read(step))
            except PermissionError:
                print(f"{self.in_fobj.name} ERROR: unable to read bytes from {pos} to {pos + step}.", end=" ")
                step = max(step // 2, 1)  # step shouldn't be 0 in the case if the previous one was 1
                self.bytes_queue.append((pos, step))
                if step > 1:
                    self.bytes_queue.append((pos + step, step))
                print(f"Added to queue {self.bytes_queue[-2:]}.")
                
            if not self.bytes_queue:
                print(f"{self.in_fobj.name} Done OK!")
                break

    def stop(self):
        self.stopped = True

if __name__ == "__main__":
    print("This module is for internal usage only. Please don't call it directly.", file=sys.stderr)
    print("Run cli.py or tkinter_gui.pyw instead.", file=sys.stderr)
