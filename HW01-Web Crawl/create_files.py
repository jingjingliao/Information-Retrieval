import os


# Create a project folder
def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# Create a crawled file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)
