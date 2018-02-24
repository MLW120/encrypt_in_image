import cv2

def string_to_ascii(s):
	ret = []
	for letter in s:
		ret.append(ord(letter))
	#ret.append(3)
	return ret

def image_to_array(im):
	ret = []
	for layer in im:
		for pixel in layer:
			ret.append(pixel[0]); ret.append(pixel[1]); ret.append(pixel[2])
	return ret
	
def array_to_image(array,original_image):
	count = 0	
	for layer in original_image:
		for pixel in layer:
			for i in range(3):
				pixel[i] = array[count]
				count += 1
	return original_image
	
def insert_string_into_array(ascii,array):
	array_of_binary_pairs = []
	for ch in message_ascii:
		for i in range(4):
			array_of_binary_pairs.append((ch & (3 * 4 ** i)) >> (2 * i))
	print(array_of_binary_pairs)
	for i in range(len(array)):
		array[i] -= (array[i] % 4)
	for i in range(len(array_of_binary_pairs)):
		if i >= len(array):
			print('Image is too small for the message')
			break
		array[i] += array_of_binary_pairs[i]
	return array
	
im = cv2.imread('Image.jpg')

message = input('Which is the message? ')
message_ascii = string_to_ascii(message)
image = image_to_array(im)
print('CONVERTED')
new_image = insert_string_into_array(message_ascii,image)
print('INSERTED')
im = array_to_image(new_image,im)
print('CONVERTED BACK')
cv2.imwrite('.//created_images//ImageN.png',im)
print('SAVED')
im2 = cv2.imread('.//created_images//ImageN.png')
boolean = True
for i in range(len(im)):
	for j in range(len(im[i])):
		for k in range(len(im[i][j])):
			if im[i][j][k] != im2[i][j][k]:
				boolean = False
if boolean:
	print('Saving went well')
else:
	print('Something went wrong saving')
