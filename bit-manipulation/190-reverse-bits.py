class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res


        # 0000 - 0 => 0100 >> 0 => 0 & 1 = 0
        # 0001 - 1 => 0100 >> 1 => 0 & 1 = 0
        # 0010 - 2 => 0100 >> 2 => 1 & 1 = 1
        # 0011 - 3 => 0100 >> 3 => 0 & 1 = 0

        # res += 0 << 3 - 0 = 0000
        # res += 0 << 3 - 1 = 0000
        # res += 1 << 3 - 2 = 0010
        # res += 0 << 3 - 3 = 0010
