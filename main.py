from datos import usuarios, soluciones, tickets


# Muestra el encabezado inicial del chatbot.
def mostrar_encabezado():
    print("=" * 60)
    print("CHATBOT DE SOPORTE TÉCNICO NIVEL 1")
    print("Mesa de ayuda interna - Organización G&H")
    print("=" * 60)


# Valida si el legajo existe y si el usuario está activo.
def validar_usuario(legajo):
    usuario = usuarios.get(legajo)

    if usuario is None:
        return None, "no_encontrado"

    if usuario["estado"] != "activo":
        return usuario, "inactivo"

    return usuario, "activo"


# Muestra las categorías de problemas disponibles.
def mostrar_menu_problemas():
    print("\nSeleccioná el tipo de problema:")
    print("1. Internet")
    print("2. Login")
    print("3. Impresora")
    print("4. Correo")
    print("5. Software")
    print("6. Hardware")
    print("7. Otro")


# Solicita una opción válida del menú.
def pedir_opcion_menu():
    while True:
        opcion = input("\nIngresá una opción del 1 al 7: ").strip()

        if opcion in soluciones:
            return opcion

        print("Opción inválida. Por favor, ingresá un número del 1 al 7.")


# Pregunta si la solución resolvió el problema.
def pedir_confirmacion():
    while True:
        respuesta = input("\n¿La solución resolvió el problema? (si/no): ").strip().lower()

        if respuesta in ["si", "sí", "s"]:
            return True

        if respuesta in ["no", "n"]:
            return False

        print("Respuesta inválida. Por favor, respondé 'si' o 'no'.")


# Pregunta si el usuario tiene otro problema.
def pedir_otro_problema():
    while True:
        respuesta = input("\n¿Tenés algún otro problema? (si/no): ").strip().lower()

        if respuesta in ["si", "sí", "s"]:
            return True

        if respuesta in ["no", "n"]:
            return False

        print("Respuesta inválida. Por favor, respondé 'si' o 'no'.")


# Solicita un correo válido para seguimiento.
def pedir_email():
    while True:
        email = input("\nIngresá un correo electrónico para seguimiento: ").strip()

        if "@" in email and "." in email:
            return email

        print("Correo inválido. Por favor, ingresá un correo válido.")


# Genera un ticket simulado y lo guarda en la lista de tickets.
def generar_ticket(legajo, categoria, estado, email_contacto=None):
    ticket = {
        "id_ticket": len(tickets) + 1,
        "legajo": legajo,
        "categoria": categoria,
        "estado": estado,
        "email_contacto": email_contacto
    }

    tickets.append(ticket)
    return ticket


# Muestra el estado final del ticket.
def informar_ticket(ticket):
    print("\n" + "-" * 60)
    print(f"Ticket N°: {ticket['id_ticket']}")
    print(f"Categoría: {ticket['categoria']}")
    print(f"Estado final: {ticket['estado']}")

    if ticket["email_contacto"]:
        print(f"Correo de seguimiento: {ticket['email_contacto']}")

    print("-" * 60)


# Procesa el problema seleccionado y define si se cierra o deriva.
def procesar_problema(legajo, opcion):
    datos_problema = soluciones[opcion]
    categoria = datos_problema["categoria"]

    print(f"\nCategoría seleccionada: {categoria}")

    if datos_problema["deriva_directo"]:
        print("\nEste caso requiere revisión manual del área de soporte.")
        email = pedir_email()
        ticket = generar_ticket(legajo, categoria, "Derivado a soporte", email)
        informar_ticket(ticket)
        return

    print("\nSolución sugerida:")
    print(datos_problema["solucion"])

    soluciono = pedir_confirmacion()

    if soluciono:
        ticket = generar_ticket(legajo, categoria, "Cerrado correctamente")
        informar_ticket(ticket)
    else:
        print("\nEl caso será derivado a soporte técnico.")
        email = pedir_email()
        ticket = generar_ticket(legajo, categoria, "Derivado a soporte", email)
        informar_ticket(ticket)


# Ejecuta el flujo principal del chatbot.
def iniciar_chatbot():
    mostrar_encabezado()

    print("\nBienvenido al sistema de soporte técnico.")

    while True:
        legajo = input("Ingresá tu legajo: ").strip()

        usuario, estado = validar_usuario(legajo)

        if estado == "no_encontrado":
            print("\nEl legajo ingresado no corresponde a un usuario registrado.")
            print("No se puede continuar con la solicitud.")
            print("Ingresá un legajo válido.")
            continue

        if estado == "inactivo":
            print(f"\nEl usuario {usuario['nombre']} existe, pero se encuentra inactivo.")
            print("No se puede continuar con la solicitud.")
            print("Ingresá otro legajo válido.")
            continue

        break

    print("\nUsuario validado correctamente.")
    print(f"Nombre: {usuario['nombre']}")
    print(f"Departamento: {usuario['departamento']}")

    while True:
        mostrar_menu_problemas()
        opcion = pedir_opcion_menu()
        procesar_problema(legajo, opcion)

        tiene_otro_problema = pedir_otro_problema()

        if not tiene_otro_problema:
            break

    print("\nGracias por utilizar el chatbot de soporte técnico.")


if __name__ == "__main__":
    iniciar_chatbot()