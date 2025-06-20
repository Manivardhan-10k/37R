//function 

//it is a reusable block of code with specific functionality 

//named arrow  anonymous IIFE 


// const fun=  ()=>{ }

// function fun2(){}
// fun2()

// let fun3=function(){}

// console.log(fun)
// console.log(fun2)
// console.log(fun3)

// (function(){
//     console.log("hi")
// }
// )()



//parameters 
//arguments  -->should be real 



//call backs 

//using  a function inside another function 

// function fun1(param){
//     console.log("good morning")
//     param()
// }
// function fun2(){
//     console.log("good afternoon");
// }
// fun1(fun2)// arguments
//fun2  -->callback function
//fun1 --> higher order function (HOF) 



// reg  -> login ->data

// let username="user"
// let password="secret"

//each function should return a value
//function should have a single return
// sync   one after other
// debugger
// function login(id,pass){
//     if(id=="username" && pass=="secret"){
//        return true
//     }
//     else{
//         return false
//     }
// }

// function show_data(u,p){
//     let secret_msg="keep it secret"
//     if (login(u,p)){
//         console.log(secret_msg)
//     }else{
//         console.log("pls login first");
//     }
// }
// show_data(username,password)


//hoisting 
//variable declarations are moved to the top 
// //function declarations
// debugger
// function add(f,s,fun){
//     return   fun(f+s)
// }
// console.log(add(3,-7,e_o));
// function e_o(n){//7
//     if(n%2==0){
//         return "even"
//     }else{
//         return "odd"
//     }
// }


//array methods, string methods 
//map
//filter 
//forEach 
//reduce
//reduce right

//index , element 

//map is used to iterate over the array and it returns new array with updated values
// let arr=["prabhas","praveen","pradeep","sampoornesh"]

// let updated_arr=arr.map((value,index,array)=>{
//     return "hello "+value
// })
// console.log(updated_arr);


// let updated_price=price_arr.map(function(v,i,a){
    //     return 25+v
    // })
    // console.log(updated_price);
    // console.log(price_arr);
    
    // let val=price_arr.map(function(a,b){//value index 
    //     if (a%2==0){
        
    //         return a
    //     }
    
    // })
    // console.log(val);
    
    
    
// let price_arr=[250,153,200,101,500]//275,175,225,125,525
//  let filterd_arr=   price_arr.filter(function(x,y,z){
//         return x>150 && x<300
//     })
// console.log(filterd_arr);


// let arr=["prabhas","praveen","pradeep","sampoornesh"]

// let updated_arr=arr.filter((val)=>{
//     return val.startsWith("p")
// })

// console.log(updated_arr);



// let arr=["mango","kiwi","apple","pineapple"]
// let new_arr=[]
// arr.forEach((v,i)=>{
//    new_arr.push( v.toUpperCase())
// })
// console.log(new_arr);


//map ,filter -->new array 
//forEach


//3 params value index array 
//used for iteration 






//reducing --combinig all the values into a single value 



// let arr=[1,2,3,4,5,6,7,8,9,10]  //55

// let sum=arr.reduceRight((p,c,i,a)=>{
//     console.log(p,c)
// return p*c
// },1)

// console.log(sum);



// let arr=[1,10,100,20,200,3,4,5,6,8,9000,100000]
// let sorted=arr.sort((a,b)=>b-a)
// console.log(sorted);
// console.log(arr);


let names=["manivardhan","thamanna","trisha","ileana"]
console.log(names.sort())


