class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        color=image[sr][sc]
        if color==newColor:
            return image
        r_max=len(image)-1
        c_max=len(image[sr])-1
        def fill_color(r,c):
            if (not ( 0<=r<=r_max)) or (not (0<=c<=c_max)) or image[r][c]!=color:
                return
            image[r][c]=newColor
            fill_color(r-1,c)
            fill_color(r+1,c)
            fill_color(r,c-1)
            fill_color(r,c+1)
            return
        fill_color(sr,sc)
        return image        