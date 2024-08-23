//Element Checker Function
function CheckElement(arr, i, j, element){
    //printf("Checking element = %d, for i = %d, j = %d \n",element, i,j);
    let t, p, q;
    //Checking Column Elements
    for (t = 0; t < 9; t++) {
        if (t != i && arr[t][j] == element) {
            return 0;
        }
    }
    //Checking Row Elements
    for (t = 0; t < 9; t++) {
        if (t != j && arr[i][t] == element) {
            return 0;
        }
    }
    //Checking Box 1 Elements
    if (i >= 0 && i < 3 && j >= 0 && j < 3) {
        for (p = 0; p < 3; p++) {
            for (q = 0; q < 3; q++) {
                if ((p != i || q != j) && arr[p][q] == element) {
                    return 0;
                }
            }
        }
    }
    //Checking Box 4 Elements
    else if (i >= 3 && i < 6 && j >= 0 && j < 3) {
        for (p = 3; p < 6; p++) {
            for (q = 0; q < 3; q++) {
                if ((p != i || q != j) && arr[p][q] == element) {
                    return 0;
                }
            }
        }
    }
    //Checking Box 7 Elements
    else if (i >= 6 && i < 9 && j >= 0 && j < 3) {
        for (p = 6; p < 9; p++) {
            for (q = 0; q < 3; q++) {
                if ((p != i || q != j) && arr[p][q] == element) {
                    return 0;
                }
            }
        }
    }
    //Checking Box 2 Elements
    else if (i >= 0 && i < 3 && j >= 3 && j < 6) {
        for (p = 0; p < 3; p++) {
            for (q = 3; q < 6; q++) {
                if ((p != i || q != j) && arr[p][q] == element) {
                    return 0;
                }
            }
        }
    }
    //Checking Box 5 Elements
    else if (i >= 3 && i < 6 && j >= 3 && j < 6) {
        for (p = 3; p < 6; p++) {
            for (q = 3; q < 6; q++) {
                if ((p != i || q != j) && arr[p][q] == element) {
                    return 0;
                }
            }
        }
    }
    //Checking Box 8 Elements
    else if (i >= 6 && i < 9 && j >= 3 && j < 6) {
        for (p = 6; p < 9; p++) {
            for (q = 3; q < 6; q++) {
                if ((p != i || q != j) && arr[p][q] == element) {
                    return 0;
                }
            }
        }
    }
    //Checking Box 3 Elements
    else if (i >= 0 && i < 3 && j >= 6 && j < 9) {
        for (p = 0; p < 3; p++) {
            for (q = 6; q < 9; q++) {
                if ((p != i || q != j) && arr[p][q] == element) {
                    return 0;
                }
            }
        }
    }
    //Checking Box 6 Elements
    else if (i >= 3 && i < 6 && j >= 6 && j < 9) {
        for (p = 3; p < 6; p++) {
            for (q = 6; q < 9; q++) {
                if ((p != i || q != j) && arr[p][q] == element) {
                    return 0;
                }
            }
        }
    }
    //Checking Box 9 Elements
    else if (i >= 6 && i < 9 && j >= 6 && j < 9) {
        for (p = 6; p < 9; p++) {
            for (q = 6; q < 9; q++) {
                if ((p != i || q != j) && arr[p][q] == element) {
                    return 0;
                }
            }
        }
    }

    return 1;
}

function SudokuSolver(arr, i, j, s) {
    if (s == 81) {
        let sum = 0;
        for (let p = 0; p < 9; p++) {
            for (let q = 0; q < 9; q++) {
                if (arr[p][q]) {
                    sum++;
                }
            }
        }
        if (sum != 81) {
            //printf("Returning for sum = %d \n", sum);
            return 0;
        }
        else {
            //printf("Returning for sum = %d \n", sum);
            return 1;
        }
    }
    if (arr[i][j] && j != 8) {
        //   printf("Calling fun for i = %d, j = %d, s = %d \n", i,j+1,s+1);
        return SudokuSolver(arr, i, j + 1, s + 1);
    }
    else if (arr[i][j]) {
        //printf("Calling fun for i = %d, j = %d, s = %d \n", i+1,0,s+1);
        return SudokuSolver(arr, i + 1, 0, s + 1);
    }
    let l;
    for (let p = 1; p < 10; p++) {
        //printf("p = %d \n", p);
        if (CheckElement(arr, i, j, p)) {
            l = 1;
            arr[i][j] = p;
            let t;
            if (j != 8) {
                //printf("Calling fun for i = %d, j = %d, s = %d \n", i,j+1,s+1);
                t = SudokuSolver(arr, i, j + 1, s + 1);
            }
            else {
                //printf("Calling fun for i = %d, j = %d, s = %d \n", i+1,0,s+1);
                t = SudokuSolver(arr, i + 1, 0, s + 1);
            }
            if (!t) {
                l = 0;
                arr[i][j] = 0;
            }
        }
    }
    if (!l)
        return 0;
}

function SudokuChecker(arr){
    for(let i = 0; i<9; i++){
        for(let j = 0; j<9; j++){
            if(CheckElement(arr, i, j, arr[i][j])==0)
                return 0;
        }
    }
    return 1;
}

export {SudokuSolver, SudokuChecker};