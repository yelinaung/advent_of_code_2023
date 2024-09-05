#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

char* read_from_file(char* filename)
{
    FILE* file = fopen(filename, "r");
    if (file == NULL) {
        fprintf(stderr, "Could not open file %s\n", filename);
        return NULL;
    }
    // seek to the end
    fseek(file, 0, SEEK_END);
    int length = ftell(file);
    fseek(file, 0, SEEK_SET);

    char* contents = malloc(sizeof(char) * length + 1);
    fread(contents, 1, length, file);
    contents[length] = '\0';
    return contents;
}

int main(void)
{
    printf("Hello Day1\n");
    char* contents = read_from_file("day_1.txt");
    if (contents == NULL) {
        return 1;
    }
    int first_num = -1;
    int last_num = -1;
    int sum = 0;
    for (size_t i = 0; contents[i] != '\0'; i++) {
        if (isdigit(contents[i])) {
            // first time
            if (first_num == -1 ) {
                first_num = contents[i] - '0';
            }
            last_num = contents[i] - '0';
        }
        // last line or next line
        if (contents[i] == '\n' || contents[i+1] == '\0') {
            // printf("first_num: %d, last_num: %d\n", first_num, last_num);
            sum += first_num * 10 + last_num;
            first_num = -1;
            last_num = -1;
        }
    }
    printf("sum: %d\n", sum);
    free(contents);
    return 0;
}
