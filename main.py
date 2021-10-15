# cv2(OpenCV)を利用する宣言を行う。
import cv2
import sys

# imread : 画像ファイルを読み込んで、多次元配列(numpy.ndarray)にする。
# imreadについて : https://kuroro.blog/python/wqh9VIEmRXS4ZAA7C4wd/
# 第一引数 : 画像のファイルパス
# 第二引数 : 画像の形式を指定。0を指定する場合、画像をグレースケールで読み込む。
# 戻り値 : 多次元配列(numpy.ndarray)が返される。
img = cv2.imread('./sample.jpg', 0)

# 画像ファイルが正常に読み込めなかった場合、プログラムを終了する。
if img is None:
    sys.exit("Could not read the image.")

# threshold関数 : しきい値を用いて画素の色を示す値を2値化(0 or N)するための関数。

# 第一引数 : 多次元配列(画像情報)
# 第二引数 : しきい値。float型。127とする。

# 第三引数 : しきい値を超えた画素に対して、色を示す値を指定。 2値化(0 or N)のNの部分に相当する。float型。255とする。

# 第四引数 : 2値化(0 or N)するための条件のタイプを指定する。
# cv2.THRESH_BINARY : (画素の色を示す値 <= 第二引数)の場合、画素に対して、0の値を与える。(画素の色を示す値 > 第二引数)の場合、画素に対して、第三引数の値を与える。

# 戻り値 #################
# ret : しきい値を返す。127を返す。
# thresh : 多次元配列(numpy.ndarray)を返す。
#########################
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# imwrite : 画像の保存を行う関数
# 第一引数 : 保存先の画像ファイル名
# 第二引数 : 多次元配列(numpy.ndarray)
# <第二引数の例>
# [
# [
# [234 237 228]
# ...
# [202 209 194]
# ]
# [
# [10 27 16]
# ...
# [36 67 46]
# ]
# [
# [34 51 40]
# ...
# [50 81 60]
# ]
# ]
# imwriteについて : https://kuroro.blog/python/i0tNE1Mp8aEz8Z7n6Ggg/
cv2.imwrite('./output.png', thresh)
