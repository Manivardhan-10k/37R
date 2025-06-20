//register 
//save the user
//login 
// homepage 
//    links 
//    google amazon youtube instagram



//register code 


const handleLoad=()=>{
    location.assign("http://127.0.0.1:5500/register.html")



}

let handleRegister=()=>{
let username=document.getElementById("username").value
let mob=document.getElementById("mob").value
let password=document.getElementById("password").value
let confirm_password=document.getElementById("confirm_password").value
// console.log(username,mob,password,confirm_password);
let user_details={
    name:username,
    mobile:mob,
    password:password
}
let users=window.localStorage.getItem("users")
users=JSON.parse(users)
users.push(user_details)
//JSON 
user_details=JSON.stringify(users)
// console.log(typeof(user_details));
//setting data in local storage 
if(password===confirm_password){
window.localStorage.setItem("users",user_details)
alert("user registerd succesfully")
location.assign("http://127.0.0.1:5500/login.html")
}
else{
    alert("passwords do not match");  
}
}



//login code 

//we need to compare the user input with registered data 

function handleLogin(){
    let user_name=document.getElementById("user_name").value
    let user_password=document.getElementById("user_password").value
    // console.log(user_name,user_password);
    let reg_user_list=window.localStorage.getItem("users")
    //stored will be in string form
    // console.log(reg_user.name)
    reg_user_list=JSON.parse(reg_user_list)//converting the string back into object form
    // console.log(reg_user);
   
    let user_found=false
    reg_user_list.forEach((v,i,a)=>{
        if(user_name==v.name && user_password===v.password){
        alert("login successful")
        user_found=true
  
    }
    })
    if (user_found===true){
              location.assign("http://127.0.0.1:5500/homepage.html")
    }else{

        location.assign("http://127.0.0.1:5500/register.html")
    }



}



//JSON 

//javascript object notation 
// data format for imnformation exchange between the system

//text format  --strings

//strings 
//number


// stringify -->object to string form
// parse-->converts string to object
// "01111002221111100041101"