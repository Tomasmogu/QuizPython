# QuizPython
Diccionario y Glosario
d = {"Rio Amazonas": "Sudamerica",
     "Rio Missisipi": "Estados Unidos",
     "Rio Danubio": "Alemania",
     "Rio Yangste": "China",
     "Rio Nilo": "Egipto"
     }
print(d)
print(d.keys())
for key in d:
    print(key,end="\n")
print(d.items())
for item in d:
    print(d[item])

for o in {"El Amazonas es el rio mas importante del mundo",
          "El Missisipi es el segundo rio mas grande",
          "El Danubio pasa por Alemania y Heslovaquia",
          "El Yangste es el 5into rio mas importante",
          "El rio Nilo esta en Egipto"}:
   print(o,end="\n")


print("\t---------------Bienvenido a mi glosario---------------")
print("\t      las palabras que a lo largo del semestre son:")

#palabras
print("\n>Java:\n\tPlataforma informática de lenguaje de programación creada por Sun Microsystems en 1995")

print("\n>Python:\n\tEs un lenguaje de programación orientado a objetos de alto nivel y fácil de interpretar con sintaxis fácil de leer")

print("\n>Eficiencia:\n\tEs la facultad de conseguir un resultado optimizando el uso de los recursos.\n\tTambién puede referirse a la realización de un trabajo en un periodo de tiempo más corto")

print("\n>Eficacia:\n\tEs la realización de las cosas correctamente, con el simple propósito de lograr o alcanzar las metas previstas.")

print("\n>Respeto:\n\tEl respeto es un valor y una cualidad positiva que se refiere a la acción de respetar;\n\tes equivalente a tener veneración, aprecio y reconocimiento por una persona o cosa")

print("\nFin del glosario.")
