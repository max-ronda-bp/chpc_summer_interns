import os

def create_directory(path):
    """Helper function. Function creates
    directories.
    
    Parameters
    ----------
        path : string. a path
            A path where you want to create new directory
    """
    try:
        exists = os.path.exists(path)
        
        if not exists:
            os.mkdir(path)
    except Exception as e:
        print(f"An exception occurred: {e}")