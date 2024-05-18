from expense import Expense
import datetime

def main():
    print("Ejecutando")
    expense_file = "expenses.csv"
    budget = float(input("Introduce tu presupuesto: "))  # Solicitar al usuario que introduzca el presupuesto

    # Entrada del usuario
    expense = get_user_expense()
    print(f"Gasto introducido: {expense.name}, {expense.category}, {expense.amount}")

    # Escribir entrada en el archivo
    save_expense(expense, expense_file)

    # Leer gastos y mostrar
    show_expenses(expense_file, budget)

def get_user_expense():
    print("Introduciendo entrada del usuari@: ")
    expense_name = input("Introduce el nombre del gasto: ")
    expense_amount = float(input("Introduce la cantidad gastada: "))
    print(f"Has introducido {expense_name}, {expense_amount}")

    expense_categories = ["Alimentación", "Vivienda", "Transporte", "Ahorro e inversión", "Ropa y accesorios", "Vacaciones", "Otros"]

    while True:
        print("Selecciona la categoría: ")
        for index, category in enumerate(expense_categories, start=1):
            print(f"{index}. {category}")
        try:
            select_index = int(input("Escoja la categoría deseada: "))
        except ValueError:
            print("Introduzca un número válido.")
            continue

        if 1 <= select_index <= len(expense_categories):
            new_expense = Expense(name=expense_name, amount=expense_amount, category=expense_categories[select_index - 1])
            return new_expense
        else:
            print("Categoría no encontrada.")

def save_expense(expense: Expense, expense_file):
    now = datetime.datetime.now()
    expense_date = now.strftime("%Y-%m-%d")  # Obtener la fecha actual en formato YYYY-MM-DD
    print(f"Guardando datos {expense.name}, {expense.category}, {expense.amount} en {expense_file} el {expense_date}")
    with open(expense_file, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount},{expense_date}\n")

def show_expenses(expense_file, budget):
    print("Mostrando gastos: ")
    expenses = []
    with open(expense_file, "r") as f:
        lines = f.readlines()
        for index, line in enumerate(lines, start=1):
            parts = line.strip().split(",")
            if len(parts) == 4:
                expense_name, expense_category, expense_amount, expense_date = parts
                print(f"Leyendo {index}: {expense_name}, {expense_category}, {expense_amount} (Fecha: {expense_date})")
                line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
                expenses.append(line_expense)

    category_amount = {}
    for index, expense in enumerate(expenses, start=1):
        print(f"Procesando {index}: {expense.name}, {expense.category}, {expense.amount}")
        if expense.category in category_amount:
            category_amount[expense.category] += expense.amount
        else:
            category_amount[expense.category] = expense.amount

    print("Gastos por categoría:")
    for category, total_amount in category_amount.items():
        print(f"  {category}: ${total_amount:.2f}")

    total_spent = sum(x.amount for x in expenses)
    print(f"Total gastado: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"Presupuesto Restante: ${remaining_budget:.2f}")

if __name__ == "__main__":
    main()
