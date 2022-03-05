import numpy as np
import cv2


class Seat:
    def __init__(self, size, rate):
        self.size = size
        self.rate = rate
        self.seat = np.zeros((size, size))

    def expression(self):
        for i in range(self.size):
            for j in range(self.size):
                tmp = np.random.randint(0, self.rate)
                if 0 < tmp <= 1:
                    self.seat[i, j] = tmp

    def reflection(self):
        reflected = self.seat.copy()
        for i in range(self.size):
            for j in range(self.size):
                density = int(np.sum(self.seat[i-1:i+2, j-1:j+2]) - self.seat[i, j])
                if self.seat[i, j] == 1:
                    if 2 <= density <= 3:
                        reflected[i, j] = 1
                    if (density <= 1) or (density >= 4):
                        reflected[i, j] = 0
                elif self.seat[i, j] == 0:
                    if density == 3:
                        reflected[i, j] = 1
        self.seat = reflected


def main():
    size = 128
    rate = 10

    seat = Seat(size, rate)

    seat.expression()
    while(True):
        seat.reflection()
        tmp = seat.seat.copy()
        tmp = cv2.resize(tmp, (512, 512))
        tmp[tmp >= 0.3] = 1
        tmp[tmp < 0.3] = 0
        cv2.imshow("Life Game", tmp)
        wkey = cv2.waitKey(1) & 0xFF
        if wkey == ord('q'):
            break
        elif wkey == ord('e'):
            seat.expression()
        elif wkey == ord('r'):
            seat = Seat(size, rate)
            seat.expression()


if __name__ == '__main__':
    main()
