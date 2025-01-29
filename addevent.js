// Stockage des événements
let events = {};

// Ajout d'un événement
function addEvent() {
    let date = document.getElementById("eventDate").value;
    let lieu = document.getElementById("eventLieu").value;
    let activite = document.getElementById("eventActivite").value;

    if (!date || !lieu || !activite) {
        alert("Veuillez remplir tous les champs.");
        return;
    }

    if (!events[date]) {
        events[date] = [];
    }

    events[date].push({ lieu, activite });
    displayEvents(date);
}

// Affichage des événements
function displayEvents(dateKey) {
    const eventContainer = document.getElementById("eventList");
    eventContainer.innerHTML = "";
    
    if (events[dateKey]) {
        events[dateKey].forEach((event, index) => {
            let eventItem = document.createElement("div");
            eventItem.innerHTML = `<strong>${event.lieu}</strong> - ${event.activite} 
            <button onclick="deleteEvent('${dateKey}', ${index})">❌</button>`;
            eventContainer.appendChild(eventItem);
        });
    } else {
        eventContainer.innerHTML = "Aucun événement pour cette journée.";
    }
}

// Suppression d'un événement
function deleteEvent(dateKey, index) {
    events[dateKey].splice(index, 1);
    if (events[dateKey].length === 0) delete events[dateKey];
    displayEvents(dateKey);
}

// Sélection d'une date dans le calendrier
for (let i = 0; i < Cases.length; i++) {
    Cases[i].addEventListener("click", function () {
        if (Cases[i].innerText !== "") {
            let selectedDate = `${year}-${String(month).padStart(2, "0")}-${String(Cases[i].innerText).padStart(2, "0")}`;
            displayEvents(selectedDate);
        }
    });
}
