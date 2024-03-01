<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tiles Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .tile {
            width: 100px;
            height: 100px;
            background-color: #ccc;
            border: 1px solid #000;
            display: inline-block;
            margin: 5px;
            text-align: center;
            line-height: 100px;
            font-size: 24px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div id="container">
        <!-- Tiles will be dynamically generated here -->
    </div>
    <script>
        const container = document.getElementById('container');
        const tiles = [];
        const gridSize = 4; // Change this to adjust grid size
        // Function to create tiles
        function createTiles() {
            for (let i = 1; i <= gridSize * gridSize; i++) {
                const tile = document.createElement('div');
                tile.classList.add('tile');
                tile.textContent = i;
                tile.addEventListener('click', () => {
                    if (checkMove(i)) {
                        swapTiles(i);
                        checkWin();
                    }
                });
                tiles.push(tile);
                container.appendChild(tile);
            }
        }
        // Function to check if a move is valid
        function checkMove(number) {
            const emptyIndex = tiles.findIndex(tile => tile.textContent === '');
            const numberIndex = tiles.findIndex(tile => tile.textContent == number.toString());
            const rowDiff = Math.abs(Math.floor(emptyIndex / gridSize) - Math.floor(numberIndex / gridSize));
            const colDiff = Math.abs((emptyIndex % gridSize) - (numberIndex % gridSize));
            return (rowDiff == 1 && colDiff == 0) || (colDiff == 1 && rowDiff == 0);
        }
        // Function to swap tiles
        function swapTiles(number) {
            const emptyIndex = tiles.findIndex(tile => tile.textContent === '');
            const numberIndex = tiles.findIndex(tile => tile.textContent == number.toString());
            const temp = tiles[emptyIndex];
            tiles[emptyIndex] = tiles[numberIndex];
            tiles[numberIndex] = temp;
            redrawTiles();
        }
        // Function to redraw tiles after a swap
        function redrawTiles() {
            container.innerHTML = '';
            tiles.forEach(tile => container.appendChild(tile));
        }
        // Function to check if the player has won
        function checkWin() {
            const correctOrder = Array.from({ length: gridSize * gridSize - 1 }, (_, i) => (i + 1).toString());
            const currentOrder = tiles.map(tile => tile.textContent).slice(0, -1);
            if (JSON.stringify(correctOrder) === JSON.stringify(currentOrder)) {
                alert('Congratulations! You won!');
            }
        }

        // Initialize the game
        createTiles();
    </script>
</body>
</html>
