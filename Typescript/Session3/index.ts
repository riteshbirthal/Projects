
class Animal{
    // ! mark is used to skip initialiazation
    public name!:string;
    constructor(name:string){
        this.name = name;
    }
    private func(){
        console.log("In private function");
    }
    public move(distance:number = 0){
        console.log(`${this.name} moved ${distance} kms.`);
    }
}

class Dogs extends Animal{
    // default access modifier is public
    Bark(){
        console.log("Checking data distance.");
    }
}

const dog = new Dogs("ABC");
dog.Bark();
dog.move(10);
// dog.func();

// Abstract Class

abstract class Department{
    constructor(public name: string){

    }
    printName():void{
        console.log(this.name);
    }
}

class AccountingDept extends Department{
    constructor(){
        super('Accounting and Auditing');
    }
    printMethod():void{
        console.log("Hello World!");
    }
}
let dept:Department;
dept = new AccountingDept();
dept.printName();

// import and export
import {add} from './add'
console.log(add(3,4));


// generics
function identity<T>(arg:T):T{
    return arg;
}

let out1 = identity<string>("myString");
console.log(out1);


// utility
interface Patient{
    id: number;
    name: string;
    admitCount: number;
}

const p1:Partial<Patient> = {
    id : 1,
    name: "abc"
};

const p2:Required<Patient> = {
    id : 2,
    name : "def",
    admitCount : 10
};

const p3: Readonly<Patient> = {
    id : 1,
    name: "patient 1",
    admitCount: 2
};

// p3.id = 5;

type key = "key1" | "key2" | "key3";

interface Value {
    var1: number;
    var2: string;
    var3: boolean;
}

// all keys are required in Record
const record: Record<key, Value> = {
    key1: {var1 : 1, var2: "hello", var3: true},
    key2: {var1 : 2, var2: "world", var3: true},
    key3: {var1 : 3, var2: "2.0", var3: false},
};

console.log(record.key1)

// pick some selected keys from interface
type pick_type = Pick<Value, "var1" | "var3">;

const pick_var: pick_type = {
    var1: 2,
    var3: true
};
console.log(pick_var);

// to remove keys from an interface and pick all others
type omit_type = Omit<Value, "var1">;

const omit_var: omit_type = {
    var2: "temp",
    var3: true
};
console.log(omit_var);