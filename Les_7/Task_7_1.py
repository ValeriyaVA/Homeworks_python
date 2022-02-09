import os

parent_dir = 'my_project'
daughter_dirs = ['settings', 'mainapp', 'adminapp', 'authapp']
path = os.path.join(os.getcwd(), parent_dir)
if not os.path.exists(path):
    os.mkdir(path)
os.chdir(path)
for dir in daughter_dirs:
    daughter_path = os.path.join(dir)
    if not os.path.exists(daughter_path):
        os.mkdir(daughter_path)
