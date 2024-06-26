Plot-Mirroring
Mirroring a plot with respect to another plot

Этот небольшой код используется для отражения одного графика относительно другого. Конструктор класса Mirroring принимает следующие параметры: f_x, g_x, min_v, max_v, step.
Где:
f_x - функция, которую отражают;
g_x - функция, относительно которой отражают;

min_v, max_v, step - задают границы отражения и шаг. Т.е. анализируется все точки функции f_x на отрезке [min_v, max_v] с шагом step.

Подразумевается, что f_x и g_x на отрезке [min_v, max_v] определены, непрерывны и дифференцируемы.

В консоль выводится процентный счетчик, т.к. время выполнения программы зависит от порядка функции g_x.
Если g_x 2-го порядка (парабола), время выполнения составляет около 8 сек., тогда как ф-ии 3-го порядка вычисляются ~6 минут. 
(Данные приведены для ознакомления. Время выполнения зависит от устройств)

![image](https://github.com/WDW825/Plot-Mirroring/assets/87891702/790b8748-9d60-491b-9ee9-edc4c3884384)

На рисунке оранжевая прямая отражена относительно зеленого графика параболы. Результатом стала синяя линия
