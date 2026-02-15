from tkinter import Image
import cv2
import numpy as np
import sys
import os

def load_images(path):
    """Load images from a file or directory."""
    imagePaths = []

    if os.path.isfile(path):
        # Single file case
        if is_image_file(path):
            imagePaths.append(path)
            
        else:
            print(f"Error: {path} is not a valid image file.")
    
    elif os.path.isdir(path):
        # Directory case
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path) and is_image_file(file_path):
                imagePaths.append(file_path)

    else:
        print(f"Error: {path} is neither a file nor a directory.")
    
    return imagePaths

def is_image_file(filename):
    """Check if a file has a valid image extension."""
    valid_extensions = (".png", ".jpg", ".jpeg", ".bmp", ".tiff")
    return filename.lower().endswith(valid_extensions)

def main():

    # Chessboard dimensions
    chessboard = (7, 10)

    # Termination criteria for corner refinement
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

    # Prepare 3D object points
    objp = np.zeros((chessboard[0] * chessboard[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:chessboard[0], 0:chessboard[1]].T.reshape(-1, 2)

    imageShape = []
    objpoints = []  # 3D points in real world space
    imgpoints = []  # 2D points in image plane
    imagePaths = load_images(sys.argv[1])  # Load images from the provided path

    for imgPath in imagePaths:
        img = cv2.imread(imgPath)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imageShape = gray.shape

        # Find chessboard corners
        ret, corners = cv2.findChessboardCorners(gray, chessboard, None)

        # If corners are found, refine them and add to the list
        if ret:
            corners_refined = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners_refined)
            objpoints.append(objp)

            # Draw and display the corners
    #         cv2.drawChessboardCorners(img, chessboard, corners_refined, ret)
    #         cv2.imshow('Chessboard Corners', img)
    #         cv2.waitKey(1000)

    # cv2.destroyAllWindows()

    # Camera calibration
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, imageShape[::-1], None, None)
    print("Camera matrix:\n", mtx)
    print("Distortion coefficients:\n", dist)
    np.savez('calibration.npz', mtx=mtx, dist=dist) # Save the camera matrix and distortion coefficients

if __name__ == "__main__":
    main()