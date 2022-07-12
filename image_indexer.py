import numpy as np
import cv2
import pickle
from imutils import paths
import vptree


def dhash(image, hashSize=8):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (hashSize+1, hashSize))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2**i for (i, v) in enumerate(diff.flatten()) if v])
    
def convert_hash(h):
    return int(np.array(h, dtype="float64"))
    
def hamming(a, b):
    return bin(int(a) ^ int(b)).count("1")
    
imagePaths = list(paths.list_images("101_ObjectCategories"))
hashes = {}

for (i, imagePath) in enumerate(imagePaths):
    print("Processing image ", i+1, "/", len(imagePaths))
    image = cv2.imread(imagePath)
    h = dhash(image)
    h = convert_hash(h)
    l = hashes.get(h, [])
    l.append(imagePath)
    hashes[h] = l
    
print("Building VP tree...")
points = list(hashes.keys())
tree = vptree.VPTree(points, hamming)

print("Serializing VP tree...")
f = open("vptree.pickle", "wb")
f.write(pickle.dumps(tree))
f.close()

print("Serializing hashes...")
f = open("hashes.pickle", "wb")
f.write(pickle.dumps(hashes))
f.close()
