#define AMOUNT_PINS 2

int pins[] = {4, 7};

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
