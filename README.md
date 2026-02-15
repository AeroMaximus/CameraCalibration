Code based on https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html

Tested in a Python 3.11 conda environment

To calibrate a camera:
 1. Print out the included checkerboard pattern and photograph it on flat surface from various angles. About 10 photos are recommended.
 2. Store them in a directory and run CameraCalibration.py <DIRECTORY>
 3. A calibration.npz file containing the camera matrix and distortion coefficients will be saved to the project directory

To undistort images:
 1. Run the calibration steps or ensure the calibration.pz file is saved ot the project directory 
 2. Run undistortImages.py <FILEorDIR> on either an image file or directory of images
 3. Results will be saved to the "UndistortedPhotos" directory

If the camera is your webcam, running the undistortVideo.py script will show you a live undistorted video feed.
