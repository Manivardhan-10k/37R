//string 

//collection of characters enclosed in '' or "" or `` 

// let language="javascript"

// language[0]="J"
// console.log(language);


//primitive
//string boolean number null undefined  
//they store only single values 
//they are immutable 


// language="Javascript"

//method -->  a predefined function 


// console.log()  //pre defined function 

//string methods 
// using these methods  we can manipulate the strings 


// console.log(username.length)
// console.log("madhu kiran".length);




// let username=prompt("enter the username: ") 



//length-1 
// let last_index=username.length-1
// console.log(last_index);

// console.log(username[last_index]);


// let username="abcdefghijklm"
// //char At 
// console.log(username[115]); 

//charCodeAt 
//ASCII --American Standard Code for Information Interchange


// console.log(username.charCodeAt(2)) 

//At 

// console.log(username.at(0)); 


//slice 


// console.log(username.slice(-4,-1))

//if we give a sinlge parameter it will the starting index  


// console.log(username.substring(0,4))

// console.log(username.substr(0,10))


//

// let input=prompt("enter the heading: ")

// input=input.toUpperCase()
// console.log(input);
// input=input.toLowerCase()
// console.log(input);




// let username=prompt("enter the name: ")

// username=username.trim()

// console.log(username.length);
// console.log(username==="mani vardhan")



// let username="mamatha mohan das" 
// console.log(username.padStart(10,"*"))
// console.log(username.padEnd(100," "))

// console.log(username.replace("m","M"))
//it replaces the first matching value
// console.log(username)

//replaceAll 
// console.log(username.replaceAll("m","M"));





// console.log(username.split(" ").join("-"));  

//indexof --> ifrst matching index
// console.log(username.indexOf("b"));


//lastindexof  -->last matching index
// console.log(username.lastIndexOf("b"));


// console.log(username.search("an"));


// console.log(username.includes("an"))

// -1

// let username="mamatha mohan das"
// if(username.search("m")){
//         console.log(true)
//     }else{
//             console.log(false);
        
//         }
// if(username.includes("an")){  //false
//     console.log(true)
// }else{
//     console.log(false); 
// }


// console.log(username.startsWith("mam"))
// console.log(username.endsWith("as"))




// console.log(`my name is ${username}`);




let username="madhu kumar ,laxman kumar , surya kiran "

console.log(username.replace("ma",""))











