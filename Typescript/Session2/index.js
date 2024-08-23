var strValue = "Hello World";
var num = 10;
var cond = true;
var strArr = ["Hello ", "World ", "2"];
var generic = "hey";
var anything = [1, "2"];
console.log(strValue, num, generic, anything);
var val;
val = "Hello World";
console.log(typeof val, typeof val === "string");
console.log(val.toUpperCase());
val = 10;
console.log(typeof val);
// difference between any and unknown
function func(val) {
    if (typeof val === "string")
        console.log(val.toUpperCase());
    if (typeof val === "number")
        console.log(val.toFixed(2));
}
function func2(val) {
    console.log(val.toUpperCase());
    console.log(val.toFixed(2));
}
// intersection
var variable;
variable = "temp";
variable = 23890;
var variable1;
variable1 = "temp1";
variable1 = 45656;
var logMessage = function (msg) { return console.log(msg); };
logMessage("Hello World...");
