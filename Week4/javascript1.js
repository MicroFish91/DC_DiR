function decipher(phrase,offset){
    phrase = phrase.toLowerCase();
    var letters = "abcdefghijklmnopqrstuvwxyz";
    var phraseDecrypt ="";
    var n="";
    for(var i = 0; i < phrase.length; i++){
        if(phrase[i].toLowerCase() != phrase[i].toUpperCase()){
            console.log((letters.indexOf(phrase[i]) - offset) % 26);
            n = letters[(letters.indexOf(phrase[i]) - offset) % 26];
        }
        else{
            n = phrase[i];
        }
        phraseDecrypt = phraseDecrypt.concat(n);
    }
    console.log(phraseDecrypt)
}

decipher('Travhf jvgubhg rqhpngvba vf yvxr fvyire va gur zvar', 13);