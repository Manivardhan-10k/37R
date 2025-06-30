//event propogation

// 1.trickling phase /capturing phase
// 2. bubbling phase -- we can control

// stoppropogation

// same Element multiple event

// stop immediate propogation

// addEventListener(else,false,)

// Scope:
// debugger;
// var   a
// let  b
// const c=10

// global scope

// var greet="hello"

// console.log(greet);

// let greet2="good afternoon"
// console.log(greet2);

// local scope
//   function scope

// function outer(){
//     var a=10
//     console.log(a)

//     let b=20
//     const c="hello"
//     console.log(b)
// console.log(c)
// //  return a
// }
// outer()
// console.log(a)
// console.log(b)
// console.log(c)

// block scope
//

// { ----block----}
// {
//     let greet="hello"
//     const greet2="hi"
// }
// //outside the block
// // console.log(greet)
// console.log(greet2)

// function scope      block
//   var
//   let                let
//   const              const

// var u_name="shiva"

// function say_hi(){
//     u_name="pradeep"
//     console.log("hello "+u_name)
// }
// say_hi()

let name="ramesh"
function outer(){//parent function
    let name="shravan"

    function inner(){// child function
        // let name="kushal"
        console.log(name)
    }
    inner()

}
// outer()

// closure:
// debugger
// function outer(){ // higher order function
//     let lang="js"
//     function inner(){
//         console.log(lang);
//     }
//     return inner
// }

// let fun=outer()

// fun()

// function account() {
//   let amount = 10000;
//   function add_money(val) {
//     amount += val;
//     console.log(amount);
// }
// let child1="child1"
//   function debit_money(val) {
//     console.log(child1)
//     if (amount - val < 0) {
//       console.log("insufficient balance");
//     } else {
//       amount -= val;
//       console.log(amount);
//     }
//   }
//   return debit_money;
// }
// let acc = account();
// acc(10000);




// let a=10 
// function add(){

//     a++

// }
// console.log(a)
// add()
// console.log(a)88
// G E F


// lexical -- provides the access 

// closure --> remembers the values for further use