// Object. 

// keys 
// values 
// entries 
// assign 
// seal 
// freeze 
 
// issealed 
// isfrozen

// let obj={
//     key:"value",
//     name:"mani"
// }
// console.log(obj.key) 

// for (let iterator in obj){
//     console.log(obj[iterator])
// }




// DOM --Document Object Model

// html --structure (static page)

// css -- styling 

// js-- dynamic web pages 

// console.log(document) 
//getElementById()

// console.log(document.getElementById("head1"))
// let head1=document.getElementById("head1")//html element 

//innerText 
//innerHtml
//textContent 
// console.log( head1.innerText);
// head1.innerText="this is modified from js"



// function change_name(){
//     let userName=prompt("enter the username: ") 
//     let element=document.getElementById("head1")
//     console.log(element)
//     element.innerHTML= `welcome <i><u> ${userName} </u></i>`  // welcome + userName
// }
// change_name()



// let container=document.getElementById("container")
// console.log(container);
// // container.innerText="new text"

// console.log(container.innerText)
// console.log(container.innerHTML) 
// console.log(container.textContent) 


// #id 
// .class 
//tagname  p{} 

// let list=document.getElementsByClassName("item")
//multiple values in a collection 
//collection is accessed by using index

// console.log(list.length);
// let element=list[0]
// element.innerText=   element.innerText.toUpperCase()

// let last_ele=list[list.length-1] 
// console.log(last_ele);
// last_ele.innerText= last_ele.innerText.toUpperCase()

//id 
//class --- collection -- index 
//tagname  --collection --index

// let tags=document.getElementsByTagName("li")
// console.log(tags);
// for(let i =0;i<tags.length;i++){
//     if(i%2!==0){
//         let ele=tags[i]
//         ele.innerText= ele.innerText.toUpperCase()
//     }
// }











