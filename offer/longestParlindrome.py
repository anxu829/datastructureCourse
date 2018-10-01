class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = 'abcba'


        string = s

        maxstring = ''
        lenOfString = len(string)
        # 注意，每次只需要位置最后一列的数组
        mask = []
        max_ = 0
        for col in range(len(string)):
            for row in range(0,col + 1):
                # print(row, col)
                if row == col:
                    mask.append( string[col] == string[row] )
                if col - row == 1:
                    mask[col -1 ] = string[col] == string[row]
                if col - row > 1 :
                    mask[row]  = mask[row + 1] and string[row] == string[col]
            if len(mask) - mask.index(True) > max_ :
                max_ =len(mask) - mask.index(True) 
                maxstring = string[mask.index(True): col+1]
        return maxstring
