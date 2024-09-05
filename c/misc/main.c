#include <stdio.h>

int main(void)
{
    // the character '4' has an ASCII value of 52.
    char* c = "4";
    printf("char c -> %s\n", c);
    int num_c = -1;

    // The variable c is a pointer to a string literal "4", and c[0] accesses
    // the first character of this string, which is '4'.
    // The expression c[0] - '0' subtracts the ASCII value of the character '0'
    // (which is 48) from the ASCII value of c[0] (which is 52).
    num_c = c[0] - '0';
    // The result of this subtraction is 52 - 48, which equals 4.
    // This effectively converts the character '4' to its integer equivalent, 4.
    printf("num_c -> %d\n", num_c);
    return 0;
}
