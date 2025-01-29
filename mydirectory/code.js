let Cases = document.getElementsByClassName('case')

let date = new Date();
let year = date.getFullYear();
let month = date.getMonth() + 1;
let day = date.getDate();

const monthName = ["janvier", "février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","décembre"];

const UP_MONTH = 'upMonth'
const DOWN_MONTH = 'downMonth'

function CALENDRIER_REDUCER(action) {
    switch (action) {
        case UP_MONTH:
            if (month < 12) month++
            else {
                year++
                month=1
            }
            break;

        case DOWN_MONTH: 
            if (month > 1) month--
            else {
                year--
                month=12
            }
            break;
        
        default:
            break;
    }
    calendrier(year,month)
}

document.getElementById('avant').onclick = function () {
    CALENDRIER_REDUCER(DOWN_MONTH)
    console.log(month)
}

document.getElementById('apres').onclick = function () {
    CALENDRIER_REDUCER(UP_MONTH)
    console.log(month)
}


function calendrier(year, month) {
    const monthNb = month + 12 * (year - 2020);
    let cld = [{ dayStart: 2, length: 31, year: 2020, month: "janvier" }];

    for (let i = 0; i < monthNb - 1; i++) {
        let yearSimulé = 2020 + Math.floor(i / 12);
        const monthsSimuléLongueur = [
            31, getFévrierLength(yearSimulé), 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31
        ];
        let monthSimuléIndex = (i + 1) - (yearSimulé - 2020) * 12;

        cld[i + 1] = {
            dayStart: (cld[i].dayStart + monthsSimuléLongueur[monthSimuléIndex - 1]) % 7,
            length: monthsSimuléLongueur[monthSimuléIndex],
            year: 2020 + Math.floor((i + 1) / 12),
            month: monthName[monthSimuléIndex]
        };

        if (cld[i + 1].month === undefined) {
            cld[i + 1].month = "janvier";
            cld[i + 1].length = 31;
        }
    }

    for (let i = 0; i < Cases.length; i++) {
        Cases[i].innerText = "";
        Cases[i].classList.remove("today", "selected"); // Réinitialise les styles
    }

    for (let i = 0; i < cld[cld.length - 1].length; i++) {
        let caseIndex = i + cld[cld.length - 1].dayStart;
        Cases[caseIndex].innerText = i + 1;

        // Vérifie si c'est la date actuelle
        if (year === date.getFullYear() && month === date.getMonth() + 1 && (i + 1) === date.getDate()) {
            Cases[caseIndex].classList.add("today"); // Ajoute la surbrillance pour aujourd’hui
        }
    }

    document.getElementById('cldT').innerText =
        cld[cld.length - 1].month.toLocaleUpperCase() + " " + cld[cld.length - 1].year;
}calendrier(year, month);



function getFévrierLength(year) {
    if (year%4 === 0) return 29
    else return 28
}


function updateSelectedDate(selectedCase) {
    // Supprime 'selected' de toutes les cases
    for (let i = 0; i < Cases.length; i++) {
        Cases[i].classList.remove("selected");
    }

    // Ajoute 'selected' à la case cliquée
    selectedCase.classList.add("selected");
}

// Ajoute un événement click à chaque case pour changer la sélection
for (let i = 0; i < Cases.length; i++) {
    Cases[i].addEventListener("click", function () {
        if (Cases[i].innerText !== "") {
            updateSelectedDate(Cases[i]); // Met à jour la sélection
        }
    });
}

// Sélectionne la date du jour au chargement
function selectToday() {
    for (let i = 0; i < Cases.length; i++) {
        if (Cases[i].innerText == day) {
            Cases[i].classList.add("selected"); // Marque la date du jour
        }
    }
}

// Exécute la sélection de la date du jour une fois le calendrier chargé
setTimeout(selectToday, 100);





// Fonction pour afficher les événements sous forme de tableau
function displayEvents(dateKey) {A
    const eventTableBody = document.getElementById("eventContent");
    eventTableBody.innerHTML = ""; // Nettoie le tableau

    if (events[dateKey]) {
        events[dateKey].forEach(event => {
            const row = document.createElement("tr");

            row.innerHTML = `
                <td>${event.date}</td>
                <td>${event.lieu}</td>
                <td>${event.activite}</td>
            `;

            eventTableBody.appendChild(row);
        });
    } else {
        // Aucun événement pour cette journée
        const row = document.createElement("tr");
        row.innerHTML = `<td colspan="3" style="text-align: center;">Aucun événement pour cette journée.</td>`;
        eventTableBody.appendChild(row);
    }
}

// Sélection automatique du jour actuel
function setTodaySelection() {
    for (let i = 0; i < Cases.length; i++) {
        if (Cases[i].innerText == day) {
            Cases[i].classList.add("selected");

            // Formater la date pour la clé d'événements
            const todayFormatted = `${year}-${String(month).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
            displayEvents(todayFormatted);
        }
    }
}


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

// Affichage des événements sans casser le calendrier
function displayEvents(dateKey) {
    const eventListContainer = document.getElementById("eventList");
    eventListContainer.innerHTML = `<h3>Événements du ${dateKey}</h3>`;

    if (events[dateKey]) {
        events[dateKey].forEach((event, index) => {
            let eventItem = document.createElement("div");
            eventItem.innerHTML = `<strong>${event.lieu}</strong> - ${event.activite}
            <button onclick="deleteEvent('${dateKey}', ${index})">❌</button>`;
            eventListContainer.appendChild(eventItem);
        });
    } else {
        eventListContainer.innerHTML += "<p>Aucun événement pour cette journée.</p>";
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




events = {'2025-01-24':[{lieu:'place2',activite:'un autre exemple',freq:'0'}],'2025-01-31':[{lieu:'place2',activite:'un autre exemple',freq:'0'}],'2025-02-07':[{lieu:'place2',activite:'un autre exemple',freq:'0'}],'2025-02-14':[{lieu:'place2',activite:'un autre exemple',freq:'0'}],'2025-01-23':[{lieu:'Place',activite:'un exemple',freq:'1'}],'2025-02-23':[{lieu:'Place',activite:'un exemple',freq:'1'}],'2025-03-23':[{lieu:'Place',activite:'un exemple',freq:'1'}],'2025-04-23':[{lieu:'Place',activite:'un exemple',freq:'1'}],'2025-01-26':[{lieu:'place2',activite:'exemple3',freq:'2'}],'2025-02-26':[{lieu:'place2',activite:'exemple3',freq:'2'}],'2025-03-26':[{lieu:'place2',activite:'exemple3',freq:'2'}],'2025-04-26':[{lieu:'place2',activite:'exemple3',freq:'2'}],}