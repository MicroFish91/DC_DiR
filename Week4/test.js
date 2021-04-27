var readline = require('readline');

var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Enter player name? ", function(answer) {
    console.log("Player name:", answer);
    rl.pause();
});