document.addEventListener("DOMContentLoaded", function () {
    async function fetchWords() {
        try {
            const response = await fetch("words.txt");
            const text = await response.text();
            return text.split(/\r?\n/).map(word => word.trim()).filter(word => word.length > 0);
        } catch (error) {
            console.error("Error loading words.txt:", error);
            return [];
        }
    }

    async function solvePuzzle() {
        const mainLetter = document.getElementById("mainLetter").value.trim().toLowerCase();
        const includeLetters = document.getElementById("includeLetters").value.trim().toLowerCase();

        if (!mainLetter) {
            alert("Please enter a main letter.");
            return;
        }

        const allLetters = new Set(includeLetters + mainLetter); // Allowed letters
        const words = await fetchWords(); // Fetch words from file
        const wordList = document.getElementById("wordList");
        wordList.innerHTML = ""; // Clear previous results

        const filteredWords = words.filter(word => {
            word = word.toLowerCase();
            return (
                word.includes(mainLetter) && // Must contain the main letter
                word.length >= 4 && // At least 4 letters long
                [...word].every(letter => allLetters.has(letter)) // No excluded letters
            );
        });

        if (filteredWords.length === 0) {
            wordList.innerHTML = "<li>No words found.</li>";
        } else {
            filteredWords.forEach(word => {
                const li = document.createElement("li");
                li.textContent = word;
                wordList.appendChild(li);
            });
        }
    }

    window.solvePuzzle = solvePuzzle; // Expose function to global scope for button onclick
});
