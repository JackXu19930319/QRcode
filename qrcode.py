# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 2019
@author: Shayne
"""

import numpy as np
import pyzbar.pyzbar as zbar
import cv2
import numpy as np
import pyzbar.pyzbar as zbar
import matplotlib.pyplot as plt
import time

def detect(I): 
    # 偵測所有的 QR code
    barcodes = zbar.decode(I)
    
    # 逐一解碼，回傳位置與結果
    bbox = []; msg = [];
    for i, barcode in enumerate(barcodes):
        bbox.append(np.array(barcode.rect))
        msg.append(barcode.data.decode('utf-8'))
    return bbox, msg


cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    # frame = img.copy()
    cv2.imshow("capture", frame) 
    # cv2.imwrite("test.png", frame)
    # I = cv2.imread('test.png')
    bbox, msg = detect(frame)
    print(msg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.1)
cam.release()
cv2.destroyAllWindows()