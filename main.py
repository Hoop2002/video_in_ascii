import cv2
import os
import time
import shutil

def frame_to_ascii(frame, cols=80):
    height, width = frame.shape[:2]
    aspect_ratio = height / float(width)
    new_width = cols
    new_height = int(aspect_ratio * new_width * 0.55)
    resized_frame = cv2.resize(frame, (new_width, new_height))

    gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    ascii_chars = "@%#*+=-:. "
    ascii_frame = ""

    for row in gray_frame:
        for pixel in row:
            index = pixel // 25
            if index >= len(ascii_chars):
                index = len(ascii_chars) - 1
            ascii_frame += ascii_chars[index]
        ascii_frame += "\n"

    return ascii_frame

def center_text(text, width):
    lines = text.split('\n')
    centered_lines = []
    for line in lines:
        centered_line = line.center(width)
        centered_lines.append(centered_line)
    return '\n'.join(centered_lines)

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    console_width = shutil.get_terminal_size().columns

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        ascii_frame = frame_to_ascii(frame)
        print(center_text(ascii_frame, console_width))
        cv2.waitKey(300000)
        time.sleep(0.02)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    video_path = input("MP4 file path: ")
    main(video_path)