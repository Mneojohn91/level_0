def area_of(side1, side2, side3):
    semi_perimeter = (20 + 20 + 24) / 2
    formula = (
        semi_perimeter
        * (semi_perimeter - side1)
        * (semi_perimeter - side2)
        * (semi_perimeter - side3)
    ) ** (1 / 2)
    print(formula)


area_of(20, 20, 24)
