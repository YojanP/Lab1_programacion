#Librería para generar los valores aleatorios
from random import choice

#Función para eliminar una pregunta de las listas de preguntas
def remove_question(question, entertaiment_questions, sports_questions):
    #Verifica si la pregunta está en la lista de entretenimiento
    if question in entertaiment_questions:
        #Si está en la lista, la elimina
        entertaiment_questions.remove(question)
    #Verifica si la pregunta está en la lista de deportes
    elif question in sports_questions:
        #Si está en la lista, la elimina
        sports_questions.remove(question)

#Función para las preguntas, opciones de respuesta y respuesta correcta de la categoría entretenimiento
def entertaiment():
    # Lista de preguntas que contiene diccionarios.
    # Cada diccionario tiene:
    # - 'question': La pregunta formulada.
    # - 'answers': Lista de opciones de respuesta.
    # - 'correct': La clave de la respuesta correcta. 
    questions = [
        {
        "question": "Cuál es el nombre del ratón más famoso de Disney?",
        "answers": ["A. Tom","B. Jerry", "C. Mickey", "D. Stuart"],
        "correct":"C"
        },
        {
        "question":"¿Cómo se llama el mejor amigo de Shrek?",
        "answers":["A. Pinocho", "B. El gato con botas", "C. Burro", "D. Lord Farquaad"],
        "correct": "C"
        },
        {
            "question": "¿Qué personaje de dibujos animados vive en una piña debajo del mar?",
            "answers": ["A. Patricio", "B. Calamardo", "C. Don Cangrejo", "D. Bob Esponja"],
            "correct": "D"
        },
        {
            "question":"¿Cuál es el héroe que tiene una armadura roja y dorada?",
            "answers": ["A. Hulk","B. Iron Man", "C. Capitán América", "D. Thor"],
            "correct": "B"
        },
        {
            "question": "¿En qué pelicula hay un animal obsesionado con una nuez?",
            "answers": ["A. Friends", "B. Star Wars", "C. El libro de la vida", "D. La era de hielo"],
            "correct": "D"
        },
        {
            "question": "¿Cómo se llama el villano principal en 'Los Vengadores: Infinity War'?",
            "answers": ["A. Loki", "B. Ultron", "C. Thanos", "D. Ronan"],
            "correct": "C"
        },
        {
            "question": "¿Cuál de las siguientes peliculas está insparada en hechos reales?",
            "answers":["A. Son como niños", "B. Titanic", "C. Stuart Little", "D. Iron Man"],
            "correct": "B"
        },
        {
            "question": "¿Cómo se llama el cantante más grande del vallenato colombiano?",
            "answers": ["A. Diomedes Díaz", "B. Silvestre Dangon", "C. Kaleth Morales", "D. Rafael Orozco"],
            "correct": "A"
        },
        {
            "question": "¿Qué pelicula de Pixar cuenta la historia de una familia de superhéroes?",
            "answers": ["A. Ratatouille", "B. Los Increíbles", "C. Cars", "D. Coco"],
            "correct": "B"
        },
        {
            "question": "En qué ciudad vive Batman?",
            "answers":["A. Metrópolis", "B. Nueva York", "C. Santadilla", "D. Ciudad Gótica"],
            "correct":"D"
        }
    ]
    return questions

#Función para las preguntas, opciones de respuesta y respuesta correcta de la categoría deportes
def sports():
    # Lista de preguntas que contiene diccionarios.
    # Cada diccionario tiene:
    # - 'question': La pregunta formulada.
    # - 'answers': Lista de opciones de respuesta.
    # - 'correct': La clave de la respuesta correcta. 
    questions = [
        {
            "question": "¿En qué país se originó el fútbol?",
            "answers": ["A. Brasil", "B. Inglaterra", "C. Alemania", "D. Argentina"],
            "correct": "B"
        },
        {
            "question": "¿Cuántos jugadores conforman un equipo de baloncesto en la cancha?",
            "answers": ["A. 5", "B. 6", "C. 7", "D. 8"],
            "correct": "A"
        },
        {
            "question": "¿Quién ha ganado más títulos de Grand Slam en tenis masculino?",
            "answers": ["A. Roger Federer", "B. Rafael Nadal", "C. Novak Djokovic", "D. Pete Sampras"],
            "correct": "C"
        },
        {
            "question": "¿Cuántos anillos de la NBA tiene Michael Jordan?",
            "answers": ["A. 4", "B. 5", "C. 6", "D. 7"],
            "correct": "C"
        },
        {
            "question": "¿En qué deporte se utiliza una pelota ovalada?",
            "answers": ["A. Rugby", "B. Balonmano", "C. Fútbol Americano", "D. A y C son correctas"],
            "correct": "D"
        },
        {
            "question": "¿Quién ganó la Copa Mundial de Fútbol de la FIFA en 2018?",
            "answers": ["A. Brasil", "B. Francia", "C. Alemania", "D. Argentina"],
            "correct": "B"
        },
        {
            "question": "¿Qué selección de fútbol ha ganado más Copas del Mundo?",
            "answers": ["A. Argentina", "B. Italia", "C. Brasil", "D. Alemania"],
            "correct": "C"
        },
        {
            "question": "¿En qué país se celebraron los Juegos Olímpicos de 2021?",
            "answers": ["A. China", "B. Japón", "C. Francia", "D. Estados Unidos"],
            "correct": "B"
        },
        {
            "question": "¿Qué equipo de fútbol tiene más títulos de la UEFA Champions League?",
            "answers": ["A. Barcelona", "B. Bayern Múnich", "C. Manchester United", "D. Real Madrid"],
            "correct": "D"
        },
        {
            "question": "¿Quién es conocido como 'El Fenómeno' en el fútbol?",
            "answers": ["A. Lionel Messi", "B. Cristiano Ronaldo", "C. Ronaldo Nazário", "D. Ronaldinho"],
            "correct": "C"
        }
    ]
    return questions

# Función principal creada para los requerimientos del laboratorio
def main():
    #Da la bienvenida y las categorías de preguntas del juego
    print("Bienvenido, este videojuego contiene dos categorías de preguntas: Entretenimiento y Deportes")
    user = input("Ingresa tu nombre: ") #Se pide el nombre al usuario 
    
    cant_questions = 0 #Cantidad de preguntas respondidas
    correct_answers = 0  #Cantidad de preguntas correctas
    incorrect_answers = 0 # de preguntas incorrectas
    entertaiment_questions = entertaiment() #Carga la lista de preguntas de la categoría entretenimiento
    sports_questions = sports() #Carga la lista de preguntas de la categoría deportes
    all_questions = entertaiment()+sports() #Carga la cantidad de preguntas totales

    # Bucle para mostrar las preguntas y opciones de respuesta
    while cant_questions < (len(all_questions)):
        category = choice(["entertaiment", "sports"])  # Selecciona una pregunta aleatoria de todas las categorías
        
        if category == "entertaiment":
            aleatory_question = choice(entertaiment_questions)
        elif category == "sports":
            aleatory_question = choice(sports_questions)
        
        print("\n" + aleatory_question["question"])  # Muestra la pregunta

        for answer in aleatory_question["answers"]:
            print(answer)  # Muestra las opciones de respuesta

        # Solicita la respuesta del usuario
        user_answer = input("Selecciona tu respuesta (o escribe 'salir' para finalizar): ").upper()  

        if user_answer == "SALIR":  # Condición para salir del juego
            print("\nGracias por jugar")
            break

        elif user_answer == aleatory_question["correct"]:  # Comprueba si la respuesta es correcta
            print("Tu respuesta es correcta")
            correct_answers += 1  # Incrementa el contador de respuestas correctas
            print("Ganaste 60 puntos :D")
            # Elimina la pregunta ya respondida correctamente de la lista
            #remove_question(aleatory_question, entertaiment_questions, sports_questions)  
        else:
            print(f"La respuesta correcta era {aleatory_question['correct']} :(")  # Muestra la respuesta correcta
            print("Perdiste 15 puntos :(")
            incorrect_answers += 1

        remove_question(aleatory_question, entertaiment_questions, sports_questions)
        cant_questions += 1  # Incrementa el contador de respuestas respondidas

    # Calcula la puntuación del usuario
    points = (correct_answers * 60)-(incorrect_answers*15)
    #Muestra la cantidad de aciertos
    print(f"{user}, respondiste correctamente {correct_answers} preguntas de {len(all_questions)}")
    
    if correct_answers == len(all_questions): #Condición para felicitar al usuario si respondió correctamente todas las preguntas
        print("¡Felicidades, contestaste correctamente todas las preguntas!")
    
    if points < 0:
        print(f"Tu puntuación es: 0")  # Muestra la puntuación final
    else: 
        print(f"Tu puntuación es: {points}")  # Muestra la puntuación final

# Llama a la función principal para ejecutar el juego
main()