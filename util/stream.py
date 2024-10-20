import cv2 as cv
import numpy as np

class Stream:
    def __init__(self, source = 0, width = 640, height = 480, exposure = None):
        self.source = source
        self.height = height
        self.width = width
        self.exposure = exposure
        self.camera = None

    def get_dimensions(self):
        return (self.length, self.width)

    def get_source(self):
        return self.source
    
    def get_exposure(self):
        return self.exposure
    
    def print_attributes(self):
        print(f"Camera source {self.source} attributes:")
        print(f"Frame height: {self.height}")
        print(f"Frame width: {self.width}")
        print(f"Frame exposure {self.exposure}") if self.exposure else print("Using auto frame exposure")

    def start_capture(self):
        self.camera = cv.VideoCapture(self.source, cv.CAP_DSHOW)
        self.camera.set(cv.CAP_PROP_FRAME_WIDTH, self.width)
        self.camera.set(cv.CAP_PROP_FRAME_HEIGHT, self.height)
        if self.exposure:
            self.camera.set(cv.CAP_PROP_EXPOSURE, self.exposure)

        # Error handling if camera is not opened
        if not self.camera.isOpened():
            print(f"Error: Cannot open camera at source: {self.source}")
            return

        while True:
            ret, frame = self.camera.read()
            if not ret:
                print("Error: Failed to capture frame")
                break

            cv.imshow(f"Camera Source: {self.source}", frame)

            # Wait 1 ms for esc key press to exit
            if cv.waitKey(1) == 27:
                break

        # Frees the camera and closes OpenCV windows
        self.camera.release()
        cv.destroyAllWindows()

if __name__ == "__main__":
    camera = Stream()
    camera.print_attributes()
    camera.start_capture()
