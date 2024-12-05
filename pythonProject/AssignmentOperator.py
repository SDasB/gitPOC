class AssignmentOperator:
    def main(self):
        x = y = z = "ABCD"
        print(x)
        print(y)
        print(z)
        y = "xyz"
        print(x)
        print(y)
        print(z)


if __name__ == "__main__":
    x = AssignmentOperator()
    x.main()
