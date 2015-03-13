var readline = require('readline');

var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

var between = function(low, high) {
    var guess = Math.floor((low + high) / 2);
    rl.question(guess.toString() + "\n", function (answer) {
        if (answer === '=') {
            rl.write("Your number is " + guess.toString() + "!  Thanks for playing.\n");
            rl.close();
        } else if (answer === '>') {
            between(guess, high);
        } else if (answer === '<') {
            between(low, guess);
        } else {
            between (low, high);
        }
    });
};

rl.write('Think of a number between 0 and 100.\n');
rl.write("Don't tell me what it is.\n");
rl.write("When I guess a number, answer me by typing = if I've guessed your number,> if your number is greater, or < if your number is less than my guess\n");

between(0,101);
