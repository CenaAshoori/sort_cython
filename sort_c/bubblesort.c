#include <stdio.h>

typedef unsigned int BOOL;
#define FALSE 0
#define TRUE 1

void sort(int* array, int size) {
    int i, j;
    for (i = 0; i < size-1; i++) {
        BOOL sorted = TRUE;
        for (j = 0; j < size-i-1; j++)
            if (array[j] > array[j+1]) {
                sorted = FALSE;
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        if (sorted)
            break;
    }
}