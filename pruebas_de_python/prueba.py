from goto import with_goto
@with_goto  # Decorador necesario.
def f():
    label .get_input  # Definir la etiqueta.
    age = input("Ingresa tu edad: ")
    try:
        age = int(age)
    except ValueError:
        goto .get_input  # Regresar a get_input.
    print("Tienes", age, "años.")
f()
