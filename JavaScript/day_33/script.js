//ES-6 

//ECMA script - 6   2013  
//let const 
//arrow function
//template literals ``   //string template
//default parameters 
//destructuring 
//spread operator
//modules 


//fuc


// named export 
// default export

// import {msg, say_hi,wish} from "./module.js"
// console.log(msg);
// console.log(say_hi())
// console.log(wish())


//call by value 
//when we access a ele by its value

//call by reference
//when a value/element is accessed by location


// primitive                       non primitive 
// number                             array ,obj 
// Boolean
// string 
// null 
// undefined 


//primitive  single values                multiple values 
//immutable                               mutable 




// let pl_name="javascript"

// let name2=pl_name   //
// pl_name="10"
// pl_name=""

// console.log(name2);


// let num=true 

// let num2=num 
// num=false

// console.log(num2);


// let arr1=[1,2,3]
// let arr2=arr1    //shallow copy
// let arr3=arr2
// arr1.push(4)
// console.log(arr2===arr3)

// console.log([]==[])



// let obj={id:1,name:"harsha"}
// let obj2={...obj}   /// deep copy
// obj.name="madhu"
// console.log(obj2);

// let obj3=obj2
// console.log(obj2,obj3);
// console.log(obj==obj2 && obj2==obj3)
// console.log({}=={});


// call by value:   primitive 
// call by reference :   non primitive datatype

// console.log([1]==[1],""=="");  //false true          true false     

//deep copy 
// spread operator 


// let obj={
//     name:"ravi teja",
//     batch:"35r"
// }
// let obj2=obj   ///shallow copy
// obj2={...obj}  //deep copy

// stringify and parse
// let obj2=JSON.stringify(obj)
// obj2=JSON.parse(obj2)
// obj.name="kalyan"
// console.log(obj2==obj,obj2);


// let obj={
//     name:"ravi teja",
//     batch:"35r"
// }
// let obj2={id:1,city:"hyd"}

// //values entries keys freeze seal assign
// let new_obj={...obj,...obj2}

// console.log(new_obj);


//fake store api 


//rest operator  --->

// function add(...c){  /// rest operator   -- array
//     sum=0
//     if (c.length>0){
//         for(let i=0;i<c.length;i++){
//            sum+= c[i]
//         }
//     }
//     return sum
// }
// console.log(add())



// module in browser
// value 
// reference 
// spread 
// rest 





