 #!/usr/bin/python
 # -*- coding: utf-8 -*-

#Esta clase sirve para manipular los ficheros AIML:
#	- Buscar un patron : exist_pattern() [ok]
#	- Añadir nuevo conocimiento : insert_pattern() [ok]
#	- Borrar conocimiento: delete_pattern() [*]
#	- Duplicar un archivo AIML : duplicate_brain() [*]

class aiml_manipulator:
	file=''
	isOpen=False #Nos indica si el archivo AIML esta abierto (1) o cerrado (0)
	isModified=False #Este atributo nos indica que se ha modificado el fichero AIML
	name_file=''

	def __init__(self,name_file):
		self.name_file=name_file
		self.isOpen=False #El archivo no ha sido abierto
		self.isModified=False

	def open_aiml(self,mode):
		self.isOpen=True
		self.file=open(self.name_file,mode)
		self.isModified=False

	def close_aiml(self):
		self.isOpen=False;
		self.file.close();

	def exist_pattern(self,pattern):
		#This function find a pattern and if this pattern exist return True else return False
		if(self.isOpen==True):
			#The file is open
			for line in self.file:
				counter=len(line.split(pattern))-1
				if(counter!=0):
					#Exist the pattern
					return True
				else:
					pass

			return False
		else:
			#The file is close, in this moment open the file
			self.open_aiml('r') #Open for read
			return Exist_Pattern(pattern)

	def insert_pattern(self,pattern,respost):
		#Esta funcion inserta un nuevo patron en el archivo aiml

		if(self.isOpen==True):
			#El archivo esta abierto
			variable_aiml=self.file.read() #leemos todo el fichero

			text1="\n<category> \n"
			text2="<pattern>"+pattern+"</pattern>\n"
			text3="<template>"+respost+"</template>\n"
			text4="</category>\n"
			text_final=text1+text2+text3+text4
			palabra="</aiml>"
			text_final=text_final+palabra

			variable_aiml=variable_aiml.replace(palabra,text_final) #Remplazamos el texto
			self.file.close()
			self.file=open(self.name_file,'w') #Borraremos el contenido que tenga el fichero
			self.file.write(variable_aiml)
			self.isModified=True
			
		else:
			print("[*] - The file is closed, open the file first")

	def duplicate_brain(self):
		#Esta funcion devuelve un objeto manipulador que es copia del self
		iter=self; #Creo que tengo que hacer el constructor de copia luego me lo miro con calma
		return iter;