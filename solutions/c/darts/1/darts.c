#include "darts.h"

uint8_t score(coordinate_t landing_position){
    uint8_t earn_score = 0;
    float distance_sq = landing_position.x * landing_position.x + landing_position.y * landing_position.y;

    if (distance_sq <= 1){
        earn_score = 10;
    }
    else if (distance_sq <= 25){
        earn_score = 5;
    }
    else if (distance_sq <= 100){
        earn_score = 1;
    }
    else
        earn_score = 0;
        
    return earn_score;
}
