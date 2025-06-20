// functions 

// callback function

// map 
// filter  
// forEach 
// reduce 
// reduceRight 
// sort()  -->comaparative function 
// 1 10 100 2 3 4 5 1000 22  
//ascending order 1 2 3 4  5 10 22 100 1000 
//1 10 100 1000 2 22 3 4  5



// register --> otp 

// login  -->otp 

// password change --> otp 

// forgot password --> otp 



// function otp_generate(){
//     let otp="1267"
//    return  otp

// }
// otp_generate()



// function register(ot_password,gen){

//     if (gen()==ot_password){
//         console.log("registration successful");
        
//     }

// }


// const login=(ot_password,gen)=>{
//     if(gen()==ot_password){
//         console.log("login successful");
        
//     }
    
// }

// register(1267,otp_generate)///otp_generate is callback  ,,   register is hof
// login(1267,otp_generate)






// function sum(a,b){  //--> +
//     return a+b
// }

// function  sub(a,b){/// --> -

//     return a-b
// }


// function arthemetic(a,b,o){

//     if(o=="+"){
//        return  sum(a,b)  //8
//     }
//     if(o=="-"){
//        return sub(a,b)
//     }
// }
// console.log(arthemetic(5,3,"-"))


// Object 

//data type  -->non primitive 

//collection 



// let languages=[{lan:"tel",read:"yes",write:"yes",speak:"yes"},"hindi","english"]


// console.log(person["name"])
// console.log(person.city);
// arr[ind]=value

// person.name="manivardhan"
// console.log(person);

// person.employed=true
// person.salary="not sufficient"

// delete person.salary
// console.log(person);

//keys
//values
//entries
//assign
//seal
//freeze

//string.method(params)
// array.method(params)
//keys 
let person={
    age:25,
    city:"hyd",
    name:"mani"
}
// person.employed=true
// console.log(Object.keys(person).length)

// console.log(Object.values(person).length); 


// console.log(Object.entries(person).length)



// console.log(Object.assign(marks,person))

// console.log(person)
// console.log(marks)


//seal 
// debugger
// let marks={
//     m1:"fail",
//     p1:90,
//     c1:85
// }
// Object.seal(marks)

// marks.c1=90
// marks.m2=75

// console.log(marks.m2)

// console.log(Object.isSealed(marks))




// let account={
//     ac_no:1232456,
//     ifsc:"aab2356",
//     holder:"vikas",
//     branch:"kphb"
// }
// account.status="active"

// Object.seal(account)


// account.status="inactive"
// account.j_d="09-06-2025"
// delete account.status

// console.log(account)
// console.log(Object.isFrozen(account))
// console.log(Object.isSealed(account))




// seal --> update // yes      insert//no
// freeze --> update/no    insert/no



// let account={
//     ac_no:1232456,
//     ifsc:"aab2356",
//     holder:"vikas",
//     branch:"kphb",
//     address:{
//         dr_no:50,
//         street:"bank st"
//     }
// }


// console.log(account.address.dr_no);

// for ( const i in account){
//     console.log(i,account[i])
// }

// object oriented syntax 




//find the factorial 

// 7 
// 


// for (let i=7;i>=1;i--){
//     fact=fact*i  //1*7  7*6*5*4*3*2*1
// }
// console.log(fact)

//recursion 

//a function calling itself
// debugger
// let num=7 
// function factorial(n){
//     if (n==1){
//         return 1
//     }
//     return n*factorial(n-1)// 7*factorial(6*factorial(5*factorial(4*factorial(3*factorial(2*factorial(1))))))
// }
// console.log(factorial(num))


