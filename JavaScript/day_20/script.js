// //dom -- task 
// //create product cards only using dom 

// //to make pages dynamic  

// getelement  
// create 
// append() 
// remove -->element itself 
// parent.removeChild(child)

// styling 
// element.style.

// attributes 
// set 
// get 
// remove


// let parent=document.getElementById("container") 

// let paragrarphs=document.getElementsByTagName("p")//html collection 

// console.log(parent);
// console.log(paragrarphs);

// //removeChild
// // parent.removeChild(paragrarphs[1]
// //0-1  1 -2
// paragrarphs[0].remove()

// // 
// paragrarphs[0].remove()


//event -->
// pre-release event 
// 100 days event 
// freshers day event


// user actions performed on the web page 
// scroll 
// hover 
// button click 



// js -- it listens for the action 

// event listener 


// mouse events 


// let btn=document.getElementById("clik")

// btn.addEventListener("click",()=>{
//     alert("button is clicked")
//     console.log("button clicked");
    
// })


// let btn2=document.createElement("button")
// btn2.innerText="2nd button"
// document.body.append(btn2)


// btn2.addEventListener("dblclick",function(){
//     console.log("button is double clicked");
// })


// let para=document.getElementsByTagName("p")[0]

// para.addEventListener("mouseover",function(){
//     para.style.color="orange"
// })

// para.addEventListener("mouseout",()=>{
//     para.style.color="green"
// })
// para.addEventListener("mouseleave",()=>{
//     para.style.textDecoration="underline"
// })


// mouseover , mouseenter 
// mouseout, mouseleave



// document.addEventListener("keydown",(e)=>{
   
//     console.log("short cut for copy");
// })

// document.addEventListener("keyup",(event)=>{
//     console.log(event.key)
// })



// mouse 
// keyboard 
//form events 

//to collect data 

// let user_form =document.getElementsByTagName("form")[0]
// console.log(user_form);

// user_form.addEventListener("submit",(e)=>{
//     e.preventDefault()
//     // alert("form submitted")
//     console.log("form submitted");  
// })


// let inp=document.getElementById("username")

// let btn=document.getElementById("btn")
// btn.addEventListener("click",()=>{
//     console.log(inp.value)
// })

// inp.addEventListener("change",()=>{
//     console.log("value changed");
    
// })

// inp.addEventListener("focus",()=>{
//     inp.style.backgroundColor="orange"
// })

// let email_ele=document.getElementById("email")
// email_ele.addEventListener("blur",()=>{
//     email_ele.style.backgroundColor="gray"
// })


// submit 

//inputs
// change
// focus 
// blur


// input.value 


// num1 -- input
// num2 -- input  
// add


// onchange()
// onsubmit 
// onclick 
// prevent default