const submit_data = (e) => {
  console.log("btn clicked");

  // let api=

fetch("http://localhost:8000/register/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({
        id: "1",
        username: "manivardhan",
        password: "mani@123",
        email: "mani@gmail.com",
        age: "25",
        mobile: "9848022338"
    })

  })
    .then((res) => res.json())
    .then((data) => console.log(data))
    .catch((err) => console.error(err));
};

console.log(document.cookie);
