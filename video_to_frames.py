#!/usr/bin/env python

"""
There was a video from which i wanted to extract all frames, many examples using OpenCV can be found for this online.
The problem is that there was an invalid/corrupt frame in my video.
This made the program crash when the invalid frame was encountered.
I rewrote the code to keep going unless 5 invalid frames are encountered (i.e. end of the stream).
"""

import cv2
import os

__author__ = "Willem Boone"
__email__ = "willem.boone@outlook.com"


def frame_capture(path):
    """
    function that reads a video and writes the frames to image files
    :param path: String to file location
    :return:
    """
    # make a directory to store the frames as images
    dir_path = os.path.dirname(path) + "/frames/"
    os.mkdir(dir_path)

    # Path to video file
    cap = cv2.VideoCapture(path)

    # counter variables
    count = 0
    fails = 0

    # loop over the frames
    while cap.isOpened():
        print(count)

        success, image = cap.read()
        # the issue starts here if there is no success
        # success == False might indicate that the video has no more frame and thus the end of the video is reached
        # OR there might be a corrupt frame in the video (which was the case in my video)
        # in that case we do not want to program to end yet, just this particular invalid frame needs to be skipped

        # if there is a frame: write to image
        if success:
            fails = 0
            cv2.imwrite(dir_path + "frame" + str(count) + ".jpg", image)

        # if there is no valid frame: decide whether it is a single invalid frame
        # or if we reached the end of the video
        else:
            print("could not read frame")
            fails += 1

            # if there have been 5 invalid frames in a row
            # we consider the video to be over
            if fails > 5:
                print("end of the video")
                break

        count += 1


if __name__ == '__main__':
    path = "D:/downloads/RAZ2020/GH019901_1597591005927.mp4"
    frame_capture(path)