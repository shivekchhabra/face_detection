import cv2


# Setting your cascade file
def setting_cascade(filename):
    human_cascade = cv2.CascadeClassifier(filename)
    return human_cascade


# Face detection using Haar Cascade
def detection(filename):
    cap = cv2.VideoCapture(0)
    human_cascade = setting_cascade(filename)
    while 1:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        word2 = "human"
        human = human_cascade.detectMultiScale(gray, 1.3, 5)
        for (wx, wy, ww, wh) in human:
            cv2.rectangle(img, (wx, wy), (wx + ww, wy + wh), (255, 0, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, word2, (wx + ww, wy + wh), font, 1, (255, 255, 0), 2, cv2.LINE_AA)
            print("human detected")
        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    file = 'human.xml'  # Path to file
    detection(file)
