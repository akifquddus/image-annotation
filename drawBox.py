import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from generate_xml import write_xml
import sys
from pynput.keyboard import Key, Controller
import natsort

# global constants
img = None
tl_list = []
br_list = []
object_list = []

print(sys.argv[1])
# constants
image_folder = "images/{}".format(sys.argv[1])
savedir = "annotations/{}".format(sys.argv[1])
obj = 'person'

def line_select_callback(clk, rls):
    global tl_list
    global br_list
    global object_list
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    object_list.append(obj)


def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img
    if event.key == 'r':
        tl_list = []
        br_list = []
        object_list = []
        print("Object List cleared")
    # if event.key == 'r':
    #     print(object_list)
    #     write_xml(image_folder, img, object_list, tl_list, br_list, savedir)
    #     tl_list = []
    #     br_list = []
    #     object_list = []
    #     img = None
    #     keyboard = Controller()
    #     keyboard.press('q')
    #     keyboard.release('q')
    if event.key == 't':
        print(object_list)
        write_xml(image_folder, img, object_list, tl_list, br_list, savedir, sys.argv[1])
        img = None
        keyboard = Controller()
        keyboard.press('q')
        keyboard.release('q')


def toggle_selector(event):
    toggle_selector.RS.set_active(True)

image = 1

if __name__ == '__main__':
    dirList = os.listdir(image_folder)
    dirList = natsort.natsorted(dirList,reverse=False)
    #dirList.sort()
    #print(dirList)
    for n, image_file in enumerate(dirList):

        img = image_file
        fig, ax = plt.subplots(1, figsize=(10.5, 8))
        # mngr = plt.get_current_fig_manager()
        # mngr.window.setGeometry(250, 40, 800, 600)
        image = cv2.imread("images/{}/".format(sys.argv[1])+image_file)
        #print("image: {}".format(image))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.title(image_file)
        ax.imshow(image)

        toggle_selector.RS = RectangleSelector(
            ax, line_select_callback,
            drawtype='box', useblit=True,
            button=[1], minspanx=5, minspany=5,
            spancoords='pixels', interactive=True,
        )
        bbox = plt.connect('key_press_event', toggle_selector)
        key = plt.connect('key_press_event', onkeypress)
        plt.tight_layout()
        plt.show()
        plt.close(fig)
