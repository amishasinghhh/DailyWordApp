    /**
     * Sample JavaScript code for sheets.spreadsheets.values.get
     * See instructions for running APIs Explorer code samples locally:
     * https://developers.google.com/explorer-help/code-samples#javascript
     */
     function kr_execute() {
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
        window.location = "kr-flashcard.html"
        console.log(window.location)
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
                window.location = "kr-flashcard.html" 

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
    }
    function loadClient() {
        gapi.client.setApiKey("AIzaSyA7yuO-d3GkigRjUD4v8ZU7cjeVIuk-Rns");
        return gapi.client.load("https://sheets.googleapis.com/$discovery/rest?version=v4")
            .then(function() { console.log("GAPI client loaded for API"); },
                function(err) { console.error("Error loading GAPI client for API", err); });
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
                window.location = "sp-flashcard.html" 

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
    }
    gapi.load("client:auth2", function() {
        gapi.auth2.init({client_id: "301275820345-5972hb0n3ci0ndiuhsk50vj0p6qhn4cl.apps.googleusercontent.com", discoveryDocs: ['https://sheets.googleapis.com/$discovery/rest?version=v4'],});
    });