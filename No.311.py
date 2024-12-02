# yukicoder_no.311

N = int(input())

Fizz = (N // 3) * 2
Buzz = (N // 5) * 2

z_counter = (Fizz + Buzz)
print(z_counter)

# 名前を付けなければ一行で簡潔に記述できる
# print((N // 2 + N // 5) * 2 )
# 何を出力しているのか分かりやすいほうがいいのか, 短いコードがいいのか, 天秤にかける