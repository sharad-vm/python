import cv2 as cv

#read a local image
original_image = cv.imread('./original-images/josh-hild-1313363-unsplash.jpg')

#convert color image to grey scale
grayscale_image = cv.cvtColor(original_image, cv.COLOR_BGR2GRAY)

#load the classifier and create a cascade object for face detection
face_cascade = cv.CascadeClassifier('/Users/shara/AppData/Local/Programs/Python/Python37/Lib/site-packages/cv2/data/haarcascade_frontalface_alt.xml')

detected_faces = face_cascade.detectMultiScale(grayscale_image)

for (column, row, width, height) in detected_faces:
    cv.rectangle(
        original_image,
        (column, row),
        (column + width, row + height),
        (139, 0, 139),
        3
    )

cv.imwrite('./detected-images/josh-hild-1313363.jpg',original_image)
#cv.waitKey(0)
#cv.destroyAllWindows()
