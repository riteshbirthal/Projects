let strValue:string = "Hello World";
let num:number = 10;
let cond:boolean = true;
let strArr:string[] = ["Hello ", "World ", "2"];
let generic: unknown = "hey";
let anything: any = [1, "2"];
console.log(strValue, num, generic, anything);

let val:any;
val = "Hello World";

console.log(typeof val, typeof val === "string");
console.log(val.toUpperCase());

val = 10;
console.log(typeof val);

// difference between any and unknown
function func(val:unknown){
    if(typeof val === "string")
        console.log(val.toUpperCase());
    if(typeof val === "number")
        console.log(val.toFixed(2));
}

function func2(val:any){
    console.log(val.toUpperCase());
    console.log(val.toFixed(2));
}


// intersection

let variable : number | string;
variable = "temp";
variable = 23890;
// variable = true;        this is gonna through error


// type alias
type Name = string | number;
let variable1 : Name;

variable1 = "temp1";
variable1 = 45656;
// variable1 = true; 

type Log = (message:string) => void;

const logMessage: Log = (msg) => console.log(msg);

logMessage("Hello World...");
