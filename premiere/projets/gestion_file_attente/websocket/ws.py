import asyncio
import websockets
import json
from random import randint


# Variables globales
subscribers = set()  # Liste des connexions ws en cours
conn = {}  # Connexion ws assignee pour chaque ticket

ticket = 1  # Numero du ticket actuel
queue = []  # Liste des tickets en attente

counter_nb = 5  # Nombre de guichet
counter = [f"counter_{i}" for i in range(1, counter_nb + 1)]
counter_empty = counter  # Liste des guichets libres
counter_status = {}  # Statut de chaque guichet


# Mettre a jour l'affichage avec les donnees
def update_display(status, queue):
    data = {
        "event_name": "update_display",
        "payload": {
            "status": status,
            "queue": queue
        }
    }
    content = json.dumps(data)

    # Envoyer les donnes a toutes les connexions
    websockets.broadcast(subscribers, content)


# Mettre a jour le ticket
async def ticket_update(ws, ticket, counter):
    data = {
        "event_name": "ticket_update",
        "payload": {
            "ticket_number": ticket,
            "counter": counter
        }
    }
    content = json.dumps(data)

    await ws.send(content)


# Assigner un ticket a un guichet
async def assign(ticket, counter):
    # Mettre le guichet pour ce ticket
    counter_status[counter] = ticket

    # Enlever le guichet des guichets libres
    counter_empty.remove(counter)

    await ticket_update(conn[ticket], ticket, counter)

    # Recuperer un temps au hasard pour la duree du guichet
    time = randint(20, 60)

    print(f"{ticket} assigné à {counter} pendant {time} secondes")

    # Terminer le ticket
    asyncio.get_event_loop().call_later(
        time, lambda: asyncio.ensure_future(finish(counter)))


# Liberer un guichet d'un ticket
async def finish(counter):
    # Enlever le guichet du statut des guichets
    counter_status.pop(counter)

    # Ajouter le guichet aux guichets libres
    counter_empty.append(counter)

    await assign_counter_empty(queue)


# Assigner un guichet libre a un ticket
async def assign_counter_empty(queue):
    # Recuperer la liste des guichets libres
    for counter in counter_empty:
        # Regarder s'il reste des tickets dans la queue
        if len(queue) > 0:
            # Supprimer le premier ticket de la queue, principe FIFO (First Int, First Out)
            ticket = queue.pop(0)

            # Assigner le ticket
            await assign(ticket, counter)

    # Mettre a jour l'affichage
    update_display(counter_status, queue)


# Gestion des requetes au websocket
async def handler(ws):
    global conn, ticket, queue
    current_ticket = None

    try:
        # Ajouter la nouvelle connexion entrante à la liste des connexions en cours
        subscribers.add(ws)

        # Mise à jour de l'affichage avec les donnees
        update_display(counter_status, queue)

        async for msg in ws:
            # Recuperer le contenu de la requete
            content = json.loads(msg)

            # Verification du nom de l'event demander
            if content["event_name"] == "request_ticket":
                # Ajouter la connexion ws en cours au ticket
                current_ticket = ticket
                conn[ticket] = ws

                # Ajouter le ticket dans la queue
                queue.append(ticket)

                # Mettre a jour le ticket
                await ticket_update(ws, ticket, None)

                # Nouveau ticket
                ticket += 1

                await assign_counter_empty(queue)
    finally:
        # Supprimer la connexion de la liste des connexions en cours
        subscribers.remove(ws)

        # Supprimer la connexion du ticket en cours
        if current_ticket:
            del conn[current_ticket]

            if current_ticket in queue:
                queue.remove(current_ticket)


# Serveur websocket
async def main():
    async with websockets.serve(handler, "0.0.0.0", 3000):
        await asyncio.Future()

asyncio.run(main())