function handleRegister() {
  let username = document.getElementById("username").value;
  let mob = document.getElementById("mob").value;
  let password = document.getElementById("password").value;
  let confirm_password = document.getElementById("confirm_password").value;

  console.log(username, mob, password, confirm_password);
  if (password == confirm_password) {
    new_user = {
      username: username,
      mobile: mob,
      password: password,
    };
    existing_users = window.localStorage.getItem("users");
    if (existing_users) {
      user_array = JSON.parse(existing_users);
      let exists = false;
      user_array.forEach((val) => {
        if (val.mobile == mob) {
          exists = true;
        }
      });
      if (exists == false) {
        user_array.push(new_user);
        converted_array = JSON.stringify(user_array);
        window.localStorage.setItem("users", converted_array);
      } else {
        alert("user already exists with same mobile number");
      }
    } else {
      user_list = [];
      user_list.push(new_user);
      user_list = JSON.stringify(user_list);
      window.localStorage.setItem("users", user_list);
    }
  }
}


//dom bom json 


//username/mob     +    password

let attempts=3


function handleLogin(){
    if (attempts>0){
    let username_input=document.getElementById("username").value
    let password=document.getElementById("password").value 
    // console.log(username,password);
    let users_list=window.localStorage.getItem("users")
     users_list=JSON.parse(users_list)
     let match=false
     users_list.forEach((val)=>{
        if ((val.mobile==username_input || val.username==username_input) && val.password===password){
            alert("login successful")
            window.sessionStorage.setItem("is_active","true")
            setTimeout(()=>{
                window.sessionStorage.setItem("is_active","false")
            },10*1000)
            match=true
        }
     })
     if(match==false){
         attempts-=1
        alert("invalid credentials")
        alert(`remaining attempts ${attempts}`)

        console.log(attempts)
     }

    }else
        {
    alert("pls try after 30secs")
    setTimeout(()=>{
        attempts=3
    },30*1000)
}
    
}

