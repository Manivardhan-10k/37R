// let num =   123   //8 + 4 +8+ 2 +8 =30

// let even_sum=0

// while (num!=0){//123  12 1 0
//     let last_digit=num%10 //3  2 1

//     if(last_digit%2==0){
//         even_sum+=last_digit //0+2
//     }
//    num =Math.floor(num/10)  //123/10 12.3 12     12/10  1.2  1  1/10   0.1  0
// }


// let num =123   //321  32  321
// rev=0 
// while (num!=0){//123 12 1 0
//     let last_digit=num%10 // 3   2 
//     rev=rev*10+last_digit   //0*10 +3 3    3*10  +2  30+2  32 32*10 +1  320+1 321
//     num= Math.floor(num/10) // 12  1 0
// }
// console.log(rev)


//fibanocci series  
// let limit=10 
// let a=0
// let b=1 
// let count=0
// while (true){
//     count++ //1
//     if(count===limit){
//         console.log(a) //0    ..... 34
//         break;
//     }
//     let c=a+b 
//     a=b 
//     b=c
// }


// let fact=7   // 5040   1*2*3*4*5*6*7 ==5040

// function factorial(n){
//     if(n===1){
//         return 1
//     }
//  return n* factorial(n-1)
// }
// console.log(factorial(fact))



// let senetence="HELLO world" //3   aeiouAEIOU 
// // senetence=senetence.toLowerCase()
// // 65-90   97-122
// let vowels="aeiouAEIOU"
// let vowel_count=0 
// for(let i=0;i<senetence.length;i++){
//    if( vowels.includes(senetence[i])){
//     vowel_count++
//    }
// }
// console.log(vowel_count);


// let strarray=["mom","dad","sis","amma","anna","babai","madam","racecar"]


// count ==strarray.length



// hashmap  hashing

// let word="javascriptttttt" //a   {j:1,a:2,v:1...t:6}

// //most repeated character 
// // count each char occurances 
// //compare the most no of occurances
// let obj={} //{j:1}

// for (let i=0;i<word.length;i++){ //j  ... t  //0 1
//     if(obj[word[i]]){   // obj[j]  obj[a]  obj[v]  obj[a]
//         obj[word[i]]++ //obj[a]++ 1++ 2
//     }else{
//         obj[word[i]]=1//obj[j]=1 obj[a]=1
//     }
//     console.log(obj);
// }
// // debugger
// let max=0
// let char=""
// for(let i in obj){

//     if(obj[i]>max){
//         max=obj[i] //1 2 6
//         char=i  //j a t
//     }
// }
// console.log(char, max);




// // let obj2={
// //     name:"mani"
// // }



// console.log(obj2["age"])


// console.log({}=={});

// call by reference


// console.log("hello"==="hello");
//call by value
