# yukicoder_no.57

N = int(input())
print(N * 3.5) # ev = sum((i * 1/6 for i in range(1, 7))) = 3.5

# 期待値の線形性
# https://manabitimes.jp/math/698


# 別解
import statistics
lst = range(N, N * 6 + 1)
print(statistics.median(lst))

# statistics は平均値, 中央値, 最頻値, 分散, 標準偏差などを求めるのに便利

