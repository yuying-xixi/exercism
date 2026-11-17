#include "collatz_conjecture.h"
#include <stdio.h>

int steps(int start){
    if (start <1){
        return ERROR_VALUE;
    }
    
    int count_step = 0;
    while(start != 1){
        if (start % 2 == 0) {
            start = start / 2;
            count_step++;
        }
        else{
            start = start * 3 + 1;
            count_step++;
        }
    }
    return count_step;
}