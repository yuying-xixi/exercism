#include "hamming.h"
#include <string.h>

int compute(const char *lhs, const char *rhs){
    int hamming_distance = 0;
    int l_length = strlen(lhs);
    int r_length = strlen(rhs);
    if (l_length != r_length) return -1;
    
    for(int i=0;i < r_length; i++){
       if (*(lhs + i) != *(rhs + i)){
           hamming_distance++;
       }
    }
    return hamming_distance;
}
