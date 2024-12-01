# yukicoder_no.47

biscuit_requirement = int(input())
biscuit = 1
punch = 0

while biscuit < biscuit_requirement:
    biscuit *= 2
    punch += 1

print(punch)
