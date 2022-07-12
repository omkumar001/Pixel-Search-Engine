# Pixel-Search-Engine

## About  

It's a scalable image hashing search engine using OpenCV and VP-Trees . 

#### Image hashing algorithms used over here :
* Uniquely quantifies the contents of an image using only a single integer.
* Find duplicate or near-duplicate images in a dataset of images based on their computed hashes.

To find near-duplicate images, our original image hashing method would require us to perform a linear search, comparing the query hash to each individual image hash in our dataset . Since , in real-world application that is too slow  , so we have used specialized data structure called VP-Trees . Using this , we can reduce our search complexity from O(n) to O(log n), enabling us to obtain our sub-linear searching time .

## Dataset

[CALTECH-101](https://www.tensorflow.org/datasets/catalog/caltech101) is used in this project , which consists of 9,144 total images across 101 categories .

## To Run 

* We need to install the following dependencies ( numpy ,cv2 , imutils and vptree ) using pip .

* After that , we add the location of images in index_images.py. Here , "101_ObjectCategories" refers to the location of images.
``` 
imagePaths = list(paths.list_images("101_ObjectCategories"))
``` 
* Create the pickle files of hashes and VP-tree by running index_images.py.
``` 
$python index_images.py
``` 
* For searching an image , we use 
```
$python search.py --query "image location"
```
