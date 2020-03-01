import matplotlib.pyplot as plt
import numpy as np
import cv2


def read_img(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def show_img(img):
    plt.imshow(img)
    plt.show()


def invert(img):
    return 255 - img


def get_correlation(img, pattern, threshold=0.9):
    x = np.fft.fft2(img)
    y = np.fft.fft2(np.rot90(pattern, 2), x.shape)
    res = np.multiply(x, y)
    correlation = np.abs(np.fft.ifft2(res))
    plt.imshow(correlation)
    plt.show()
    correlation[correlation < threshold * np.amax(correlation)] = 0
    correlation[correlation != 0] = 155     # dla lawicy 255
    return correlation


def get_letter_positions(corr, pattern):
    width, height = pattern.shape
    x, y = (-1 * width, -1 * height)
    positions = []
    for (i, j), v in np.ndenumerate(corr):
        if v > 0.0 and not (x + width > i and y + height > j):
            positions.append((i, j))
            x, y = i, j
    return positions


def mark_positions(img, pattern, positions):
    for x, y in positions:
        width, height = pattern.shape
        for i in range(x-width, x):
            for j in range(y-height, y):
                if img[i, j] > 0:
                    img[i, j] = 255
    return img


if __name__ == '__main__':
    galia = invert(read_img('galia.png'))
    galia_e = invert(read_img('galia_e.png'))
    cor = get_correlation(galia, galia_e)
    show_img(cor)
    pos = get_letter_positions(cor, galia_e)
    print(len(pos))
    result = mark_positions(galia, galia_e, pos)
    show_img(result)
    #
    # img = read_img('school.jpg')
    # fish = read_img('fish_pattern.png')
    # cor = get_correlation(img, fish, 0.80)
    # show_img(cor)
    # pos = get_letter_positions(cor, fish)
    # result = mark_positions(img, fish, pos)
    # show_img(result)
