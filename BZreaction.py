import time

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
                if 0 < tmp <= 2:
                    self.seat[i, j] = tmp


    def reflection(self):
        reflected = self.seat.copy()
        for i in range(self.size):
            for j in range(self.size):
                if self.seat[i, j] == 0:
                    if np.any(self.seat[i-1:i+2, j]==1) or np.any(self.seat[i, j-1:j+2]==1):
                    #if np.any(self.seat[i-1:i+2, j-1:j+2]==1):
                        reflected[i, j] = 1
                        continue
                if self.seat[i, j] == 1:
                    reflected[i, j] = 2
                    continue
                if self.seat[i, j] == 2:
                    reflected[i, j] = 0
        self.seat = reflected


def main():
    size = 128
    rate = 60

    seat = Seat(size, rate)

    seat.expression()
    while(True):
        seat.reflection()
        tmp = seat.seat.copy()
        tmp = cv2.resize(tmp, (512, 512))
        tmp[tmp!=1] = 0
        cv2.imshow(f"BZ-Reaction rate={rate}", tmp)
        wkey = cv2.waitKey(1) & 0xFF
        if wkey == ord('q'):
            break
        elif wkey == ord('r'):
            seat = Seat(size, rate)
            seat.expression()
        #time.sleep(0.3)

if __name__ == '__main__':
    main()
