import os

def identifyPaths(path):
    """Load images from a file or directory."""
    imagePaths = []

    if os.path.isfile(path):
        # Single file case
        if isImageFile(path):
            imagePaths.append(path)
            
        else:
            print(f"Error: {path} is not a valid image file.")
    
    elif os.path.isdir(path):
        # Directory case
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path) and isImageFile(file_path):
                imagePaths.append(file_path)

    else:
        print(f"Error: {path} is neither a file nor a directory.")
    
    return imagePaths

def isImageFile(filename):
    """Check if a file has a valid image extension."""
    valid_extensions = (".png", ".jpg", ".jpeg", ".bmp", ".tiff")
    return filename.lower().endswith(valid_extensions)