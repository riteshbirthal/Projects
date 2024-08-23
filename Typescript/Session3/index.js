"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
var Animal = /** @class */ (function () {
    function Animal(name) {
        this.name = name;
    }
    Animal.prototype.func = function () {
        console.log("In private function");
    };
    Animal.prototype.move = function (distance) {
        if (distance === void 0) { distance = 0; }
        console.log("".concat(this.name, " moved ").concat(distance, " kms."));
    };
    return Animal;
}());
var Dogs = /** @class */ (function (_super) {
    __extends(Dogs, _super);
    function Dogs() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    // default access modifier is public
    Dogs.prototype.Bark = function () {
        console.log("Checking data distance.");
    };
    return Dogs;
}(Animal));
var dog = new Dogs("ABC");
dog.Bark();
dog.move(10);
// dog.func();
// Abstract Class
var Department = /** @class */ (function () {
    function Department(name) {
        this.name = name;
    }
    Department.prototype.printName = function () {
        console.log(this.name);
    };
    return Department;
}());
var AccountingDept = /** @class */ (function (_super) {
    __extends(AccountingDept, _super);
    function AccountingDept() {
        return _super.call(this, 'Accounting and Auditing') || this;
    }
    AccountingDept.prototype.printMethod = function () {
        console.log("Hello World!");
    };
    return AccountingDept;
}(Department));
var dept;
dept = new AccountingDept();
dept.printName();
// import and export
var add_1 = require("./add");
console.log((0, add_1.add)(3, 4));
// generics
function identity(arg) {
    return arg;
}
var out1 = identity("myString");
console.log(out1);
var p1 = {
    id: 1,
    name: "abc"
};
var p2 = {
    id: 2,
    name: "def",
    admitCount: 10
};
var p3 = {
    id: 1,
    name: "patient 1",
    admitCount: 2
};
// all keys are required in Record
var record = {
    key1: { var1: 1, var2: "hello", var3: true },
    key2: { var1: 2, var2: "world", var3: true },
    key3: { var1: 3, var2: "2.0", var3: false },
};
console.log(record.key1);
var pick_var = {
    var1: 2,
    var3: true
};
console.log(pick_var);
