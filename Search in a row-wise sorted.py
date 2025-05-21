class Solution:

    # Row-wise sorted matrix mein search karne ka function
    def searchRowMatrix(self, mat, x):
        n = len(mat)
        m = len(mat[0])

        for i in range(n):
            # Pehle check karo ki x iss row mein ho sakta hai ya nahi
            if mat[i][0] <= x <= mat[i][m - 1]:
                # Binary search lagao uss row mein
                low, high = 0, m - 1
                while low <= high:
                    mid = (low + high) // 2
                    if mat[i][mid] == x:
                        return True  # Element mil gaya
                    elif mat[i][mid] < x:
                        low = mid + 1  # Right half mein dhoondo
                    else:
                        high = mid - 1  # Left half mein dhoondo
        return False  # Agar kahin nahi mila toh False return karo
