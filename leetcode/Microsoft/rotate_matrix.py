"""

    ROTATE IMAGE (in place):
        BCR == O(n^2) --> have to touch every pixel.
        
    PROCEDURE: top row becomes right column, right column becomes bottom row, etc etc
    STRATEGY:
        * iterate layer by layer: NxN image has N//2 layers.
            * if N is odd, still N//2 because middle pixel stays in place
        * call rotate layer on each layer
            * start with first pixel in first row, save it
            * overwrite first pixel with pixel from left, then left from bottom, bottom from right, right from saved
            * repeat for additional pixels in layer
    
    GENERALIZATION:
        Rotate 90, 180, 270 or 360 degrees?
        Overload Rotate_Pixel function. Set which part of matrix pixel will go to. Will not do here.


"""
tc_num = 0
def test_rotate():
    sut = Solution()
    
    def matrix_eq(m1,m2):
        if len(m1) != len(m2) or (len(m1) > 0 and (len(m1[0]) != len(m2[0]))): return False
        for row in range(len(m1)):
            for col in range(len(m1[0])):
                if m1[row][col] != m2[row][col]: return False
        return True
        
    def test(matrix,expected):
        global tc_num
        sut.rotate(matrix)
        assert matrix_eq(matrix,expected), "TC%d FAIL" % tc_num
        print("TC%d PASS" % tc_num)
        tc_num += 1

    test([],[])
    test([[1]],[[1]])
    test([[1,2],[4,3]],[[4,1],[3,2]]) 
    test([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]])
    
"""

1 2 3  7 4 1
4 5 6  8 5 2
7 8 9  9 6 3

"""
    
def rotate_layer(layer,matrix):
    for i in range(layer,len(matrix) - layer - 1):
        rotate_pixel(matrix,i,layer)

"""
1 2 temp = 1
3 4

3 2
3 4

3 2
4 4

3 2
4 2

3 1
4 2
"""

def rotate_pixel(matrix,pixel_num,layer):
    temp = matrix[layer][pixel_num]
    matrix[layer][pixel_num] = matrix[-(pixel_num + 1)][layer]
    matrix[-(pixel_num + 1)][layer] = matrix[-(layer + 1)][-(pixel_num + 1)]
    matrix[-(layer + 1)][-(pixel_num + 1)] = matrix[pixel_num][-(layer + 1)]
    matrix[pixel_num][-(layer + 1)] = temp

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        num_layers = N//2
        for layer in range(num_layers):
            rotate_layer(layer,matrix)
        
# test_rotate()
