# 'hAck3rr4ank' -->  '43Ah*ck0rr0nk'
s  = '43Ah*ck0rr0nk'

def passdecryption(s):
    s_list = []
    i = 0
    b = 0
    j = len(s) - 1
    for char in range(len(s)):
        s_list.append(s[char])
    # print(s_list)
    while b <= len(s):
        num = ['1','2','3','4','5','6','7','8','9','0']
        cap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        if s_list[i]  in  cap and s_list[i+1]  in small and s_list[i+2] == '*':
        
            i_val = s_list[i]
            i_1_val = s_list[i+1] 
            s_list[i] = i_1_val
            s_list[i+1] = i_val
            s_list.remove(s_list[i+2])
        elif s_list[i] in num :
            while j >= 0 :
                if s_list[j] == '0':

                    s_list[j] = s_list[i]
                    j_val = s_list[j]
                    i_val = s_list[i] 
                    s_list[j] = i_val
                    s_list[i] = j_val
                    s_list.remove(s_list[i])
                j -= 1
        b += 1
    pass_decrypt = ''.join(s_list)
    return pass_decrypt
    

if __name__ == '__main__':
    print(passdecryption(s))
      



