class Solution:
    def compress(self, chars: List[str]) -> int:
        
        write = 0 
        read = 0
        charLen = 1
# write.  0 1 2
# read    4 5
# charLen 5 1
        for read in range(len(chars)):
            if read + 1 < len(chars) and chars[read] == chars[read+1]:
                charLen += 1

            if (read + 1 < len(chars) and chars[read] != chars[read+1]) or read == len(chars) - 1:
                if charLen == 1:
                    chars[write] = chars[read]
                    write += 1
                else:
                    chars[write] = chars[read]
                    write += 1
                    for digit in str(charLen):
                        chars[write] = digit
                        write += 1
                    charLen = 1 

        print(chars)
        return write

