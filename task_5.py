class TestCase:
    def __init__(self):
        self.steps = {}  # инициализируем поле steps как пустой словарь
        self.result = None  # инициализируем поле result как None

    def set_step(self, step_number, step_text):
        """Добавляет шаг тест‑кейса в словарь steps."""
        self.steps[step_number] = step_text

    def delete_step(self, step_number):
        """Удаляет шаг из словаря steps по номеру шага."""
        if step_number in self.steps:
            del self.steps[step_number]

    def set_result(self, result):
        """Устанавливает ожидаемый результат тест‑кейса."""
        self.result = result

    def get_test_case(self):
        """Печатает информацию о составе тест‑кейса в заданном формате."""
        output = {
            'Шаги': self.steps,
            'Ожидаемый результат': self.result
        }
        print(output)



# Пример использования класса
test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()
##задание 5