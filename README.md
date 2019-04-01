# image-annotation
It's a handy tool to annotate images which can then be fed to a YOLO model for any kind of a custom object detection training.

How to use:
1.) Create two direcories, called "images" and "annotations". The images folder should have different sub-folders, and each sub-folder should contain images which needed to be annotated.

2.) Run the drawBox.py script through the terminal (python drawBox.py [dirName]) and pass the image folder as an argument.
For example, if you have a subfolder inside images as "images/people", then you can run the script with the command: python drawBox.py people.

3.) Draw the boxes around the object of interest, and press 't' to generate an xml file, and get on to the next frame from the people directory. If you press the 't' again, annotations from the brevious bounding box shall be saved into a new xml file. This is done because there can be cases where there isn't any change in the positin of the object.

If we have accidentally made a wrong annotation, or there is some mistake, then we can just press the “R” key on the keyboard to redraw the box. Otherwise, we need to press the “T” button to have the next frame. When we switch on the next frame, the annotated values of the previous frame are still maintained. This was done because there were videos where there wasn’t any movement for a huge number of frames, so, instead of drawing a box again, we just needed to press the “T” button again to tell the annotator to annotate the new frame with the same bounding boxes. If there is a difference in the next frame, we would again press the “R” key to drop any bounding-box values in the memory, and draw new boxes again. Every time we press the “T” key, a corresponding .xml file to the frame in the annotations directory.
