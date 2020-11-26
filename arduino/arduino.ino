#define AMOUNT_PINS 2

#define FAST_MODE

#ifdef FAST_MODE
int pins[] = {
    24, 25, 26, 27, 28, 29, 30, 31,                                 // data
    34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, // address
    51, 52, 53                                                      // rest
};
// https://www.arduino.cc/en/Hacking/PinMapping2560
// 22 - 29 -> PortA 0 - 7
// 30 - 37 -> PortC 7 - 0
// 38      -> PortD 7
// 39 - 41 -> PortG 2 - 0
// 42 - 49 -> PortL 7 - 0
// 50 - 53 -> PortK 3 - 0
#else
int pins[] = {4, 7};
#endif

// in microseconds
#define SAMPLING_INTERVAL 10


void setup()
{
    Serial.begin(230400);
    for (int i = 0; i < AMOUNT_PINS; i++)
    {
        pinMode(pins[i], INPUT);
    }
}

void loop()
{

    if (micros() % SAMPLING_INTERVAL == 0)
    {
        String data = "";
        
        #ifdef FAST_MODE
        
        // make evulation on needed pins on receiver side.
        data += (String)PORTA + "; ";
        data += (String)PORTC + "; ";
        data += (String)PORTD + "; ";
        data += (String)PORTG + "; ";
        data += (String)PORTL + "; ";
        data += (String)PORTK;
        
        #else
        
        for (int i = 0; i < AMOUNT_PINS; i++)
        {
            data += (String)digitalRead(pins[i]);
            if (i != AMOUNT_PINS - 1)
            {
                data += "; ";
            }
        }
        
        #endif

        Serial.println(data);
    }
}
