# Created by: Joanne Santhosh
# Created on: Nov 15
# This program calculates the factors of any integer


def main():
    # this function calculates the factor
    try:
        positive_integer = int(input("Enter an integer: "))

        def print_factors(integer):
            print("The factors of", integer, "are:")
            for i in range(1, integer + 1):
                if integer % i == 0:
                    print(i)

        print_factors(positive_integer)
    except Exception:
        print("\n This is an invalid input. Please try again")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
