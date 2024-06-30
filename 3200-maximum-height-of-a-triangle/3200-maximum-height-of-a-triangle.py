class Solution(object):
    def getMaxHeight(self, red, blue, Parity, Height, maxHeight):
        if Height>red and Parity==1:
            return maxHeight
        if Height>blue and Parity==0:
            return maxHeight
        if Parity==1 and red>=Height:
            return self.getMaxHeight(red - Height, blue, 0, Height+1, maxHeight+1)
        elif Parity==0 and blue>=Height:
            return self.getMaxHeight(red, blue - Height, 1, Height+1, maxHeight+1)
        return 0

    def maxHeightOfTriangle(self, red, blue):
        return max(self.getMaxHeight(red, blue, 0, 1, 0), 
                   self.getMaxHeight(blue, red, 0, 1, 0))



