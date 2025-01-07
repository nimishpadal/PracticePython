"""Input: s = "This is a python language"
Output: This is python language"""

input_str = "Tamil Nadu Governor R.N. Ravi walks out of Assembly without reading customary address"
input_str = input_str.split(" ")
# print(input_str)
evenWordList = list(filter(lambda x: len(x) % 2 == 0, input_str))
output_str = " ".join(evenWordList)
print(output_str)