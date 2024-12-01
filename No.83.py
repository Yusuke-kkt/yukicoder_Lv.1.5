# yukicoder_no,83

match = int(input())

if match % 2 == 0:
    print("1" * (match // 2))
else:
    print("7" + "1" *(match // 2 - 1))

# '//' ではなく '/' にすると TypeError: can't maltiply sequence by non-int of type 'float'
# 整数: int
# 浮動小数点: float (数値を "X(仮数) * Y(基数) ^ Z(指数)" で表現する方法のこと？)