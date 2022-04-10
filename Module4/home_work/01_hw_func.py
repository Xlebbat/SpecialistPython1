# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) == 6:
        digits_tiket_list = [int(i) for i in str(ticket_number)]
        return sum(digits_tiket_list[:3]) == sum(digits_tiket_list[3:])
    return False


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
