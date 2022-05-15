import cv2

class DrawLineWidget(object):
    def __init__(self):
        self.original_image = cv2.imread(r'.\\3.2_mapping&mosaic\\map.png')
        self.clone = self.original_image.copy()

        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.extract_coordinates)

        # List to store start/end points
        self.image_coordinates = []

    def extract_coordinates(self, event, x, y, flags, parameters):
        # Record starting (x,y) coordinates on left mouse button click
        if event == cv2.EVENT_LBUTTONDOWN:
            self.image_coordinates = [(x,y)]

        # Record ending (x,y) coordintes on left mouse bottom release
        elif event == cv2.EVENT_LBUTTONUP:
            self.image_coordinates.append((x,y))
            print('Starting: {}, Ending: {}'.format(self.image_coordinates[0], self.image_coordinates[1]))

            # Draw line
            cv2.line(self.clone, self.image_coordinates[0], self.image_coordinates[1], (42, 42, 165), 2)
            cv2.imshow("image", self.clone) 

        # Clear drawing boxes on right mouse button click
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.clone = self.original_imag.copy()

    def show_image(self):
        return self.clone

if __name__ == '__main__':
    draw_line_widgetk = DrawLineWidget()
    while True:
        cv2.imshow('image', draw_line_widgetk.show_image())
        key = cv2.waitKey(10)

        # Close program with keyboard 'x'
        if key%256 == 27:
            cv2.destroyAllWindows()
            exit(1)
