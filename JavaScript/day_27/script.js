//event propogation 


// flow of event from outer most to innermost Element /target element


//trickling/capturing phase 


//bubbling phase 


let child= document.getElementById("child")
child.addEventListener("click",(event)=>{
    console.log("child called");
    // event.stopPropagation()
    // event.stopImmediatePropagation()
    
},)

let parent= document.getElementById("parent")
parent.addEventListener("click",(e)=>{
    console.log("parent called");
    // e.stopPropagation()
    
})
let  grand= document.getElementById("grand")
grand.addEventListener("click",(e)=>{
    console.log("grand called");
    // e.stopPropagation()
})


// child.addEventListener("mouseover",(event)=>{
//     console.log("child called event 2");
//     event.stopPropagation()
    
// })
// child.addEventListener("mouseout",(event)=>{
//     console.log("child called event 3");
//     event.stopPropagation()
// })

//stop Immediate propogation 
// it is used to stop multiple events for same element


