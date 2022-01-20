from os import system
system ("cls")
import sqlite3

nombre=input("Escribí el nombre del archivo.db: ")
print()
con=sqlite3.connect(nombre+".db")
ciclo_tabla="S"
ciclo_campo="S"
creacion_bd=""
campos=0

while (ciclo_tabla.upper()=="S"):
	cant_pk_ai=0
	campos=0
	creacion_bd=""
	nom_tabla=input("Escribí el nombre de la nueva tabla: ")
	print()
	ciclo_tabla="N"
	ciclo_campo="S"

	while (ciclo_campo.upper()=="S"):
		primary_key=""
		autoincrement=""	
		nom_campo=input("Escribí el nombre del nuevo campo: ")
		print()
		tipo_campo=int(input("""Escribí el tipo de dato del nuevo campo
		1 → TEXT
		2 → INTEGER
		3 → REAL
		Otro → BLOB

		"""))
		print()
		if tipo_campo==1:
			nom_tipo_campo=" TEXT "
		elif tipo_campo==2:
			nom_tipo_campo=" INTEGER "
		elif tipo_campo==3:
			nom_tipo_campo=" REAL "
		else:
			nom_tipo_campo=" BLOB "

		if cant_pk_ai==0:
			clave_si_no=input("¿Querés que sea un campo clave? (S/N): ")
			print()

			if clave_si_no.upper()=="S":
				cant_pk_ai+=1
				primary_key="PRIMARY KEY "
				if tipo_campo==2:
					autoinc_si_no=input("¿Querés que sea un campo autoincremental? (S/N): ")
					print()
					if autoinc_si_no.upper()=="S":
						cant_pk_ai+=1
						autoincrement="autoincrement "
					else:
						autoincrement=""
				else:
					autoincrement=""
			else:
				primary_key=""
				autoincrement=""

		ciclo_campo=input("¿Querés crear un nuevo campo dentro de esta tabla? (S/N): ")
		print()

		creacion_bd1=str("CREATE TABLE IF NOT EXISTS ")
		creacion_bd2=str(nom_tabla)
		creacion_bd3=str(" (")
		creacion_bd4=str(nom_campo)
		creacion_bd5=str(nom_tipo_campo)
		creacion_bd6=str(primary_key)
		creacion_bd7=str(autoincrement)
		creacion_bd8=str("not null")
		if ciclo_campo.upper()=="S":
			creacion_bd9=str(",\n")
		else:
			creacion_bd9=str(")")

		if campos==0:
			creacion_bd=creacion_bd+creacion_bd1+creacion_bd2+creacion_bd3+creacion_bd4+creacion_bd5+creacion_bd6+creacion_bd7+creacion_bd8+creacion_bd9
		else:
			creacion_bd=creacion_bd+creacion_bd4+creacion_bd5+creacion_bd6+creacion_bd7+creacion_bd8+creacion_bd9
		campos+=1

		if ciclo_campo.upper()!="S":
			cur=con.cursor()
			cur.execute(creacion_bd)
			con.commit()
			lista=cur.fetchall()			
			ciclo_tabla=input("¿Querés crear una nueva tabla? (S/N): ")
			print()
con.close()
