import os
import sys
import PIL.Image
import PIL.ExifTags
import datetime
import exifread

if len(sys.argv) != 2:
    sys.exit()
else:
    src = sys.argv[-1]


total = 0
total_with_same_time = 0
for src_name in os.listdir(src):
    ext = os.path.splitext(src_name)[-1]
    f = open(os.path.join(src, src_name), 'rb')
    tags = exifread.process_file(f)
    #print(sorted(tags.keys()))
    try:
        date_time_original = PIL.Image.open(os.path.join(src, src_name))._getexif()[36867]
    except (OSError, AttributeError, TypeError):
        continue
    try:
        date_time_converted = datetime.datetime.strptime(
            date_time_original, '%Y:%m:%d %H:%M:%S').strftime('%Y-%m-%d_%H%M%S')
    except ValueError:
        continue
    dst_name = date_time_converted + ext
    print(dst_name)
    if src_name == dst_name:
        continue
    idx = 1
    while os.path.exists(os.path.join(src, dst_name)):
        dst_name = date_time_converted + '_' + str(idx) + ext
        idx += 1
        total_with_same_time += 1
    os.rename(
        os.path.join(src, src_name),
        os.path.join(src, dst_name)
    )
    total += 1

print('Total renamed: ', total)
print('Total with the same time: ', total_with_same_time)
