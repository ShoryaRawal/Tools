import numpy as np 
from os.path import exists
from argparse import ArgumentParser, ArgumentTypeError
import cv2

def application(image):
    img = cv2.imread(image, 0)
    cv2.imshow("Image", img)
    k = cv2.waitKey(0) 
    if k == 27 :
        cv2.destroyAllWindows()

def check(Path):
    if not exists(Path) :
        print("The path does not exist")
    else :
        image = Path
        application(image)

def args():
    args = ArgumentParser()
    args.add_argument("path")
    return args.parse_args()

if __name__ == "__main__":
    arguments = args()
    Path = arguments.path

    check(Path)

