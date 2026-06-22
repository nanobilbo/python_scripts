# tres codigos de acceso

edad = 25
tiene_licencia = True
if edad >= 18 and tiene_licencia:
    print("puedes conducir")
else:
    print("no puedes conducir")

# pedido en restaurante
es_dia_laboral = False
es_festivo = True

if es_dia_laboral or es_festivo:
    print("el restaurante esta abierto")
else:
    print("el restaurante esta cerrado")

"""
explicacion del 
es_dia_semana = False   # Esto es "NO es día semana"
es_festivo = True       # Esto es "SÍ es festivo"

# Evaluamos la condición
if es_dia_semana or es_festivo:
    # Reemplazamos con los valores
    if False or True:
        # Aplicamos la regla del or
        if True:  # Porque False or True = True
            print("📅 El restaurante está abierto")
"""
# CASO 1: Día semana SÍ, Festivo SÍ
es_dia_semana = True
es_festivo = True
print(f"Día semana: {es_dia_semana}, Festivo: {es_festivo}")
if es_dia_semana or es_festivo:
    print("✅ ABIERTO (True or True = True)\n")

# CASO 2: Día semana SÍ, Festivo NO
es_dia_semana = True
es_festivo = False
print(f"Día semana: {es_dia_semana}, Festivo: {es_festivo}")
if es_dia_semana or es_festivo:
    print("✅ ABIERTO (True or False = True)\n")

# CASO 3: Día semana NO, Festivo SÍ
es_dia_semana = False
es_festivo = True
print(f"Día semana: {es_dia_semana}, Festivo: {es_festivo}")
if es_dia_semana or es_festivo:
    print("✅ ABIERTO (False or True = True)\n")

# CASO 4: Día semana NO, Festivo NO
es_dia_semana = False
es_festivo = False
print(f"Día semana: {es_dia_semana}, Festivo: {es_festivo}")
if es_dia_semana or es_festivo:
    print("✅ ABIERTO")
else:
    print("❌ CERRADO (False or False = False)\n")