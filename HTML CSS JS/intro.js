// arrow function
console.log('Arrow function');

const fun = () => {
    console.log('Arrow function executed.');
}

fun();

// template literals

let temp_lit = "World!";
let temp_sent = `Hello ${temp_lit}`;
console.log("template literals: ", temp_sent, "\n");

// property
console.log("length is property,.... length of temp_lit variable is: ", temp_lit.length, "\n");

console.log("Upper Case: ", temp_lit.toUpperCase(), "\n");

console.log("Lower Case: ", temp_lit.toLowerCase(), "\n");

console.log("slice function for word World! .... slice(2,5): ", temp_lit.slice(2,5), "\n");

console.log("replace function for World! word... replacing Wor to Mo: ", temp_lit.replace("Wor", "Mo"), "\n");

temp_lit = "This ";

console.log(temp_lit.concat("is an ", "example of ", "concat function."), "\n");

temp_lit = "    ";
temp_lit = temp_lit.trim();
if(temp_lit){
    console.log("This is not null: ", temp_lit, "\n");
}

// Array functions

// join function will join all the elements using a separatorclear
temp_lit = [1,2,3,4,5];
console.log("join method example: ", temp_lit.join(" and "), "\n");

// push, pop, shift, unshift functions
var array_length = temp_lit.push(6);
console.log("push function for [1,2,3,4,5] with element 6: ", temp_lit, "\nnew array length: ", array_length);
var removed_element = temp_lit.pop();
console.log("push function for [1,2,3,4,5,6]: ", temp_lit, "\npoped element: ", removed_element);
removed_element = temp_lit.shift()
console.log("shift function for [1,2,3,4,5]: ", temp_lit, "\nshifted element: ", removed_element);
array_length = temp_lit.unshift(removed_element);
console.log("unshift function for [2,3,4,5] with element 1: ", temp_lit, "\nnew array length: ", array_length, "\n");

//delete function
console.log("array and array length before using delete function...");
console.log("array: ", temp_lit);
console.log("array length: ", temp_lit.length);
delete temp_lit[0];
console.log("array and array length after using delete function on 0th element...\n");
console.log("array: ", temp_lit);
console.log("array length: ", temp_lit.length, "\n");
temp_lit[0] = 1;




// strings are immutable
temp_lit = "Hello";
temp_lit[4] = "O";
console.log("Immutable string example, we have changed o to O in Hello string: ", temp_lit);

// escape sequence character:  two characters which are treated as one character, like \' will be considered as one character '

var temp_var = 'hello\'world';
console.log("escape sequence character example: ", temp_var);

// default parameters
const sum_func = (a=0, b=1) => {
    return a + b;
}

console.log(`default parameters value of sum function: ${sum_func()}`);
console.log(`with parameters value of sum function: ${sum_func(10, 12)}`);

// multi lines strings

console.log(`hello world!\n
        this is multi line string example.\n`);

// destructuring assignment
const person = {fname : 'abc', lname: 'def'}
const {fname, lname} = person;

console.log('destructuring assignment example : ', fname, lname);

var flag = false;
let promise_fun = new Promise(function(resolve, reject){
    if(flag){
        resolve('promise function resolved.');
    }else{
        reject('promise function rejected.');
    }
});

console.log('Promise function calling...')
promise_fun.then(function(){
    console.log('Promise function successfully executed.');
}).catch(function(){
    console.log('Promise function execution failed.');
});

//enhanced objects
var firstname = "hello";
var lastname = "world";
var person_ = {firstname, lastname};
console.log('Enhanced Object Example');
console.log(person_);

//classes
class Person{
    constructor(first_name, last_name){
        this.first_name = first_name;
        this.last_name = last_name;
    }
    name_(){
        console.log(`Name of the Person: ${this.first_name} ${this.last_name}`);
    }
}

const person_1 = new Person("HELLO", "WORLD");
console.log('Classes Example');
person_1.name_();


