# Pixel-Search-Engine
Image Hashing Search Engine with VP-Trees and OpenCV

It's a scalable image hashing search engine using OpenCV and VP-Trees.


Image hashing algorithms used over here :

 Uniquely quantifies the contents of an image using only a single integer.
 Find duplicate or near-duplicate images in a dataset of images based on their computed hashes.


To find near-duplicate images, our original image hashing method would require us to perform a linear search, comparing the query hash to each individual image hash in our dataset.

Since , in real-world application that is too slow  , so we have used specialized data structure called VP-Trees . Using this , we can reduce our search complexity from O(n) to O(log n), enabling us to obtain our sub-linear searching time !!
