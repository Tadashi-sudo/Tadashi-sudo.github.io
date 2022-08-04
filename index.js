function trun(x) {
    return Math.floor(x * 10 ** 2) / 10 ** 2;
}

function calc(snack, numDrink, drink) {
    var tax = 0.047;
    
    snack = parseFloat(snack);
    numDrink = parseInt(numDrink);
    drink = parseFloat(drink);

    snack += (snack * tax);
    drink += (drink * tax) + (0.06 * numDrink);
    total = snack + drink;

    for (let i = 1000; i > 0; i--) {
        cost = trun((1.83 * i) + total);
        if (Number.isInteger(cost)) {
            document.getElementById('output').innerHTML = i + " items for $" + cost;
        }
    }
}