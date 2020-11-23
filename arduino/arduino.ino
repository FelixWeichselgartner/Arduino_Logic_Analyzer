#define AMOUNT_PINS 2

int pins[] = {4, 7};

/*int pins[] = {
    24, 25, 26, 27, 28, 29, 30, 31,                                 // data
    34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, // address
    51, 52, 53                                                      // rest
};*/

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

    if (micros() % 10 == 0)
    {
        String data = "";
        for (int i = 0; i < AMOUNT_PINS; i++)
        {
            data += (String)digitalRead(pins[i]);
            if (i != AMOUNT_PINS - 1)
            {
                data += "; ";
            }
        }
        Serial.println(data);
    }
}
