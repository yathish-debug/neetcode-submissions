class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=''
        
        for string in strs:
            encoded_string+= str(len(string))+','+string
        print(encoded_string,'encoded_string')
        return encoded_string

    def decode(self, s: str) -> List[str]:
        
        decoded_array=[]
        if len(s)==1:
            return [""]
        i=0
        while i<len(s):
            j=i
            while s[j]!=',':
                j+=1
            count = int(s[i:j])
            decoded_array.append(''.join(s[j+1:count+j+1]))
            i = count+j+1 

        return decoded_array 
'''
Input: strs = ["Hello","World"] 
rangee= 0-250 ASCII
encode: 
    encode_array = ''
    loop through every element 
        's1'
        add the count and special character
decode:
        decode-array=[]
        use a split function with a seperater we used in the encoder

strs = [Hello, World]
c = len(i)
'c'
'c,'
'c,Hello'
'c,Hello'
encoded_string = 'c,Helloc,World'
encoded_string = '5,Hello5,World'
decoded_array = []
for i in range(len(encoded_string)):
    if int(encoded_string[i]) and i+1 == ',':
        count = int(encoded_string[i])
        decoded_array.append(''.join(encoded_string[i+2, count+i+2]))
        i = count+i+2

TC: O(n+n) ~= O(n)
SC: O(n+n) != O(n)
'''