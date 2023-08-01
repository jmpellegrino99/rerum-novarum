const alphabet = "abcdefghiklmnopqrstuvwxyz";
const key = "death";
let message = "hello there how are you";

// Prepare the message for use in the cipher
message = message.replaceAll(" ","");
if (message.length % 2 !== 0) {
    message += "x";
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

// Split message into two-letter pairs
let pairList = [];
for (let i = 0; i < message.length; i += 2) {
    pairList.push(message.substring(i,i+2));
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

