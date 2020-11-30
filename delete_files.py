import os
import glob

for folder in ['Desktop', 'Downloads']:
    path = "/Users/jjespinoza/{0}/*".format(folder)
    files = glob.glob(path)
    for f in files:
        os.remove(f)