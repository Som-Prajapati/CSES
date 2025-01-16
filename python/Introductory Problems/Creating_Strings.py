letter = [i for i in input()]

letter.sort()
values = []


def creating_strings(a=None, b=None) -> None:
    if a == None:
        a = [0] * len(b)

    if len(b) == 1:
        a[-1] = b[0]
        values.append("".join(a))
        return

    for i in range(len(b)):

        if i > 0:
            if b[i - 1] == b[i]:
                continue

        x = b.copy()
        a[-len(b)] = b[i]
        x.pop(i)
        creating_strings(a, x)


creating_strings(b=letter)
print(len(values))
print("\n".join(values))
