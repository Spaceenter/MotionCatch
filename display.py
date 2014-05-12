import os, glob, time;

img_source = '/home/weisun/Desktop/motion/*.jpg';
last_img = '/home/weisun/Desktop/new.jpg';

# main loop
while True:

  # get and sort the image list
  img_list = glob.glob(img_source);

  n_img = len(img_list);
  if n_img == 0: continue;

  # get the name of the last image
  img_list.sort();
  last_img_source_name = img_list[n_img-1];

  # move the last image to display folder
  os.system('mv ' + last_img_source_name + ' ' + last_img);

  # delete all the images if any left
  if n_img > 1:
    os.system('rm ' + img_source);

  # sleep for 0.05 sec
  time.sleep(0.05);
