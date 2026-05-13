time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0

# Разбиваем строку на отдельные временные значения
time_values = time_string.split(',')

# Обрабатываем каждое временное значение
for value in time_values:
    # Убираем пробелы и разбиваем на части
    parts = value.replace(' ', ' ').split()
    
    for part in parts:
        if 'h' in part:
            # Извлекаем число часов (удаляем 'h' и преобразуем в число)
            hours = int(part.replace('h', ''))
            total_minutes += hours * 60
        elif 'm' in part:
            # Извлекаем число минут (удаляем 'm' и преобразуем в число)
            minutes = int(part.replace('m', ''))
            total_minutes += minutes
        elif 's' in part:
            # Извлекаем число секунд (удаляем 's' и преобразуем в число),
            # затем переводим в минуты (делим на 60)
            seconds = int(part.replace('s', ''))
            total_minutes += seconds // 60

print(total_minutes)

##1 задание