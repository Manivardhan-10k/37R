// Dom 

// Document web pages  

// .html 

//dynamic content creation  

// console.log( document );

//getElementById()
// document.

// let ele=document.getElementById("h6")

//  ele.innerHTML="welcome to the <u><i><b>DOM</b></i></u> class" 

// let caption=document.createElement("p")
// caption.innerText="make webpages dynamic"

// document.body.append(caption)

// {
//     font-weight:800
// }
 
// let paragraph=document.getElementsByTagName("p")[0]
// let userColor=prompt("enter the color: ")
// let con=confirm("are u sure?")
// paragraph.style.fontSize="150px"
// paragraph.style.color= con?userColor:"black"
// paragraph.style.backgroundColor="yellow"
// paragraph.style.textDecoration="underline"
// paragraph.style.border="5px solid black"



// let names=["kalyan","harsha","shiva","sudheer","shakar","mahendar","vinay","chandini","mani vardhan","brahmi"]

// let names_list=document.createElement("ul")
// //forEach map filter reduce reduceRight
// names.forEach(function(v,i,a){
//     let name_item=document.createElement("li")
//     name_item.innerText=v
//     names_list.append(name_item)
// })
// names_list.style.listStyle="none"
// document.body.append(names_list)



// let students=[{name:"kalyan",marks:500},{name:"shiva",marks:520,},{name:"vinay",marks:499},{name:"raju",marks:475}]
// let stu_list=document.createElement("ol")
// students.forEach((v,i,a)=>{
//     let stu_item=document.createElement("li")
//     stu_item.innerText=v.name 
//     v.marks>500?stu_item.style.color="green":""
//     stu_list.append(stu_item) 
// })
// document.body.append(stu_list)


let heros=["prabhas","dhanush","salman khan","karthee","nani"]
let heroines=["samantha","sai pallavi","anushka","katrina","shradda"]


//     prabahs-samantha 
//    |
//    |
//    |
//    nani -shradda
// 1 -1 
// 2 -2 
// 3 -3

// n -n

let pair_list=document.createElement("ol")
for(let i=0;i<heros.length;i++){
    let pair=document.createElement("li") 
    pair.innerText=`${heros[i]}- ${heroines[i]}`
    pair_list.append(pair)
}
document.body.append(pair_list)