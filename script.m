##Loading the image 
pkg load image;
clear all;
x = imread("Photo.jpg");
#x = imread("Vaibhav Pic.jpg");

x = rgb2gray(x);
imshow(x)
# determining mid point fro reference 
xavg = size(x,1)/2;
yavg =size(x,2)/2;


#for i = xavg-50 : xavg+50
 # for j = yavg-50 : yavg+50
  #  xcrop(i,j) = x(i,j);
    
  #end
#end

#imshow(xcrop)
#size(xcrop)



rshape = resize(x(xavg-64:xavg+64, yavg-64:yavg+64), [128,128]);
size(rshape)
imshow(rshape)
