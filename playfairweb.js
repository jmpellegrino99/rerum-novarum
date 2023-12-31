const encrypt = 1;
const key = "death";
let message = "this is my first playfair cipher";
const alphabet = "abcdefghiklmnopqrstuvwxyz"; 

// Convert the message to lowercase
message = message.toLowerCase();

// Prepare the message for use in the cipher
message = message.replaceAll("j", "i");
message = message.replaceAll(" ", "");
if (message.length % 2 !== 0) {
    message += "x";
}

// Split message into two-letter pairs
let pairList = [];
for (let i = 0; i < message.length; i += 2) {
    pairList.push(message.substring(i,i+2));
}

// If a pair is the same letter twice, change the second to "x"
for (let i = 0; i < pairList.length; i++) {
    const first = pairList[i][0];
    const second = pairList[i][1];
    if (first === second) {
        pairList[i] = first + "x";
    }
}

// Arrange the letters in the order they will appear in the grid
let letters = key;
for (let i = 0; i < alphabet.length; i++) {
    if (!key.includes(alphabet[i])) {
        letters += alphabet[i];
    }
}

// Function to create a blank NxN matrix
function createBlankMatrix(rows, cols) {
    const matrix = [];
    for (let i = 0; i < rows; i++) {
        matrix.push(new Array(cols).fill(""));
    }
    return matrix;
}

// Create a 5x5 blank matrix
const matrix = createBlankMatrix(5, 5);

// Populate the matrix with letters
for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
        matrix[i][j] = letters[5*i + j];
    }
}

// Find the index of a letter in a grid
function index(letter) {
    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 5; j++) {
            if (letter === matrix[i][j]) {
                return {row: i, col: j};
            }
        }
    }
}

function swap(l1, l2) {
    const r1 = index(l1).row;
    const r2 = index(l2).row;
    const c1 = index(l1).col;
    const c2 = index(l2).col;
    if (r1 === r2) {
        return matrix[r1][(((c1+encrypt)%5)+5)%5] + matrix[r2][(((c2+encrypt)%5)+5)%5];
    }
    if (c1 === c2) {
        return matrix[(((r1+encrypt)%5)+5)%5][c1] + matrix[(((r2+encrypt)%5)+5)%5][c2];
    }
    else {
        return matrix[r1][c2] + matrix[r2][c1];
    }
}

let resultPairList = [];
for (let i = 0; i < pairList.length; i++) {
    const first = pairList[i][0];
    const second = pairList[i][1];
    const swapFirstSecond = swap(first, second);
    resultPairList.push(swapFirstSecond);
}

function finalReturn() {
const newMessage = resultPairList.join("");
return(newMessage)
}

console.log(key);
console.log(matrix);
console.log(message);
console.log(pairList);
console.log(resultPairList);
console.log(finalReturn());