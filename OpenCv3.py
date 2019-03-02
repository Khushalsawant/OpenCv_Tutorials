'''
Basic operations on images
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html#basic-ops
'''

import cv2
import numpy as np

print("cv2.__version__" , cv2.__version__)

e1 = cv2.getTickCount()  #returns the number of clock-cycles after a reference event

Path_of_img = 'C:/Users/khushal/Pictures/khushal.jpg'
# Load an color image in grayscale
img = cv2.imread(Path_of_img,255)

# to display an image in a window
'''
By default, the flag is cv2.WINDOW_AUTOSIZE. But if you specify flag to be cv2.WINDOW_NORMAL, you can resize window.
'''

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#To display pixel vaules = returns an array of Blue, Green, Red values.
# For grayscale image, just corresponding intensity is returned.

px = img[100,100]
print('pixel vaules = ', px) # O/P is B-G-R format

#accessing only blue pixel

px_blue = img[100,100,0]
print('pixel value of blue = ', px_blue) # O/P is B-G-R format

#Better pixel accessing and editing method :

# accessing RED value :
px_red = img.item(100,100,2)
print('pixel value of red = ', px_red)  


# modifying RED value
img.itemset((10,10,2),100)
px_red1 = img.item(10,10,2)
print('pixel value of Modified red = ', px_red1)

'''
Accessing Image Properties
Image properties include number of rows, columns and channels, type of image data, number of pixels etc.
'''

#Shape of image = returns a tuple of number of rows, columns and channels (if image is color)
#For Grayscale, tuple returned contains only number of rows and columns.
#So it is a good method to check if loaded image is grayscale or color image.
img_shape = img.shape
print('Image Shape = ', img_shape)

#Total number of pixels
img_size = img.size
print('Image Size = ', img_size)

#data-type of image
img_dtype = img.dtype
print('Image data-type = ', img_dtype)

'''
Image ROI
'''

ball = img[200:340, 300:390]
img[273:413, 100:190] = ball
cv2.imshow('image',ball)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Splitting and Merging Image Channels
'''
b,g,r = cv2.split(img) # b = img[:,:,0] , g = img[:,:,1], r = img[:,:,2]
img = cv2.merge((b,g,r))

'''
Making Borders for Images (Padding)

cv2.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next argument.
cv2.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT - Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba
cv2.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
cv2.BORDER_WRAP - Can’t explain, it will look like this : cdefgh|abcdefgh|abcdefg

'''
BLUE = [255,0,0]

Path_of_img = 'C:/Users/khushal/Pictures/khushal.jpg'
# Load an color image in grayscale
img1 = cv2.imread(Path_of_img,255)

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)

cv2.imshow('replicate',replicate)
cv2.waitKey(0)
cv2.destroyAllWindows()

reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)

cv2.imshow('reflect',reflect)
cv2.waitKey(0)
cv2.destroyAllWindows()

reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)

cv2.imshow('reflect101',reflect101)
cv2.waitKey(0)
cv2.destroyAllWindows()

wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)

cv2.imshow('wrap',wrap)
cv2.waitKey(0)
cv2.destroyAllWindows()

constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

cv2.imshow('constant',constant)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Arithmetic Operations on Images
'''

x = np.uint8([250])
y = np.uint8([10])

print('cv2 addition = ', cv2.add(x,y)) # 250+10 = 260 => 255
print('numpy addition = ',x+y) # 250+10 = 260 % 256 = 4

# Addition of images
res = img + img1
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Image Blending

dst = x.img1 + y.img2 + z

'''
Path_of_img = 'C:/Users/khushal/Pictures/khushal.jpg'
# Load an color image in grayscale
img2 = cv2.imread(Path_of_img,255)

dst = cv2.addWeighted(img1,0.2,img2,0.3,0) ## dst = x.img1 + y.img2 + z

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
bitwise operations
'''

Path_of_img = 'C:/Users/khushal/Pictures/khushal.jpg'
# Load an color image in grayscale
img2 = cv2.imread(Path_of_img,255)

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('bitwise',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Default Optimization in OpenCV
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_optimization/py_optimization.html
'''

cv2.useOptimized() # check if optimization is enabled
print(cv2.useOptimized())
res1 = cv2.medianBlur(img,49)
# optimization is disabled
cv2.setUseOptimized(False)
cv2.useOptimized()
print(cv2.useOptimized())
res1 = cv2.medianBlur(img,49)

cv2.imshow('res1',res1)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
Measuring Performance with OpenCV
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_optimization/py_optimization.html
'''
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print("Time taken for execution ", time)

z = np.count_nonzero(img)
e3 = cv2.getTickCount()
print((e3 - e2)/ cv2.getTickFrequency())