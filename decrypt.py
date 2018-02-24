import cv2

def image_to_array(im):
	ret = []
	for layer in im:
		for pixel in layer:
			ret.append(pixel[0]); ret.append(pixel[1]); ret.append(pixel[2])
	return ret

def extract_message_from_the_image(array):
	array_of_binary_pairs = []
	for element in array:
		array_of_binary_pairs.append(element & 3)
	ret = []
	for i in range(len(array)//4):
		ret.append(0)
		for j in range(4):
			ret[i] += array_of_binary_pairs[4*i+j] << 2 * j
		
		#ret.append(array_of_binary_pairs[4*i+3]
	return ret
	
def ascii_to_string(s):
	ret = ''
	for letter in s:
		if letter == 0:
			break
		ret += chr(letter)
	return ret
	
im = cv2.imread('.//created_images//ImageN.png')
image = image_to_array(im)
print('CONVERTED')
message_ascii = extract_message_from_the_image(image)
print('EXTRACTED')
message = ascii_to_string(message_ascii)
print(message)
