import pylab as p


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar_without = d.replace('$', '')
    return float(dollar_without)


def percent_to_float(p):
    percent_without = p.replace('%', '')
    p2 =float(percent_without) / 100
    return p2

main()