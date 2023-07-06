# dataset:https://www.kaggle.com/datasets/nomaanahmeddd/color-codes
import cv2
import pandas as pd

img_path = r'living room.jpg'
img = cv2.imread(img_path)

clicked = False
r = g = b = x_pos = y_pos = 0

index = ["Name", "Hex", "R", "G", "B"]
data = pd.read_csv('color_names.csv', names=index, header=None,skiprows=1)


def color_name(R, G, B):
    minimum = 10000
    for i in range(len(data)):
        d = abs(R - int(data.loc[i, "R"])) + abs(G - int(data.loc[i, "G"])) + abs(B - int(data.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = data.loc[i, "Name"]
    return cname


def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:

    cv2.imshow("image", img)
    if clicked:

        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        text = color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
