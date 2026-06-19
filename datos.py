
usuarios = {
    "1001": {
        "nombre": "Rodrigo Guggiana",
        "departamento": "Administración",
        "estado": "activo"
    },
    "1002": {
        "nombre": "Mauricio Halberg",
        "departamento": "Sistemas",
        "estado": "activo"
    },
    "1003": {
        "nombre": "Carolina Bruno",
        "departamento": "Recursos Humanos",
        "estado": "inactivo"
    }
}

soluciones = {
    "1": {
        "categoria": "Internet",
        "solucion": "Verificá que el cable de red esté conectado o que la conexión WiFi esté activa. Luego reiniciá el navegador e intentá nuevamente.",
        "deriva_directo": False
    },
    "2": {
        "categoria": "Login",
        "solucion": "Verificá que el usuario y la contraseña estén correctamente ingresados. Si el problema continúa, restablecé la contraseña desde el portal interno.",
        "deriva_directo": False
    },
    "3": {
        "categoria": "Impresora",
        "solucion": "Verificá que la impresora esté encendida, conectada a la red y con papel disponible. Luego intentá imprimir nuevamente.",
        "deriva_directo": False
    },
    "4": {
        "categoria": "Correo",
        "solucion": "Cerrá sesión, volvé a ingresar al correo institucional y verificá la conexión a internet.",
        "deriva_directo": False
    },
    "5": {
        "categoria": "Software",
        "solucion": "",
        "deriva_directo": True
    },
    "6": {
        "categoria": "Hardware",
        "solucion": "",
        "deriva_directo": True
    },
    "7": {
        "categoria": "Otro",
        "solucion": "",
        "deriva_directo": True
    }
}

tickets = []