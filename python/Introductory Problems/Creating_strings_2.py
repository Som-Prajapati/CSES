from itertools import permutations


def main():
    s = input()
    b = set()
    for i in permutations(s):
        b.add("".join(i))
    ans = list(b)
    ans.sort()
    print(len(ans))
    print("\n".join(ans))


main()
