class Solution:
    def largestRectangleArea(self, heights):
        res = 0
        st = []
        n = len(heights)

        for i, h in enumerate(heights):
            while st and heights[st[-1]] > h:
                height = heights[st.pop()]
                left = st[-1] if st else -1
                width = i - left - 1
                res = max(res, height * width )
            st.append(i)

        while st:
            height = heights[st.pop()]
            left = st[-1] if st else -1
            width = n - left - 1
            res = max(res, height * width )

        return res
