//methods 

//string methods 

// concat 
// charCodeAt 
// slice 
// substring 
// uppercase




// Array methods  
// it is collection of elements   
//an element can be a value of any datatype  in js


//homogenous 
// let array=[ 1,true,null,undefined,[],"hello"] // heterogenous arrays

// //indexes --starting from 0 

// console.log(array[0]) 

// array[0]="hi"
// console.log(array[0])

// //arrays are mutable (they can be modified) 




// console.log(array[array.length-1])


//toString 

// console.log(arr.length)
// console.log( arr.toString())
// console.log(arr.at(2))


// console.log(arr.join(""))

//pop 

// arr.pop()//10 
// console.log(arr);

//push 
// arr.push(11)
// console.log(arr);
// arr.push(12)
// console.log(arr);
// arr.push(13,14,15,16,17,18,19,20)
// console.log(arr);


//shift 
// arr.shift()
// console.log(arr)

//unshift 
// arr.unshift(0)
// console.log(arr)
// arr.unshift(-2,-1,"end of -ve numbers")
// console.log(arr)


//push pop   --end   
//unshift shift --start 


// console.log(arr.length)
// delete arr[0]
// delete arr[9]
// delete arr[1]
// delete arr[2]
// delete arr[3]
// console.log(arr.length)
// console.log(arr)



//flat 

// let nested=[1,[2,[3,[4,[5,[6,[7,[8]]]]]]]]

// console.log(nested.flat());



// let flatted_arr=nested.flat(Infinity)
// console.log(flatted_arr);
// console.log(nested);
// console.log(Infinity<0)
// console.log(-Infinity == -Infinity);

// console.log(typeof(-Infinity))

//slice 



//splice 

//C R U D 
//splice

// let arr=[1,3,4,5,5,5,7,8,9,10]  
// arr.splice(1,0,2)  //
// console.log(arr);
// arr.splice(5,1,)
// console.log(arr);
// let arr=[1,2,3,3,5]
// arr.splice(3,1,4)
// console.log(arr);


//start index 

// delete count (number)

//elements to be added
// let arr=[]
// arr.splice(0,0,1,2,3,4,5,6,7,8,9,10)
// console.log(arr);



// // arr.splice(0,2,[1,2,3],{username:"mani"})
// // console.log(arr)


// arr.splice(2,0,5)//1 2 5 3 4 5 6 7 8 9 10
// console.log(arr);



// length 
// toString 
// at 
// join 
// pop 
// push 
// shift 
// unshift 
// // delete ***** 
// concat 
// flat  -- > Infinity , -Infinity  
// splice



// let arr=[1,2,3,4,5,6,7,8,9,10]  




// let result=arr.find(()=>{}) 
//find 
//map
//filter
//reduce
//reduceRight


let arr=[1,2,3,4,5,6,7,8,9,10]
console.log(arr.copyWithin(1,-10,-6)) 
