import sys
from parser import (
    print_key_value_pairs,
    write_output_properties,
    write_missing_properties,
    compare_and_write_differences_main
)

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    option = sys.argv[1]

    if option == "1":
        print_key_value_pairs()
    elif option == "2":
        write_output_properties()
    elif option == "3":
        write_missing_properties()
    elif option == "4":
        compare_and_write_differences_main()
    else:
        print("Invalid option")
        sys.exit(1)

if __name__ == '__main__':
    main()
