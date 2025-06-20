// document
// bom: 


// console.log(window.innerHeight)
// console.log(window.innerWidth)

// alert 
// prompt 
// confirm 
// window.open("http://www.google.com")

function handleClose(){

    window.close()
}




// a  
// href  ---"http://"
// target: parent , self ,blank



// console.log(navigator.userAgent)

// navigator.geolocation.getCurrentPosition(function(pos){
//    console.log(pos.coords.latitude,  pos.coords.longitude,pos.coords.accuracy);
// })

// window 
// navigator
//screen 
// console.log(screen.orientation)

// console.log(location.href) 
// location.href="https://www.instagram.com"
// location.href="http://127.0.0.1:5501/index.html"


 //   http://  127.0.0.1 :5500 / index.html 
 //3306 
 //27071 
 //8000 
 //3000

//  dns  -->domain naming system  //google amazon youtube 

//  70
//  mani villa


// ports :
// lan 
// hdmi 
// usb a 
// usb c 
// head phone  
// charging 
// cd/dvd


// location.assign("https://www.instagram.com")


//history 
// back 
// forward 
// go



// browser storage 
// sessionStorage  
// localStorage


// run enviroment  
// os 
// memory 
// display 
// cpu 

// window.sessionStorage//if tab is open we can use
// window.localStorage()// even after tab is closed data remains 

// window.sessionStorage.setItem("my_name","manivardhan")

// window.sessionStorage.setItem("is_logged_in","True")

// let user_logged=window.sessionStorage.getItem("is_logged_in")
// console.log(user_logged);



// window.localStorage.setItem("name","madhu") 


// only strings  

// languages , 
// console.log(typeof('["tel","hin","eng"]')) 

// window.sessionStorage.setItem("language",'["tel","hin","eng"]')

let user_languages=window.sessionStorage.getItem("language")

console.log(user_languages[0]);


// JSON :: text-format for data inter change  in between the systems
//JavaScript Object Notation

// let lang=(JSON.parse(user_languages)) 
// console.log(lang[0])

// console.log(typeof(JSON.stringify({batch:35})))

// API 

