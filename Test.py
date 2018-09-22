import cv2
import numpy as np


def main():
    upper_hsv = np.array([197, 235, 255])
    lower_hsv = np.array([127, 129, 154])

    color_sploch = np.zeros((300, 500, 3), np.uint8)

    def update_hav(x):
        color_upper = np.zeros((300, 250, 3), np.uint8)
        color_lower = np.zeros((300, 250, 3), np.uint8)

        upper_hsv[0] = cv2.getTrackbarPos('Upper_H', 'Color')
        upper_hsv[1] = cv2.getTrackbarPos('Upper_S', 'Color')
        upper_hsv[2] = cv2.getTrackbarPos('Upper_V', 'Color')

        lower_hsv[0] = cv2.getTrackbarPos('Lower_H', 'Color')
        lower_hsv[1] = cv2.getTrackbarPos('Lower_S', 'Color')
        lower_hsv[2] = cv2.getTrackbarPos('Lower_V', 'Color')

        color_upper[:] = [upper_hsv[0], upper_hsv[1], upper_hsv[2]]
        color_lower[:] = [lower_hsv[0], lower_hsv[1], lower_hsv[2]]
        np.copyto(color_sploch, cv2.cvtColor(np.hstack((color_lower, color_upper)), cv2.COLOR_HSV2BGR))

    cv2.namedWindow('Color')

    cv2.createTrackbar('Upper_H', 'Color', upper_hsv[0], 255, update_hav)
    cv2.createTrackbar('Upper_S', 'Color', upper_hsv[1], 255, update_hav)
    cv2.createTrackbar('Upper_V', 'Color', upper_hsv[2], 255, update_hav)

    cv2.createTrackbar('Lower_H', 'Color', lower_hsv[0], 255, update_hav)
    cv2.createTrackbar('Lower_S', 'Color', lower_hsv[1], 255, update_hav)
    cv2.createTrackbar('Lower_V', 'Color', lower_hsv[2], 255, update_hav)

    vs = cv2.VideoCapture(0)

    while True:
        _, frame = vs.read()

        if frame is None:
            break

        # convert the image to have eisier color extraction.
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow("Frame", frame)
        cv2.imshow("Object", res)
        cv2.imshow('Color', color_sploch)
        key = cv2.waitKey(5) & 0xFF

        # tests if the q key has been pressed
        if key == ord("q"):
            break

    # releases the webcam
    vs.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
