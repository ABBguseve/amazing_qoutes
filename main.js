function readTextFile() { //Funktion som läser av texten i text documentet där quoten ligger
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", "dailyquote.txt", true);
    rawFile.onreadystatechange = function() {
      if (rawFile.readyState === 4) { //Kollar om det finns något att läsa av i dokumentet
        var allText = rawFile.responseText;
        document.getElementById("dailyQuote").innerHTML = allText;
        console.log(allText)
      }
      else{
        document.getElementById("dailyQuote").innerHTML = "Unable to load Quote";
        console.log("unable to load quote")
      }
    }
    rawFile.send(); 
  }

function cereateQuote(){ //Funktion till gröna knappen för att scrolla ner till infosidan
  var cqp = document.getElementById("createQuotepage");
  cqp.scrollIntoView();
}

function dailyQuote(){ //Funktion för pilknappen på infosidan för att scrolla upp igen
  var dqp = document.getElementById("dailyQuotepage");
  dqp.scrollIntoView();
}

readTextFile() //Kär funktionen för att läsa in quoten

