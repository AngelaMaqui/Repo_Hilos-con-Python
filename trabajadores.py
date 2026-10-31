import threading
import queue
import time
import random

trabajos = queue.Queue()
resultados = {}
lock = threading.Lock()

# Cargar 24 documentos en la cola 
for doc_id in range(1, 25):
    trabajos.put((doc_id, random.randint(1, 5)))

# TODO 1: crear la función trabajador(...)
def trabajador(nombre):
    with lock:
        resultados[nombre] = []
    time.sleep(random.uniform(0.01, 0.05))

    # TODO 2: retirar trabajos hasta que la cola este vacia
    for _ in range(6):
        try:
            doc_id, tamano = trabajos.get_nowait()
        except queue.Empty:
            break

        print(nombre, "-> procesando doc", doc_id, "(tamaño:", tamano, ")")

        # TODO 3: simular el procesamiento con time.sleep(...)
        time.sleep(tamano * 0.1)

        # TODO 4: actualizar resultados dentro de lock
        with lock:
            resultados[nombre].append(doc_id)

        print(nombre, "-> finalizó doc", doc_id)

# TODO 5: iniciar 4 hilos y esperar con join()
hilo_angela = threading.Thread(target=trabajador, args=("Angela",))
hilo_maria = threading.Thread(target=trabajador, args=("María",))
hilo_valeria = threading.Thread(target=trabajador, args=("Valeria",))
hilo_fernanda = threading.Thread(target=trabajador, args=("Fernanda",))

hilo_angela.start()
hilo_maria.start()
hilo_valeria.start()
hilo_fernanda.start()

hilo_angela.join()
hilo_maria.join()
hilo_valeria.join()
hilo_fernanda.join()

# TODO 6: mostrar total y resumen por trabajador
total_procesado = sum(len(docs) for docs in resultados.values())

for nombre, docs in resultados.items():
    print(f"{nombre} ({len(docs)} documentos): {docs}")

print("Total de documentos procesados:", total_procesado)