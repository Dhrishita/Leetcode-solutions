class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        delta = [0] * (n + 1)
        for start, end, direction in shifts:
            if direction == 1:
                delta[start] += 1
                if end + 1 < n:
                    delta[end + 1] -= 1
            else:
                delta[start] -= 1
                if end + 1 < n:
                    delta[end + 1] += 1
        shift_value = 0
        for i in range(n):
            shift_value += delta[i]
            delta[i] = shift_value
        result = []
        for i in range(n):
            new_char = chr((ord(s[i]) - ord('a') + delta[i]) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)