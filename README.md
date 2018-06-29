#Face Detection using python and Dlib/Face_recognition

It contains 3 part 
1. Gettings the data from goodle images
  A file name "ImageDownload.py" will donload the image from google and store it in you local hard drive in Current working directory
  you can use the comand line arguments to specify which player image you want and how much images you want to download
  i.e run this command 
  #### "python ImageDownload.py --peopleList 'Albert Einstein','Nicola Tesla' --limit 5 "
   : -- peopleList argument expects list of peoples' images. you can specify single iamge or multiple seperated by comma.
   
   : -- limit argument specifies how many images to download. here it will downlload 5 images for each person (i.e. Albert Einstein and Nicola Tesla)

The Data gets stored in the Folder structure format as follows :
Parent Direcotry : 
FacesDB : 

---- Albert Einstein-- 5 images 

---- Nicola Tesla -- 5 images
   
all the images of people will be stored under FacesDB folder
