Code based on https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html

Tested in a Python 3.14 conda environment

## Calibration Process
To calibrate a camera, follow these steps:
1. Print out the included checkerboard pattern and photograph it on a flat surface from various angles. At least 10 photos are recommended.
2. Store them in a directory and run `CameraCalibration.py --images <DIRECTORY>`.
3. A calibration.npz file containing the camera matrix and distortion coefficients will be saved to the project directory.

## Undistortion Process
To undistort images, follow these steps:
1. Run the calibration steps or ensure that the calibration.pz file is saved in the project directory.
2. Run `undistortImages.py <FILEorDIR>` on either an image file or a directory of images.
3. Results will be saved to the "UndistortedPhotos" directory.

## Webcam Calibration
If the camera is your webcam, running the undistortVideo.py script will show you a live undistorted video feed.
