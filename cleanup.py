import os
path = r'D:/2ndBrain/Clippings/Can there ever really be “one China”.md'
if os.path.exists(path):
    os.remove(path)
    print(f'Deleted: {path}')
else:
    print(f'Not found: {path}')
