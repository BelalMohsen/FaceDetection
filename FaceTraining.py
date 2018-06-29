# =============================================================================
# Face Detection using Face Alignment wrap affine method
# =============================================================================

import numpy as np, os,time 
import cv2
import dlib
#import openface
import face_recognition
import pickle
from sklearn.svm import SVC

path = os.path.dirname(os.path.abspath("__file__")) + '/'

# =============================================================================
# predictor_path = path + 'shape_predictor_68_face_landmarks.dat'
# 
# faceDetector = dlib.get_frontal_face_detector()
# pose_Predictor = dlib.shape_predictor(predictor_path)
# 
# 
# face_aligner = openface.AlignDlib(predictor_path)
# 
# image = cv2.imread(path + 'Images/8.jpg')
# faces = faceDetector(image,1)
# 
# for rect in faces:
#     
#     pose = pose_Predictor(image,rect)
#     
#     alignFace = face_aligner.align(300,image,rect, landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
#     
#     cv2.imwrite(path + 'Images/Aligned.jpg', alignFace)
# 
# face_loc = face_recognition.face_locations(image) # returns top right bottom Left coordinate of faces 
# 
# MNFace_embedings = face_recognition.face_encodings(image,face_loc)[0]
# 
# knownFaces = [MNFace_embedings]
# 
# 
# 
# 
# 
# img = cv2.imread(path + 'Images/2.jpg')
# faces = faceDetector(img,1)
# 
# face_loc1 = face_recognition.face_locations(img)
# MNFace_embedings1 = face_recognition.face_encodings(img,face_loc1)[0]
# 
# face_recognition.compare_faces(knownFaces,MNFace_embedings1)
# 
# 
# 
# 
# 
# =============================================================================
# Apporach 1 using using face Comparision
# =============================================================================
# 
# imageDir = path + 'FacesDB/'
# knownFaces = {}
# folders = os.listdir(imageDir)
# folders = [item for item in folders if item != '.DS_Store']
# 
# for folder in folders:
#     #knownFaces.append(folder)
#     image = [item for item in os.listdir(imageDir + folder +'/') if item != '.DS_Store'][0]
#     
#     image = cv2.imread(imageDir + folder +'/' + image)
#     #getting the face location
#     faceLcoation = face_recognition.face_locations(image)
#     
#     #now getting faceEncodings
#     faceEncodings = face_recognition.face_encodings(image,faceLcoation)[0]    
#     knownFaces[str(folder)] = faceEncodings
#     
#     print('done with ', folder)
#     
# 
# =============================================================================

# =============================================================================
# Apporach 2 using SVM classifier to train the model
# =============================================================================

imageDir = path + 'FacesDB/'
knownFaces = []
knownEncodings =[]
folders = os.listdir(imageDir)
folders = [item for item in folders if item != '.DS_Store']
count=0
for folder in folders:
    #knownFaces.append(folder)
    images = [item for item in os.listdir(imageDir + folder +'/') if item != '.DS_Store']
    
    print('Starting {} which has {} faces'.format(folder,len(images)))
    
    for img in images:   
        image = cv2.imread(imageDir + folder +'/' + img)
        try:    
        #getting the face location
            faceLcoation = face_recognition.face_locations(image)
            #now getting faceEncodings
            faceEncodings = face_recognition.face_encodings(image,faceLcoation)[0]    
            #knownFaces[str(folder)] = faceEncodings
        except:
            #print('count:' , count)
            count+=1
            continue
        knownFaces.append(folder)
        knownEncodings.append(faceEncodings)
    
    print('done with {} and number for faces not found {} out of total {} facesData '.format(folder, count, len(images)))
    


#Training the SVM
print("Training Started...")
svm = SVC(C=100.0,kernel='linear',gamma=0.001,probability=True,verbose=2)

svm.fit(knownEncodings,knownFaces)

# =============================================================================
# Storing the Encodings Data
# =============================================================================

with open(path+ 'Encoding_Data/' + 'FaceEncodings.pkl','wb') as f:
                pickle.dump(knownFaces, f,  protocol=2)

# =============================================================================
# Storing the model.
# =============================================================================


with open(path+ 'Encoding_Data/' + 'FaceEncodingsModel.pkl','wb') as f:
                pickle.dump(svm, f,  protocol=2)


print("Training Finished...! Model can be found at {} location ".format(path+ 'Encoding_Data/'))






# =============================================================================
# Lets test it
# =============================================================================
# =============================================================================
# temp = list(knownFaces.values())
# person = list(knownFaces.keys())
#     
# img = cv2.imread('Images/6.jpg')    
# fLoc = face_recognition.face_locations(img)    
# fEmbeddings = face_recognition.face_encodings(img,fLoc)[0]
# 
# result = face_recognition.compare_faces(list(knownFaces.values()), fEmbeddings,tolerance=0.5)
# 
# 
# person[int(np.argmax(result))]
# =============================================================================








    