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
function kr_execute() {
    if (localStorage.getItem('kr_word') != null) {
        window.location = "kr-flashcard.html";
        return;
    }
    num = Math.floor(Math.random() * 1475)
    return gapi.client.sheets.spreadsheets.values.get({
    "spreadsheetId": "1CzxWzQrFb7bGbDWWLj_v7kWySEBGcS4NZkApCZxyBtM",
    "range": "A" + num + ":D" + num,
    "dateTimeRenderOption": "SERIAL_NUMBER",
    "majorDimension": "ROWS",
    "valueRenderOption": "FORMATTED_VALUE"
    })
        .then(function(response) {
            localStorage.setItem('kr_word', response.result["values"][0][0]);
            localStorage.setItem('kr_pos', response.result["values"][0][1]);
            localStorage.setItem('kr_definition', response.result["values"][0][2]);
            localStorage.setItem('kr_sentence', response.result["values"][0][3]);
            window.location = "kr-flashcard.html";
        },
            function(err) { console.error("Execute error", err); });
}
// Make sure the client is loaded and sign-in is complete before calling this method.
function execute() {
    var sp_counter = localStorage.getItem('sp_counter')
    if (sp_counter === null) {
        sp_counter = 5000;
    }
    sp_current_card = localStorage.getItem('sp_current_card')
    console.log(sp_current_card)
    if (sp_current_card === null) {
        sp_current_card = 5001;
    } else {
        sp_current_card++;
    }
    localStorage.setItem('sp_current_card', sp_current_card)
    sp_current_card_element = localStorage.getItem(sp_current_card)
    sp_current_card_element = JSON.parse(sp_current_card_element)
    console.log(sp_current_card_element)
    if (sp_current_card_element === null) {
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
                document.getElementById("word").innerHTML = response.result["values"][0][0];
                localStorage.setItem('sp_pos', response.result["values"][0][1]);
                document.getElementById("partOfSpeech").innerHTML = response.result["values"][0][1];
                localStorage.setItem('sp_definition', response.result["values"][0][2]);
                document.getElementById("definition").innerHTML = response.result["values"][0][2];
                localStorage.setItem('sp_sentence', response.result["values"][0][3]);
                document.getElementById("sentence").innerHTML = response.result["values"][0][3];

                const card = new Object();
                card.sp_word = localStorage.getItem('sp_word')
                card.sp_pos = localStorage.getItem('sp_pos')
                card.sp_definition = localStorage.getItem('sp_definition')
                card.sp_sentence = localStorage.getItem('sp_sentence')

                sp_counter++
                localStorage.setItem("sp_counter", sp_counter)
                localStorage.setItem(sp_counter.toString(), JSON.stringify(card)) 
                },
                function(err) { console.error("Execute error", err); });
    } else {
        console.log((sp_current_card_element))
        document.getElementById("word").innerHTML = sp_current_card_element.sp_word
        document.getElementById("partOfSpeech").innerHTML = sp_current_card_element.sp_pos
        document.getElementById("definition").innerHTML = sp_current_card_element.sp_definition
        document.getElementById("sentence").innerHTML = sp_current_card_element.sp_sentence
    }

}
gapi.load("client:auth2", function() {
    gapi.auth2.init({client_id: "301275820345-5972hb0n3ci0ndiuhsk50vj0p6qhn4cl.apps.googleusercontent.com", discoveryDocs: ['https://sheets.googleapis.com/$discovery/rest?version=v4'],});
});
window.onload = function() {
    document.getElementById("word").innerHTML = localStorage.getItem('sp_word');
    document.getElementById("partOfSpeech").innerHTML = localStorage.getItem('sp_pos');
    document.getElementById("definition").innerHTML = localStorage.getItem('sp_definition');
    document.getElementById("sentence").innerHTML = localStorage.getItem('sp_sentence');
};

function back() {
    let sp_current_card = localStorage.getItem("sp_current_card")
    sp_card_before = sp_current_card-1
    console.log(sp_card_before)
    sp_back_flashcard = localStorage.getItem(sp_card_before)
    console.log(localStorage.getItem(sp_card_before))
    sp_back_flashcard = JSON.parse(sp_back_flashcard)
    console.log(sp_back_flashcard)
    // let back_flashcard = JSON.parse(localStorage.getItem(card_before.toString));
    document.getElementById("word").innerHTML = sp_back_flashcard.sp_word
    document.getElementById("partOfSpeech").innerHTML = sp_back_flashcard.sp_pos
    document.getElementById("definition").innerHTML = sp_back_flashcard.sp_definition
    document.getElementById("sentence").innerHTML = sp_back_flashcard.sp_sentence
    localStorage.setItem("sp_current_card", sp_card_before)
}