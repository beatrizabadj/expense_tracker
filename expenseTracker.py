from expense import Expense

def main():
    print("Ejecutando")
    expense_file = "expenses.csv"
    budget = 1000  # Define el presupuesto

    # Entrada del usuario
    expense = get_user_expense()
    print(f"Gasto introducido: {expense.name}, {expense.category}, {expense.amount}")  # Depuración
    
    # Escribir entrada en el archivo
    save_expense(expense, expense_file)

    # Leer gastos y mostrar
    show_expenses(expense_file)

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
    print(f"Guardando datos {expense.name}, {expense.category}, {expense.amount} a {expense_file}")
    with open(expense_file, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

def show_expenses(expense_file):
    print("Mostrando gastos: ")
    expenses = []
    with open(expense_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 3:
                expense_name, expense_category, expense_amount = parts
                print(f"Leyendo: {expense_name}, {expense_category}, {expense_amount}")  # Depuración
                line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
                expenses.append(line_expense)
            else:
                print(f"Formato incorrecto en la línea: {line.strip()}")

    category_amount = {}
    for expense in expenses:
        print(f"Procesando gasto: {expense.name}, {expense.category}, {expense.amount}")  # Depuración
        if expense.category in category_amount:
            category_amount[expense.category] += expense.amount
        else:
            category_amount[expense.category] = expense.amount

    print("Gastos por categoría:")
    for category, total_amount in category_amount.items():
        print(f"  {category}: ${total_amount:.2f}")

    total_spent = sum(x.amount for x in expenses)
    print(f"Total gastado: ${total_spent:.2f}")

# Ejecutar el archivo solo sin ser parte de otro archivo
if __name__ == "__main__":
    main()
