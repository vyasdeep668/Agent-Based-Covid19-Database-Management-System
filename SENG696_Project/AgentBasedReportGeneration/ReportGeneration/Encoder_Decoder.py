import binascii
import base64
import os


# This function encodes file into string
# Input: path of the file which needs to be converted
# Output: string version of the file
# Example: file_str = encode_file_to_str("DeepVyas_Resume.pdf")
def encode_file_to_str(file_path):
    file = open(file_path, "rb")
    file_base64 = base64.b64encode(file.read())
    file_str = file_base64.decode('utf-8')
    file.close()

    return file_str


# This function decodes string to file
# Input: string version of the file
# Output: path of the file at which file has been saved
# Example: decode_str_to_file(file_str, "DeepVyas_Resume_Decoded.pdf")
def decode_str_to_file(file_str, file_path):
    file = open(file_path, 'wb')
    file_byte = str.encode(file_str)
    file_base64 = base64.b64decode(file_byte)
    file.write(file_base64)
    file.close()

    return file_path

# decode_str_to_file(encode_file_to_str("DeepVyas_Resume.pdf"), "DeepVyas_Resume_Decoded.pdf")
# decode_str_to_file(encode_file_to_str("Images/Image1.jpg"), "Images/Image1_Decoded.jpg")




