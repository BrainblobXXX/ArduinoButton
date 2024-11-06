const int analogPin = A6; // Номер аналогово пина кнопки
const int threshold = 1; // Уставка срабатывания кнопки (меньше уставки = сработала)
int currentValue, prevValue; // Переменные фильтра кнопки
bool trigg; // Переменная блокировки долгого нажатия кнопки

void setup() {
  Serial.begin(9600); // Инициализация серийного интерфейса
}

void loop() {
  
  currentValue = analogRead(analogPin); // Читаю текущее состояние кнопки

   if (currentValue != prevValue) {
    // Что-то изменилось, здесь возможна зона неопределенности
    // Делаем задержку
    delay(40);
    // А вот теперь спокойно считываем значение, считая, что нестабильность исчезла
    currentValue = analogRead(analogPin);
  }
  prevValue = currentValue;

  if (currentValue < threshold and trigg == 0) { // Проверка нажата ли кнопка и была ли она зажата в предыдущий цикл
    Serial.println("Button ON"); // Передаем сообщение ПК о нажатии кнопки
    delay(500);
    trigg = 1; //выставляем флаг зажатой кнопки
  } else if (currentValue >= threshold) {
    trigg = 0; //снимаем флаг зажатой кнопки
  }
  
}
