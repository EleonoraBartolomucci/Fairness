import os

import detect_face as df

# TODO: insert the path_to_my_photo/photo_name.jpg
photos = os.listdir(path_to_my_photo)

for photo in photos:
    df.detect(path_to_my_photo\%s' % photo)

