import numpy as np
import argparse
import cv2
import pickle
import time

ap = argparse.ArgumentParser()
ap.add_argument("-q", "--query", required=True, type=str, help="Path to input query image")
ap.add_argument("-d", "--distance", type=int, default=10, help="maximum Hamming distance")
args = vars(ap.parse_args())

def dhash(image, hashSize=8):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (hashSize+1, hashSize))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2**i for (i, v) in enumerate(diff.flatten()) if v])
    
def convert_hash(h):
    return int(np.array(h, dtype="float64"))
    
def hamming(a, b):
    return bin(int(a) ^ int(b)).count("1")
    
print("Loading VP tree and hashes...")
tree = pickle.loads(open("vptree.pickle", "rb").read())
hashes = pickle.loads(open("hashes.pickle", "rb").read())

image = cv2.imread(args["query"])
cv2.imshow("Query", image)
queryHash = dhash(image)
queryHash = convert_hash(queryHash)

print("Performing search...")
start = time.time()
results = tree.get_all_in_range(queryHash, args["distance"])
results = sorted(results)
end = time.time()
print("Search took", end-start, " seconds")

for(d, h) in results:
    resultPaths = hashes.get(h, [])
    print(len(resultPaths), " total image(s) with d:", d, " h:", h)
    for resultPath in resultPaths:
        result = cv2.imread(resultPath)
        cv2.imshow("Result", result)
        cv2.waitKey(0)
