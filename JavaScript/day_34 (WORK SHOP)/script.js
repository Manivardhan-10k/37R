// take the input from user

//send the input to the server

//DOM BOM  event listener json-server(fetch)
// onclick
//ele ->addeventlistener

//get post put/patch delete
//truthsy values falsy values

const handleRegister = () => {
  let username = document.getElementById("username").value;
  let password = document.getElementsByTagName("input")[1].value;
  let mobile = document.getElementsByClassName("mobile")[0].value;
  let email = document.getElementById("email").value;


  // console.log(username,password,mobile,email);
  let mob_exists=window.localStorage.getItem("reg_mobiles")
  mob_exists=JSON.parse(mob_exists)
  if(mob_exists && mob_exists.includes(mobile)){
    alert("user already exists with same mobile number")
  }else{
    // console.log("users not found");
    
  let details = {
    id: mobile,
    username: username,
    mobile: mobile,
    password: password,
    email: email,
  };


  fetch("http://localhost:3000/users", {
    method: "POST",
    headers: { "Content-Type": "Application/json" },
    //payload
    body: JSON.stringify(details),
  })
    .then((res) => res.json())
    .then(() => {
      let reg_mob = window.localStorage.getItem("reg_mobiles");
      if( !reg_mob){
        reg_mob=[]
        reg_mob.push(mobile)
        window.localStorage.setItem("reg_mobiles", JSON.stringify(reg_mob));
      }
      else{
      reg_mob=JSON.parse(reg_mob) //string -array 
      reg_mob.push(mobile); //new mobile added
      window.localStorage.setItem("reg_mobiles", JSON.stringify(reg_mob)); //setting again in storage
      }
      location.assign("./success.html");
    })
    .catch((err) => {
      location.assign("./err.html");
    });
};
}

function getusers() {
  let userslist = [];
  fetch("http://localhost:3000/users")
    .then((res) => res.json())
    .then((data) => (userslist = data))
    .catch((err) => console.log(err));
  console.log("fetch called");

  setTimeout(() => {
    userslist.forEach((val) => {
      let username = document.createElement("h1");
      username.innerText = val.username;
      let email = document.createElement("h5");
      email.innerText = val.email;
      let line = document.createElement("hr");
      document.body.append(username, email, line);
    });
  }, 3000);
  }