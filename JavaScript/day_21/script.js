//events

//user actions 


//types 

//mouse
// click  dblclick  mouseover  mouseout    mousemove


//keyboard 
//keydown keyup  keypress(deprecated)


//form
//submit   change  focus  blur  


//window



// document.addEventListener("mousemove",()=>{
//     document.body.style.backgroundColor="gray"
// })


// let count=0
// document.addEventListener("keydown",function(){
//     console.log(count)
//     count++
// })



//submit 
//change 

// let inp_ele=document.getElementById("user_input")
let para=document.getElementById("inp") 


// let names=["kalyan","ramesh","suresh"]

// inp_ele.addEventListener("change",()=>{
//  let found=false
//     names.forEach((val)=>{
//         if(val.startsWith(inp_ele.value.toLowerCase())){
//             para.innerText=val
//             found=true
//         }
//     })
//    if(found==false){
//     para.innerText="no matching names"
//    }

// })



//window events 
// alert 
// prompt 
// confirm 
// window.alert("hello")

// let val=window.confirm("r u sure??")
// console.log(val);




// load 
// debugger;
// window.addEventListener("load",function(e){
// para.innerText="page loaded" 
// })

//resize 

// window.addEventListener("resize",function(){
//     console.log("you are disqualified");
//     alert("disqualified")
    
// })


//scroll 
// window.addEventListener("scroll",()=>{
//     console.log("you have scrolled");
    
// })


// function handleClick(){
//     console.log("button clicked");
    
// }

// Btn.addEventListener("event", ()=>{})



//setTimeout 
//setinterval 


// setTimeout(()=>{
//     console.log("times up");
//     alert("stop writing")
// },5000)

// let count=1
// setInterval(function(){
//     console.log("give medicine ",count)
//     count++

// },10000)



// let user_time=prompt("enter the time in hrs: ")
// let milli_seconds=user_time*60*60*1000

// let rem=setInterval(function(){
//     // alert("drink water")
//     // confirm("have u drunk?")
//     console.log("drink water")

// },1000)


// setTimeout(()=>{
//     clearInterval(rem)
// },5000)

