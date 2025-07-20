class Solution:
    def asteroidCollision(self, N,arr):
        st = []
        for i in range(N):
            asteroid = arr[i]
            while st and asteroid < 0 < st[-1]:
                if st[-1] < -asteroid:
                    st.pop()
                    continue
                elif st[-1] == -asteroid:
                    st.pop()
                break
            else:
                st.append(asteroid)
        return st
