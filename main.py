import cv2 as cv
from mtcnn import MTCNN

vcap = cv.VideoCapture("/home/bishoy/Downloads/emos.mp4")
# vcap.set(cv.CAP_PROP_POS_FRAMES, 100)
frame_count = int(vcap.get(cv.CAP_PROP_FRAME_COUNT))

model = MTCNN()

pos = 0
while True:
    r, frame = vcap.read()
    faces = model.detect_faces(frame)
    vcap.set(cv.CAP_PROP_POS_FRAMES, pos)
    pos += 50
    for i, item in enumerate(faces):
        box = item['box']
        cv.rectangle(frame, (box[0], box[1]),(box[0] + box[2], box[1] + box[3]),
                     (0, 200, 120),
                     2)
        cv.imshow("win", frame)

    if cv.waitKey(25) & 0xFF == ord("q"):
        break

vcap.release()
cv.destroyAllWindows()
