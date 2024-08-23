import {SudokuSolver, SudokuChecker} from './sudoku_sol.js'
const puzzleBoard = document.getElementById("puzzle");
const solveButton = document.getElementById("solve-button");
const resetButton = document.getElementById("reset-button");
// const solutionDisplay = document.getElementById("solution");
const squares = 81;
const sudoku = [];

for(let i = 0; i < squares; i++){
    const inputElement = document.createElement('input');
    inputElement.setAttribute('type', 'number');
    inputElement.setAttribute('min', 1);
    inputElement.setAttribute('max', 9);

    if(
        ((i%9==0 || i%9==1 || i%9==2) && i<21) ||
        ((i%9==6 || i%9==7 || i%9==8) && i<27) ||
        ((i%9==3 || i%9==4 || i%9==5) && i>27 && i<53) ||
        ((i%9==0 || i%9==1 || i%9==2) && i>53) ||
        ((i%9==6 || i%9==7 || i%9==8) && i>53)
    ){
        inputElement.classList.add('odd-section');
    }

    puzzleBoard.appendChild(inputElement);
}

const joinValues = () => {
    const inputs = document.querySelectorAll('input');
    inputs.forEach(input=>{
        if(input.value){
            sudoku.push(input.value);
        }else{
            sudoku.push('.');
        }
    })
}

const sudokuSolver_func = (data) => {
    let sudoku_array = new Array(9);
    for(let i = 0; i<9; i++){
        sudoku_array[i] = new Array(9);
    }
    for(let i = 0; i<squares; i++){
        sudoku_array[Math.floor(i/9)][i%9] = parseInt(data[i]);
    }

    if(SudokuChecker(sudoku_array)==0) return 'No Solution';

    for(let i = 0; i<9; i++){
        for(let j = 0; j<9; j++){
            SudokuSolver(sudoku_array, 0, 0, 0);
        }
    }
    if(SudokuSolver(sudoku_array, 0, 0, 0)){
        const sudoku_solution = [];
        for(let i = 0; i<9; i++){
            for(let j = 0; j<9; j++){
                sudoku_solution.push(sudoku_array[i][j]);
            }
        }
        return sudoku_solution.join('');
    }else{
        return 'No Solution';
    }
}

const populateValues = (isSolvable, response) => {
    const inputs = document.querySelectorAll('input');
    if(isSolvable){
        inputs.forEach((input, i) => {
            input.value = response[i];
        })
        // console.log(response);
        // solutionDisplay.innerHTML = 'This is the answer';
    }else{
        if(!alert('This is not a valid sudoku.')){
            window.location.reload();
        }
    }
}

const solve = () => {
    joinValues();
    const data = sudoku.join('');
    const solution = sudokuSolver_func(data);
    if(solution != 'No Solution'){
        populateValues(true, solution);
    }else{
        populateValues(false, solution);
    }
}

solveButton.addEventListener('click', solve);
resetButton.addEventListener('click', () => {
    window.location.reload();
});
