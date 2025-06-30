// webstorages


// webstorage: name:"mani"


//webstorages are not shared between users 
//scripting  language


//programming language -- runtime environment 

// internal storage -- opearating system





// sessionStorage :

//data is saved untill the tab is closed 

// window.sessionStorage.setItem("name","manivardhan")
// console.log(window.sessionStorage.getItem("name"))

// let fav_food=["biryani","milk sweet","dosa"]

// window.sessionStorage.setItem("fav_foods",JSON.stringify(fav_food))


// //JSON  --> text format



// console.log(JSON.parse(window.sessionStorage.getItem("fav_foods"))[0])







// localStorage:




// window.localStorage.setItem("username","javascript_user")

// console.log(window.localStorage.getItem("username"));

// window.localStorage.setItem("username","manivardhan")

// window.localStorage.removeItem("username")
//CRUD  
//setItem(k,v)
//getItem(k)
//setItem(existingkey)
//removeItem(k)


//5-10mb 



//cookies
//small piece of info
//kb 



// request + cookies -->





// event propogation -->flow,



// const handleDiv=()=>{
//     console.log("div is called")
// }

// function handleClick(){
//     console.log("button is clicked")
// }

let gp=document.getElementById("grandparent")
gp.addEventListener("click",()=>{
    console.log("this is grand parent")
})


gp.style.height="200px"
gp.style.width="200px"
gp.style.border="2px solid red"

let parent=document.getElementById("parent")
parent.addEventListener("click",function(e){
    console.log(e)
console.log("this is parent");
e.stopPropagation()
parent.style.backgroundColor="green"

})


parent.style.height="150px"
parent.style.width="150px"
parent.style.border="2px solid yellow"
let child=document.getElementById("child")
child.addEventListener("click",(event)=>{
    console.log("this is child");
    event.stopPropagation()
},)


child.style.height="100px"
child.style.width="100px"
child.style.border="2px solid green"



//trickling phase 



//bubbling phase
// const handleGGP=()=>{
//     console.log("GGP")
// }



// trickling       /// capturing phase
// top ->bottom


// bubbling phase
// bottom -> top

// event --> we should get it as  a parameter of callback 
// event.stopPropagation()



