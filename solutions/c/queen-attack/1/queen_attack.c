#include "queen_attack.h"

attack_status_t can_attack(position_t queen_1, position_t queen_2){
    // init_position
    int queen_1_column = queen_1.column;
    int queen_1_row = queen_1.row;
    int queen_2_column = queen_2.column;
    int queen_2_row = queen_2.row;
    // INVALID_POSITION
    if(queen_1_column <0 || queen_1_row <0 ||
       queen_2_column <0 || queen_2_row <0 || 
       queen_1_column> 7 || queen_1_row > 7 ||
       queen_2_column > 7 || queen_2_row > 7 ||
       (queen_1_column == queen_2_column && queen_1_row == queen_2_row)
      ) return INVALID_POSITION;
    // CAN_ATTACK
    if(queen_1_column == queen_2_column || 
       queen_1_row == queen_2_row || 
       (queen_1_column - queen_2_column) == (queen_1_row - queen_2_row) ||
       (queen_1_column + queen_1_row) == (queen_2_column + queen_2_row)
      ) return CAN_ATTACK;
    // CAN_NOT_ATTACK
    return CAN_NOT_ATTACK;
    
}