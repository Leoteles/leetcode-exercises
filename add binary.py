# https://leetcode.com/problems/add-binary/

#%%
a = '11'
b = '1'
c = int(a,2)+int(b,2)
print(bin(c)[:2])


#%%
# 92% 26%
# using int(num,2)
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #bin() prints 0b before the number
        return bin(int(a,2)+int(b,2))[2:]
        
#%%

#solution 24% 7%

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        num_a =  0
        num_b =  0

        for i in a:
            num_a = num_a << 1
            num_a =  num_a + int(i)
        for i in b:
            num_b = num_b << 1
            num_b =  num_b + int(i)
        soma = num_a+num_b

        if soma == 0:
            return '0'

        k = 0
        out = ''
        while 2**k <= soma:
            bit = soma & (1 << k) >=1
            out = str(int(bit)) + out
            k += 1

        return out

#%%
# solucao 5% 54%
a = "11"
b = "1"
len_a = len(a)
len_b = len(b)

out = ''
carry = 0
for i in range(-1,-max(len_a,len_b)-1,-1):
    num_a = int(a[i]) if abs(i) <= len_a else 0
    num_b = int(b[i]) if abs(i) <= len_b else 0
    
    bit_sum =  num_a ^ num_b ^ carry
    carry = int(num_a + num_b + carry > 1)

    out = str(bit_sum) + out
    print(i,num_a,num_b,out,carry)
if carry:
    out = str(carry) + str(out)
print(out)





#%%
a = "11"
b = "1"
a = "0"
b = "0"

