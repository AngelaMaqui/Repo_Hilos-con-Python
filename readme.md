INTERPRETACION DE CADA TARABAJADOR
Se mostro que hubo un cmabion constante entre la ejecuciones realizadas a la vez que ningun trabajador interfirio con otro y a su vez causar un desequilibrio entre documentos resaltando tambien la aleatoriedad de cada docuemnto realizado por trabajador y que ninguno repitio documentos

PREGUNTAS

¿Por qué queue.Queue es apropiada para compartir trabajos?
Por que maneja mecanismos de bloqueo para que los hilos puedan agregar o extraer sin que haya perdidas en pocas palabras para que dos trabajadores no hagan el mismo documento al mismo tiempo.
¿Qué protege Lock y qué pasaría si se actualizara el resumen sin él?
el lock es el que protege el diccionario compartido,si se actualizara el resumen sin el tendriamos que dos hilos intenten realizar un documentoal mismo tiempo y esto mismo causaria perdida de docuemntos o que falaten documentos por hacer.
¿Qué cambiarías si cada documento tuviera que guardarse en un archivo real?
Cambiaria el time.sleep() por open() o write() esto para guardar el contenido en disco.
