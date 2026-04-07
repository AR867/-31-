# ================== Задача 1 — Перехват ошибки деления ==================
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero"

# Проверка задачи 1
print("=== Задача 1 ===")
print(safe_divide(10, 2))
print(safe_divide(5, 0))
