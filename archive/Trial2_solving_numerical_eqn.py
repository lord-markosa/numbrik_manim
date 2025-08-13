def f(x):
    return x ** (1 / x)


target = 3 ** (1 / 9)
lo = 0.00001
hi = 2
eps = 1e-9

while hi - lo > eps:
    mid = (lo + hi) / 2
    if f(mid) < target:
        lo = mid
    else:
        hi = mid

x = (lo + hi) / 2

print(f"Solution: x = {x}")
print(f"x^(1/x) = {f(x)}")
