//node run time environment
//front end --html css js

//api -server

//presentation

//application
//datalayer

//json server
//node

// node package manager
//3rd party library installation  --npm

//api
//fetch

base_url = `http://localhost:3000/user`;

// fetch("http://localhost:3000/users")
//   .then((data) => data.json())
//   .then((data) => console.log(data))
//   .catch((err) => console.error(err));

// fetch("http://localhost:3000/users",{
//     method:"POST",
//     headers:{"Content-Type":"Application/json"},
//     body:  JSON.stringify({id:3,name:"ramesh"})
// }).then(d=>d.json()).then(d=>console.log(d)).catch(e=>console.log(e))

//PUT
// fetch("http://localhost:3000/users/3",{
//     method:"PUT",
//     headers:{"Content-Type":"Application/json"},
//     body:JSON.stringify({
//         id:"3",
//         name:"shiva",
//         age:"22",
//         batch:"35r"

//     })
// }).then(d=>d.json()).then(d=>console.log(d)
// )

//entire record/object will be replaced

//PATCH
// fetch("http://localhost:3000/users/3",{
//     method:"PATCH",
//     headers:{"Content-Type":"Application/json"},
//     body:JSON.stringify({
//         age:"25"
//     })
// }).then(d=>d.json()).then(d=>console.log(d))

//change entire tyre  --PUT
//modify the same tyre  --PATCH

// DELETE
// C
// R
// U -2
// D
// DRY -->dont repeat yourself

// fetch(`${base_url}/1`,{
//     method:"DELETE",
//     headers:{"Content-Type":"Application/json"}
// }).then(d=>d.json()).then(d=>console.log(d)).catch(e=>console.error(e)
// )

// GET
// POST
// PUT/PATCH
// DELETE

//DOM

// function handleSubmit() {
//   let username = document.getElementById("username").value;
//   let password = document.getElementById("password").value;
//   let mob = document.getElementById("mob").value;
//   let email = document.getElementById("email").value;

//   let details = {
//     username: username,
//     password: password,
//     mobile: mob,
//     email: email,
//   };

//   fetch(`${base_url}`, {
//     method: "POST",
//     headers: { "Content-Type": "Application/json" },
//     body: JSON.stringify(details),
//   })
//     .then((d) => d.json())
//     .then((d) => console.log(d))
//     .catch((e) => console.log(e));





// }

// fetch(`${base_url}`).then(res=>res.json()).then(res=>console.info(res)).catch(err=>console.error(err))


// console.table({id:1,name:"mani"}) 
// console.warn("alert!")