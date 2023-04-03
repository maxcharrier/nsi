/**
 * Met à jour l'affichage avec les nouvelles données
 * @param {Object} data - Donnée de l'affichage
 */
function updateDisplay(data) {
    html = '<div id="wrapper">\n';

    // Recuperer la liste des status puis pour chaque guichet
    html += Object.keys(data.status).map((counter) => {
        // Recuperer le ticket assigne
        let ticket = data.status[counter];

        content = '<div class="ticket">\n';
        content += '\t<p class="name">Ticket</p>\n';
        content += `\t<p class="num">${ticket}</p>\n`;
        content += '\t<p class="name">Guichet</p>\n';
        content += `\t<p class="num">${counter.split("_")[1]}</p>\n`;
        content += "</div>\n"

        return content;
    }).join("");

    html += "</div>"

    // Mettre le nombre de ticket en attente
    html += `<p id="waiting">Ticket(s) en attente: <span>${data.queue.length}</span></p>`;

    document.getElementById("container").innerHTML = html;
}

/**
 * Créer un WebSocket avec un url définie et les événements de base
 * @param {String} url - Url du WebSocket
 */
function createWs(url) {
    let ws = new WebSocket(url);

    // Event des qu'un message est recu
    ws.addEventListener("message", (event) => {
        // Recuperer le contenu des donnees de l'event
        let content = JSON.parse(event.data);

        // Mettre a jour l'affichage
        if (content.event_name === "update_display") {
            updateDisplay(content.payload);
        }
    });

    // Gestion des erreurs
    ws.addEventListener("error", (err) => {
        console.log(err);

        createWs(url);
    });
}

let url = "wss://localhost";
createWs(url);