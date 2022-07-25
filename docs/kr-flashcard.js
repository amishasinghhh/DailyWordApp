/**
 * Sample JavaScript code for sheets.spreadsheets.values.get
 * See instructions for running APIs Explorer code samples locally:
 * https://developers.google.com/explorer-help/code-samples#javascript
 */
    function loadClient() {
    gapi.client.setApiKey("AIzaSyA7yuO-d3GkigRjUD4v8ZU7cjeVIuk-Rns");
    return gapi.client.load("https://sheets.googleapis.com/$discovery/rest?version=v4")
        .then(function() { console.log("GAPI client loaded for API"); },
            function(err) { console.error("Error loading GAPI client for API", err); });
}

function sp_execute() {
    if (localStorage.getItem('sp_word') != null) {
        window.location = "sp-flashcard.html";
        return;
    }
    num = Math.floor(Math.random() * 4699)
    return gapi.client.sheets.spreadsheets.values.get({
    "spreadsheetId": "1S2ZlZ5GDNzsVigoec0a4i9tYyZiW83SajYAZNR_0ZCU",
    "range": "A" + num + ":D" + num,
    "dateTimeRenderOption": "SERIAL_NUMBER",
    "majorDimension": "ROWS",
    "valueRenderOption": "FORMATTED_VALUE"
    })
        .then(function(response) {
            localStorage.setItem('sp_word', response.result["values"][0][0]);
            localStorage.setItem('sp_pos', response.result["values"][0][1]);
            localStorage.setItem('sp_definition', response.result["values"][0][2]);
            localStorage.setItem('sp_sentence', response.result["values"][0][3]);
            window.location = "sp-flashcard.html";
        },
            function(err) { console.error("Execute error", err); });
}
// Make sure the client is loaded and sign-in is complete before calling this method.
function execute() {
    var kr_counter = localStorage.getItem('kr_counter')
    if (kr_counter === null) {
        kr_counter = 0;
    }
    kr_current_card = localStorage.getItem('kr_current_card')
    console.log(kr_current_card)
    if (kr_current_card === null) {
        kr_current_card = 1;
    } else {
        kr_current_card++;
    }
    localStorage.setItem('kr_current_card', kr_current_card)
    kr_current_card_element = localStorage.getItem(kr_current_card)
    kr_current_card_element = JSON.parse(kr_current_card_element)
    if (kr_current_card_element === null){
        num = Math.floor(Math.random() * 1475)
        return gapi.client.sheets.spreadsheets.values.get({
        "spreadsheetId": "1CzxWzQrFb7bGbDWWLj_v7kWySEBGcS4NZkApCZxyBtM",
        "range": "A" + num + ":D" + num,
        "dateTimeRenderOption": "SERIAL_NUMBER",
        "majorDimension": "ROWS",
        "valueRenderOption": "FORMATTED_VALUE"
        })
            .then(function(response) {
                console.log(response.result["values"][0][0])
                localStorage.setItem('kr_word', response.result["values"][0][0]);
                document.getElementById("word").innerHTML = response.result["values"][0][0];
                localStorage.setItem('kr_pos', response.result["values"][0][1]);
                document.getElementById("partOfSpeech").innerHTML = response.result["values"][0][1];
                localStorage.setItem('kr_definition', response.result["values"][0][2]);
                document.getElementById("definition").innerHTML = response.result["values"][0][2];
                localStorage.setItem('kr_sentence', response.result["values"][0][3]);
                document.getElementById("sentence").innerHTML = response.result["values"][0][3];

                const card = new Object();
                card.kr_word = localStorage.getItem('kr_word')
                card.kr_pos = localStorage.getItem('kr_pos')
                card.kr_definition = localStorage.getItem('kr_definition')
                card.kr_sentence = localStorage.getItem('kr_sentence')

                kr_counter++
                localStorage.setItem("kr_counter", kr_counter)
                localStorage.setItem(kr_counter.toString(), JSON.stringify(card)) 
                },
                function(err) { console.error("Execute error", err); });
    } else {
        // current_card = current_card.toString
        // current_card_element = localStorage.getItem(current_card.toString)
        console.log((kr_current_card_element))
        document.getElementById("word").innerHTML = kr_current_card_element.kr_word
        document.getElementById("partOfSpeech").innerHTML = kr_current_card_element.kr_pos
        document.getElementById("definition").innerHTML = kr_current_card_element.kr_definition
        document.getElementById("sentence").innerHTML = kr_current_card_element.kr_sentence
    }
    
}
gapi.load("client:auth2", function() {
    gapi.auth2.init({client_id: "301275820345-5972hb0n3ci0ndiuhsk50vj0p6qhn4cl.apps.googleusercontent.com", discoveryDocs: ['https://sheets.googleapis.com/$discovery/rest?version=v4'],});
});
window.onload = function() {
    document.getElementById("word").innerHTML = localStorage.getItem('kr_word');
    document.getElementById("partOfSpeech").innerHTML = localStorage.getItem('kr_pos');
    document.getElementById("definition").innerHTML = localStorage.getItem('kr_definition');
    document.getElementById("sentence").innerHTML = localStorage.getItem('kr_sentence');
};

function back() {
    let kr_current_card = localStorage.getItem("kr_current_card")
    kr_card_before = kr_current_card-1
    kr_back_flashcard = localStorage.getItem(kr_card_before)
    kr_back_flashcard = JSON.parse(kr_back_flashcard)
    // let back_flashcard = JSON.parse(localStorage.getItem(card_before.toString));
    document.getElementById("word").innerHTML = kr_back_flashcard.kr_word
    document.getElementById("partOfSpeech").innerHTML = kr_back_flashcard.kr_pos
    document.getElementById("definition").innerHTML = kr_back_flashcard.kr_definition
    document.getElementById("sentence").innerHTML = kr_back_flashcard.kr_sentence
    localStorage.setItem("kr_current_card", kr_card_before)
}