# Face Detection using python and Dlib/Face_recognition

It contains 3 part 
## 1. Gettings the data/Images from google image search
  A file name "**ImageDownload.py**" will donload the image from google and store it in you local hard drive in Current working directory
  you can use the comand line arguments to specify which player image you want and how much images you want to download
  i.e run this command 
  ### "python ImageDownload.py --peopleList 'Albert Einstein','Nicola Tesla' --limit 5 "
   : -- peopleList argument expects list of peoples' images. you can specify single iamge or multiple seperated by comma.
   
   : -- limit argument specifies how many images to download. here it will downlload 5 images for each person (i.e. Albert Einstein and Nicola Tesla)

The Data gets stored in the Folder structure format as follows :
Parent Direcotry : 
FacesDB : 

---- Albert Einstein-- 5 images 

---- Nicola Tesla -- 5 images
   
all the images of people will be stored under FacesDB folder
* the next operation performed on the images is to crop the specific face area and replace the originial image. The command will take care of that thing as well. so finally you have al lthe face data created on your hard drive in working directory.


### Note: If you are tying to get more than 100 images then you need have **chrome driver** and you need to update the file at for chrome driver path( I have added mine ) you will have to change that. Just google it for chrome driver you will get it.

## 2. Training the Data

* Once the Data is availbale. You can simply run the belwo command which will start the training. Training mainly involved in identifying **68 facial Key points**, affining them to suitable shape and then extracting the **face embeddings (128 facial features)**.
* After getting the features the data is then fed to **SVM model for training.** 

* I have used the face_recognition api to do this stuff.

* After training is over the model gets saved into your local drive at the **Encoding_Data/** folder.

