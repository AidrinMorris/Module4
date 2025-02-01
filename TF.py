# Truth Table for the expression: (A AND B) OR (NOT B)
# A      B      (A AND B) OR (NOT B)
# True   True   True
# True   False  True
# False  True   False
# False  False  True

def truth_table():
    print("A\tB\t(A AND B) OR (NOT B)")
    for A in [True, False]:
        for B in [True, False]:
            result = (A and B) or (not B)
            print(f"{A}\t{B}\t{result}")

truth_table()

