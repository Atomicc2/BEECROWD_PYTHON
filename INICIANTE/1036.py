def main(a, b, c):
    if a <= 0 or b <=0 or c<= 0:
        print("Impossivel calcular")
        return

    delta = (b ** 2) - (4 * a * c)
    r1 = (-b + delta ** 0.5) / (2 * a)
    r2 = (-b - delta ** 0.5) / (2 * a)
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
    return


a, b, c = map(float, input().split())
main(a, b, c)