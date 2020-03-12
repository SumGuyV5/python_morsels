def justify_col(row, col_widths, justify):
    return [
        column.ljust(length) if justify == 'L' else column.rjust(length)
        for column, length, justify in zip(row, col_widths, justify)
    ]


def format_fixed_width(rows, padding=2, widths=None, justify=None):
    if widths is None:
        widths = [
            max(len(cell) for cell in col)
            for col in zip(*rows)
        ]
    if justify is None:
        justify = ['L'] * len(widths)

    joiner = " " * padding
    return "\n".join(
        joiner.join(justify_col(row, widths, justify)).rstrip()
        for row in rows
    )


if __name__ == '__main__':
    print(f"{format_fixed_width([['green', 'red'], ['blue', 'purple']])}")