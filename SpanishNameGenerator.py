# This is a Spanish name generator
import random


# main(): Runs the main program
def main():
    # Intro Banner
    print("Welcome to the Spanish name generator!")
    input("To generate a name press ENTER")
    again = 'y'  # Variable to start while loop
    # Loop to run and rerun generator
    while again == 'y' or again == 'Y':
        # gender variable determines gender of name generated
        gender = input("Would you like to generate a male or female name? M/F: ")
        # Input validation loop
        while gender not in ['F', 'f', 'M', 'm']:
            gender = input("ERROR. Enter M/F only: ")
        # num_of_names determines num of names to generate
        num_of_names = int(input("How many names would you like your character to have?: "))
        # Input validation loop
        while num_of_names >= 50:
            num_of_names = int(input("Error. Please enter a # less than 50: "))
        # if statements to determine whether to generate a male name or female name
        if gender == 'M' or gender == 'm':
            generate_male_names(num_of_names)  # calls generate_male_names
        if gender == 'F' or gender == 'f':
            generate_female_names(num_of_names)  # calls generate_female_names
        generate_last_names()  # calls generate_last_names
        # again allows user to continue to generate more names
        again = input('Would you like to generate another name? Y/N: ')
        # Input validation loop
        while again not in ['Y', 'y', 'N', 'n']:
            again = input("ERROR. Please enter Y/N only: ")


# generate_male_names(): randomly generates male first names
def generate_male_names(total_names):
    # List of male first names
    first_names = ['Alfredo', 'Antonio', 'Alberto', 'Bernardo', 'Alejandro', 'Pepe', 'Pablo',
                    'Pedro', 'Juan', 'Gustavo', 'Felipe', 'David', 'Gabriel', 'Jose', 'Mario',
                    'Leonardo', 'Joaquin', 'Jesus', 'Hector', 'Javier', 'Jaime', 'Francisco',
                    'Dominico', 'Andres', 'Guillermo', 'Patricio', 'Stefano', 'Carlos', 'Carlitos',
                    'Cristiano', 'Miguel', 'Adolfo', 'Osvaldo', 'Adriano', 'Ricardo', 'Enrique',
                    'Inigo', 'Angel', 'Julio', 'Gregorio', 'Diego', 'Roberto', 'Fernando', 'Bernardo',
                   'Benito', 'Domingo', 'Alfonso', 'Valentino', 'Martin', 'Luis', 'Eduardo', 'Zorro',
                   'Marcos', 'Arturo']
    # for loop to generate & print user specified number of names
    for x in range(0, total_names):
        name = random.choice(first_names)
        print(name, end=' ')


# generate_female_names(): randomly generates female first names
def generate_female_names(total_names):
    # list of female first names
    names = ['Adriana', 'Ariana', 'Angelica', 'Angelina', 'Alicia', 'Juanita', 'Francisca',
             'Hana', 'Herminia', 'Julia', 'Blanca', 'Cecilia', 'Carmen', 'Guadalupe', 'Catarina',
             'Carolina', 'Roberta', 'Susanna', 'Maria', 'Antonia', 'Carla', 'Angela', 'Isabella',
             'Eleanora', 'Ana', 'Rosa', 'Rosita', 'Catalina', 'Elisia', 'Fernanda', 'Isabel',
             'Barbara', 'Selena', 'Olivia', 'Camila', 'Ava', 'Sofia', 'Victoria', 'Valentina',
             'Emilia', 'Lucia', 'Elena', 'Martina', 'Sara', 'Julietta', 'Renata', 'Luciana',
             'Mia', 'Gabriella', 'Maya', 'Liliana', 'Mariana', 'Esmeralda', 'Esperanza', 'Alejandra',
             'Viviana', 'Margarita', 'Josefina', 'Teresa', 'Gloria', 'Patricia', 'Luisa']
    # for loop to generate & print user specified number of names
    for x in range(0, total_names):
        name = random.choice(names)
        print(name, end=' ')


# generate_last_names(): generates one random last name
def generate_last_names():
    # list of last names
    names = ['Fernandez', 'Rodriguez', 'Suarez', 'de Silva', 'de Luna', 'de Oro', 'de Castile',
             'de Sol', 'Montoya', 'de Trujillo', 'Iniguez', 'Iglesias', 'Escuella', 'Francisco',
             'Lopez', 'Diaz', 'Garcia', 'Hernandez', 'Cortes', 'Gonzalez', 'Perez', 'de Leon',
             'Sanchez', 'Martinez', 'Gomez', 'Ramos', 'Ramirez', 'Romero', 'Alonso', 'Ortiz',
             'Delgado', 'Blanco', 'Rivera', 'Chavez', 'Alvarez', 'Rubio', 'Herrera', 'Ortega',
             'Castro', 'Vazquez', 'Torres', 'del Toro', 'Ruiz', 'Mendez', 'Vargas', 'Cruz', 'de la Cruz',
             'Reyes', 'Juarez', 'Castillo', 'Juarez', 'Aguilar', 'Luna', 'Mendoza', 'Salazar', 'Rojas']
    # Generates and prints one last name
    name = random.choice(names)
    print(name)


# Calls main
main()
