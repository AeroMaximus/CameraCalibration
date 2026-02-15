import cv2
import numpy as np
import UndistortImages

def main():
    # Load calibration data
    with np.load('calibration.npz') as data:
        mtx = data['mtx']
        dist = data['dist']

    # Open video capture
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        undistorted = UndistortImages.undistortImage(frame, mtx, dist)

        cv2.imshow('Undistorted Frame', undistorted)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()