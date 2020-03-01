import matplotlib.pyplot as plt
import numpy as np
import string
import cv2


class OCR():
    def __init__(self, img_path, font_type="sans"):
        self.image = self.load_image(img_path)
        self.letterImages = self.load_letter_images(font_type)
        self.lettersPosition = {}
        self.searchOrder = ['t', 'a', 'b', 'd', 'x', 'f', 'p', 'h', 'w',
                            'j', 'k', 'v', 'm', 'g', 'y', 'n', 'q', 'r',
                            'z', 's', 'u', 'l', 'i', 'e', 'o', 'c']

    def load_image(self, path):
        img = cv2.imread(path)
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def load_letter_images(self, font_type):
        letters = {}
        if font_type == 'sans':
            path = 'data/sans-font/'
        else:
            path = 'data/serif-font/'
        for l in string.ascii_lowercase:
            letters[l] = 255 - self.load_image(path + l + '.PNG')
        for i in range(10):
            letters[i] = 255 - self.load_image(path + str(i) + '.PNG')
        return letters

    def show_img(self):
        plt.imshow(self.image)
        plt.show()

    def single_letter_correlation(self, letter, threshold=0.80):
        x = np.fft.fft2(255 - self.image)
        y = np.fft.fft2(np.rot90(letter, 2), x.shape)
        res = np.multiply(x, y)
        correlation = np.abs(np.fft.ifft2(res)).astype(float)
        correlation[correlation < threshold * np.amax(correlation)] = 0
        correlation[correlation != 0] = 254
        return correlation

    def get_single_letter_positions(self, letter, correlation):
        width, height = letter.shape
        x, y = (-1*width, -1*height)
        positions = []
        for (i, j), v in np.ndenumerate(correlation):
            if v > 0.0 and not (x + width > i and y + height > j):
                positions.append((i, j))
                x, y = i, j
        return positions

    def find_single_letter(self, letter, threshold=0.9):
        patternImage = self.letterImages[letter]
        cor = self.single_letter_correlation(patternImage, threshold)
        self.lettersPosition[letter] = self.get_single_letter_positions(patternImage, cor)
        for x, y in self.lettersPosition[letter]:
            width, height = patternImage.shape
            self.image[x-width:x, y-height:y] = 255

    def convert_to_text(self):
        positions = []
        for key, value in self.lettersPosition.items():
            for val in value:
                positions.append((key, val[0] - 10 - (val[0]-10) % 100, val[1]))
        positions = sorted(positions, key=lambda e: (e[1], e[2]))
        text = ""
        for i in range(len(positions) - 1):
            text += str(positions[i][0])
            space = (self.letterImages[positions[i][0]].shape[1] + self.letterImages[positions[i+1][0]].shape[1])/2
            if abs(positions[i][2] - positions[i+1][2]) - 12 > space:
                text += ' '
            if abs(positions[i][1] - positions[i+1][1]) >= 100:
                text += '\n'
        text += str(positions[len(positions)-1][0])
        self.result = text
        return text

    def show_amount_of_each_letter(self):
        for l in string.ascii_lowercase:
            print(l, len(self.lettersPosition[l]))
        for i in range(10):
            print(i, len(self.lettersPosition[i]))

    def proceed(self):
        self.rotate_img()
        for i in range(10):
            self.find_single_letter(i, 0.98)
        for l in self.searchOrder:
            self.find_single_letter(l, 0.94)
        result = self.convert_to_text()
        print(result)
        self.show_amount_of_each_letter()

    def rotate_img(self):
        img = cv2.bitwise_not(self.image)
        thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        coords = np.column_stack(np.where(thresh > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90+angle)
        else:
            angle = - angle
        (h, w) = self.image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(self.image, M, (w, h),
                                 flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        self.image = rotated


if __name__ == '__main__':
    # sans font
    ocr = OCR("data/sans-font/test_file.PNG")
    ocr.show_img()
    ocr.proceed()
    ocr.show_img()

    # testing rotation
    # ocr = OCR('data/sans-font/test_rotated.PNG')
    # ocr.show_img()
    # ocr.rotate_img()
    # ocr.show_img()

    # serif font
    # ocr = OCR('data/serif-font/test_digits.PNG', 'serif')
    # ocr.proceed()
    # ocr.show_img()
