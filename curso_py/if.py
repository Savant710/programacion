# si el estudiante saca sobre 95 aprobado con honores
# 50 a 95 aprobado
# - 50 reprobado
nota = 97
if nota >= 95:
    print("Aprobado con honores")
elif nota >= 50:
    print("alumno aprobado")
else:
    print("reprobado")
print("Hey aprobaste??")
aprobaste = input("si o no: ")
respuesta = bool(aprobaste)
if respuesta == True:
    print("Felicidades lo lograste")
else:
    print("Estudia mas duro tu puedes")
