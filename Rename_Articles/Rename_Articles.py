import glob
import os
book_filename = sorted(glob.glob("C:/Users/vct_3/Desktop/Köşe Yazıları/Ali Sirmen/*.txt"))

ct = 0

for filename in book_filename:
    os.rename(filename, "C:/Users/vct_3/Desktop/Köşe Yazıları/Ali Sirmen/mak%s-alisirmen.txt" %ct)
    ct += 1