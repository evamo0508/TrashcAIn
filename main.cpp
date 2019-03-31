
#include "Motor.h"

Serial bt(PD_5, PD_6);
Serial pc(SERIAL_TX, SERIAL_RX);
DigitalOut IN_1(PF_2);
DigitalOut IN_2(PE_5);
DigitalOut IN_3(PG_0);
DigitalOut IN_4(PG_1);
Motor motor(&IN_1, &IN_2, &IN_3, &IN_4);

int main() {
    char buf[30];
    bool str_ready = false;
    int i = 0;
    pc.printf("trashcain start!\r\n");
    while(1) {
        if(bt.readable()) {
          char ch = bt.getc();
          buf[i] = ch;
          i++;
          if(ch == '\n') {
            str_ready = true; 
          }
        }
        if(str_ready) {  
          pc.printf(buf);
          if(!strcmp(buf, "front\r\n")) {
             pc.printf("front action\r\n");
             motor.forward();    
          }
          else if(!strcmp(buf, "back\r\n")) {
            pc.printf("back action\r\n");
            motor.backward();
          }
          else if(!strcmp(buf, "stop\r\n")) {
            pc.printf("stop action\r\n");
            motor.stop();    
          }
          for(int j = 0; j < 30; j++) {
            buf[j] = 0;
          }
          str_ready = false;
          i = 0;
        }
        
    }
//        pc.printf("front\n");
//        motor.forward(2000);
//        motor.stop();
//        wait(1.0);
//        pc.printf("back\n");
//        motor.backward(2000);
//        motor.stop();
//        wait(1.0);
        //pc.printf("left\n");
//        motor.left(2000);
//        motor.stop();
//        wait(1.0);
//        pc.printf("right\n");
//        motor.right(2000);
//        motor.stop();
//        wait(1.0);
        //if(pc.readable()) {
//            bt.putc(pc.getc());
//        }
//        if(bt.readable()) {
//            pc.putc(bt.getc());
//        }
    
}
