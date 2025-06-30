// //lexical scope 
// //enclosed 
// function outer(){
// let variable="hello"
// function inner(){
//      console.log(variable +" mani")
// }

// }

// global scope 

// local scope  
// -->function scope 
// -->block scope


// closure 



// function something(){
//     var username="js_user"
// } 
// something()

// console.log(username)

// if(true){
// const greeting="good morning"
// }
// console.log(greeting)




// dom 
//bom + storage +browser
//events + propogation
// 



//server  + 





// presentation
//application + datalayer





//Application Programming Interface



//to communicate with the server




///url  -->  www.https://  domain .com /

//api



//fetch(url/api/endpoint)
// let products

// fetch("https://fakestoreapi.com/products").then(data=>data.json()).then(dat=>console.log(dat)).catch((err)=>console.log(err))




// fetch(url)
// .then( data => data.json())  .then(d=>console.log(d))
// .catch((err)=> console.log(err))


// debugger
let id=prompt("enter a prod id(1- 20): ")
// fetch("https://fakestoreapi.com/products/21").then(data=>data.json()).then(d=>console.log(d)).catch(err=>console.log(err))
let products
console.log("before API")
fetch(`https://fakestoreapi.com/products`).then(abc=>abc.json()).then(xyz=>products=xyz) //500ms
setTimeout(()=>{
    console.log(products," after api")
},2000) //2000 ms


// async






// get :   --> to get the data (  default )

// post 

//put 

//patch 

//update 

//delete 

// C R U D

// fetch("",)


// user_id :
// fetch a product

// fetch().then(resizeBy.json()).then(console).catch(err=>console)