from sqlalchemy.orm import Session

from app.models import Riddle


def default_riddles(db: Session):
    if db.query(Riddle).first() is not None:
        return

    default_riddles = [
        {"question": "¿Qué es algo que no se puede ver, pero siempre está contigo?", "solution": "Sombra",
         "category": "General"},
        {"question": "Cuanto más grande, menos se ve. ¿Qué es?", "solution": "Oscuridad", "category": "General"},
        {"question": "Tiene dientes pero no muerde. ¿Qué es?", "solution": "Peine", "category": "General"},
        {"question": "Vuelo sin alas, lloro sin ojos. ¿Qué soy?", "solution": "Nube", "category": "General"},
        {"question": "Si me nombras, desapareceré. ¿Qué soy?", "solution": "Silencio", "category": "General"},
        {
            "question": "Tiene ciudades, pero no casas; tiene montañas, pero no árboles; tiene agua, pero no peces. ¿Qué es?",
            "solution": "Mapa", "category": "General"},
        {"question": "Estoy lleno de agujeros, pero puedo contener agua. ¿Qué soy?", "solution": "Esponja",
         "category": "General"},
        {"question": "¿Qué tiene un ojo, pero no puede ver?", "solution": "Aguja", "category": "General"},
        {"question": "Me puedes romper sin tocarme. ¿Qué soy?", "solution": "Promesa", "category": "General"},
        {"question": "No habla, pero siempre responde cuando se le llama. ¿Qué es?", "solution": "Eco",
         "category": "General"},
        {"question": "Tiene llave pero no cerradura, tiene espacio pero no habitación. ¿Qué es?", "solution": "Teclado",
         "category": "General"},
        {"question": "¿Qué cosa cuanto más le quitas, más grande se vuelve?", "solution": "Agujero",
         "category": "General"},
        {"question": "Largo, largo, y sin patas; corre, corre, y sin pies. ¿Qué es?", "solution": "Agua",
         "category": "General"},
        {"question": "Tiene agujas pero no pincha. ¿Qué es?", "solution": "Reloj", "category": "General"},
        {"question": "Cuanto más se lava, más sucio se vuelve. ¿Qué es?", "solution": "Agua", "category": "General"},
        {"question": "No se puede ver, no se puede tocar, pero te sigue a todas partes. ¿Qué es?", "solution": "Sombra",
         "category": "General"},
        {"question": "Tiene corona, pero no es rey; tiene escamas, pero no es pez. ¿Qué es?", "solution": "Piña",
         "category": "General"},
        {
            "question": "Soy ligero como una pluma, pero ni el hombre más fuerte puede sostenerme por mucho tiempo. ¿Qué soy?",
            "solution": "Respiración", "category": "General"},
        {"question": "Cien hermanos viven en una casa, pero ninguno se ve. ¿Qué es?", "solution": "Un centenar",
         "category": "General"},
        {"question": "¿Qué es lo que mientras más se seca, más se moja?", "solution": "Toalla", "category": "General"},
        {"question": "Tiene orejas, pero no puede oír. ¿Qué es?", "solution": "Maíz", "category": "General"},
        {"question": "Me llenan de agua y me quitan la tapa. ¿Qué soy?", "solution": "Taza", "category": "General"},
        {"question": "¿Qué se rompe al nombrarlo?", "solution": "El silencio", "category": "General"},
        {"question": "¿Qué es lo que tiene un corazón que no late?", "solution": "Una alcachofa",
         "category": "General"},
        {"question": "¿Qué se quiebra al caer, pero nunca se rompe?", "solution": "La noche", "category": "General"},
        {"question": "Sin moverme, puedo viajar por el mundo. ¿Qué soy?", "solution": "Una carta",
         "category": "General"},
        {"question": "Vuelo sin alas, lloro sin ojos. ¿Qué soy?", "solution": "Nube", "category": "General"},
        {"question": "¿Qué tiene un pie pero no camina?", "solution": "La regla", "category": "General"},
        {"question": "¿Qué es lo que sube y nunca baja?", "solution": "La edad", "category": "General"},
        {"question": "Tiene muchos dientes pero no muerde. ¿Qué es?", "solution": "Peine", "category": "General"},
        {
            "question": "Si cinco máquinas hacen cinco artículos en cinco minutos, ¿cuántas máquinas harán cincuenta artículos en cincuenta minutos?",
            "solution": "Cinco", "category": "Matemáticas"}
    ]

    for item in default_riddles:
        riddle = Riddle(
            question=item["question"],
            solution=item["solution"],
            category=item["category"]
        )
        db.add(riddle)
    db.commit()
