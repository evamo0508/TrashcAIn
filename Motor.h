
#include "mbed.h"

class Motor {
    private:    
     DigitalOut* _in_1;
     DigitalOut* _in_2;
     DigitalOut* _in_3;
     DigitalOut* _in_4;
     
   public:
   Motor(DigitalOut* in_1, DigitalOut* in_2, DigitalOut* in_3, DigitalOut* in_4) {
     _in_1 = in_1; 
     _in_2 = in_2; 
     _in_3 = in_3; 
     _in_4 = in_4;    
   }
   void stop() {
     _in_1->write(0);
     _in_2->write(0);
     _in_3->write(0);
     _in_4->write(0);   
   }
   void forward() {
     _in_1->write(1);
     _in_2->write(0);
     _in_3->write(0);
     _in_4->write(1);
   }
   void backward() {
     _in_1->write(0);
     _in_2->write(1);
     _in_3->write(1);
     _in_4->write(0);
   }
   void left() {
     _in_1->write(1);
     _in_2->write(0);
     _in_3->write(0);
     _in_4->write(1);
   }
   void right() {
     _in_1->write(0);
     _in_2->write(1);
     _in_3->write(1);
     _in_4->write(0);
   }

  
};