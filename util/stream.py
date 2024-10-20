import cv2 as cv
import numpy as np

class Stream:
    def __init__(self, source=0, length = 640, width = 480):
        self.source = source
        self.length = length
        self.width = width
        self.camera = None

    def get_dimensions(self):
        return (self.length, self.width)

    def get_source(self):
        return self.source

    def start_capture(self):
        self.camera = cv.VideoCapture(self.source, cv.CAP_DSHOW)
        self.camera.set(cv.CAP_PROP_FRAME_WIDTH, self.length)
        self.camera.set(cv.CAP_PROP_FRAME_HEIGHT, self.width)

        # Error handling if camera is not opened
        if not self.camera.isOpened():
            print(f"Error: Cannot open camera at source: {self.source}")
            return

        while True:
            ret, frame = self.camera.read()
            if not ret:
                print("Error: Failed to capture frame")
                break

            cv.imshow(f"camera {self.source}", frame)

            # Wait 1 ms for esc key press to exit
            if cv.waitKey(1) == 27:
                break

        # Frees the camera and closes OpenCV windows
        self.camera.release()
        cv.destroyAllWindows()

if __name__ == "__main__":
    camera = Stream()
    camera.start_capture()
