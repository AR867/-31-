# ================== Задача 3 — Обработка нескольких исключений ==================
def safe_operation(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Type error"

# Проверка задачи 3
print("\n=== Задача 3 ===")
print(safe_operation(10, 2))
print
