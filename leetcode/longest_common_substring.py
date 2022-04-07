def common(nums1: str, nums2: str) -> str:
    rows = len(nums1)
    cols = len(nums2)
    commons = [[0 for _ in range(cols)] for _ in range(rows)]
    max_common = 0
    def print_commons() -> None:
        for row in commons:
            print(row)

    for i in range(rows):
        for j in range(cols):
            if nums1[i] == nums2[j]:
                if i == 0 or j == 0:
                    commons[i][j] = 1
                else:
                    commons[i][j] = 1 + commons[i-1][j-1]
                max_common = max(max_common, commons[i][j])
                end = [i,j]
    
    result =  nums1[1 + end[0] - max_common:1 + end[0]]  
    print_commons()
    print(end, max_common, result)

common('bbbbXYZABCDE', 'aaXYZaaaaABCDE')
