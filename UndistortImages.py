import cv2
import numpy as np
import selectImages
import argparse
import os
import logging

def undistortImage(frame, mtx, dist):
    h, w = frame.shape[:2]
    new_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
    undistorted = cv2.undistort(frame, mtx, dist, None, new_mtx)
    x,y,w,h = roi
    undistorted = undistorted[y:y+h, x:x+w]
    return undistorted

def main():
    parser = argparse.ArgumentParser(description='Undistort images based on calibration file.')
    parser.add_argument('images', type=str, help='Directory containing images to undistort or a single image file.')
    args = parser.parse_args()

    logging.basicConfig(
        format="{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M",
        level=logging.INFO
    )

    # Load calibration data
    with np.load('calibration.npz') as data:
        mtx = data['mtx']
        dist = data['dist']

    # Identify paths to images
    imagePaths = selectImages.identifyPaths(args.images)

    # Create output directory if it doesn't exist
    if not os.path.exists("UndistortedPhotos"):
        os.makedirs("UndistortedPhotos")

    for imgPath in imagePaths:
        img = cv2.imread(imgPath)
        undistorted = undistortImage(img, mtx, dist)

        # Save the undistorted image
        output_path = os.path.join("UndistortedPhotos", "Undistorted_" + os.path.basename(imgPath))
        cv2.imwrite(output_path, undistorted)
        logging.info(f"Saved undistorted image to: {output_path}")

if __name__ == "__main__":
    main()