import sys


class ListPOC:
    def main(self):
        list1 = [0] * 3
        list2 = [0, 0, 0]
        list3 = [0 for i in range(3)]
        print(list1)
        print(list2)
        print(list3)

        print("size of list1 :", sys.getsizeof(list1))
        print("size of list2 :", sys.getsizeof(list2))
        print("size of list3 :", sys.getsizeof(list3))


if __name__ == "__main__":
    x = ListPOC()
    x.main()
