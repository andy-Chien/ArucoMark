import pyrealsense2 as rs
import numpy as np
import cv2

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 1920, 1080, rs.format.bgr8, 30)

pipeline.start(config)

#cap = cv2.VideoCapture(4)
frameId = 0
while(True):

    frames = pipeline.wait_for_frames()
    color_frame = frames.get_color_frame()
    if not color_frame:
        continue

    color_image = np.asanyarray(color_frame.get_data())


    
    # Capture frame-by-frame
    # ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',color_image)

    if cv2.waitKey(1) & 0xFF == ord('t'):
        filename = "./pic_1920_1080_big/camera-pic-of-charucoboard-" +  str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, color_image)
        frameId += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
# cap.release()
cv2.destroyAllWindows()
# cv2.waitKey(1) & 
