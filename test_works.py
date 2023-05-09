#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h> #include <unistd.h>
#include <time.h>
#define SPICH 0 // SPI
#define ADC CH2 0 // AD 변환기 채널
#define ADC_CS 10
#define SPI_SPEED 500000 // SPI Speed
int main(void){
int adcValue=0, i;
char adChannel = ADC_CH2;
unsigned char buff];
MIDI
if(waringPiSetup () == -1)
return 1;
pinMode(ADC_CS,OUTPUT);
if(wiringPiSPISetup(SPI_CH,SPI_SPEED) == -1){
printf("wiringPi SPI Setup failed!Wn");
exit(0);
S
while(1){
buff0] = 0x06 | ((adChannel & 0x07)> > 2);
buff1] = ((adChannel & 0x07) < <6);
buf(2] = 0x00;
digitalWrite(ADC_CS,O);
wiringPiSPIDataRW(SPI_CH,buf,3);
buf[1] = OxOF & buff1];
adcValue = (buf[1] < < 8) | bufl2];
digitalWrite(ADC_CS, 1);
printf("Sound ADC Value -> %dWn", adcValue);
usleep(100000);
return 0;


