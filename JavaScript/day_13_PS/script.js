// 1. Find the Second Largest Number
//    Write a program to find the second largest number in an array using a single loop. Do not use built-in sort.


// let arr=[9,2,3,4,5,6,7,8,1,9,10,10,10,10,9,9,9,9]
// //remove the duplicates 
// let arr_2=[]
// for(let i=0;i<arr.length;i++){
//     if(arr_2.includes(arr[i])){
//     }else{
//         arr_2.push(arr[i])
//     }
// }
// arr_2.sort((a,b)=>b-a)
// console.log(arr_2[1])




// 2. Sum of Even Digits
//    Given a number, calculate the sum of its even digits using a loop (e.g., input: 2346, output: 2+4+6 = 12).

// let num=1246     // 6-1's   4-10's    2-100's   1-1000's  124.6
// let even_sum=0
// while (num>0){ //1246 124 12 1 0
//     let last_digit=num%10  //6 4 2 1
//     if (last_digit%2==0){
//         even_sum+=last_digit //0+6   6+4 10+2 12
//     }  
//     num=Math.floor(num/10)   //124.6  124  12.4  12 1.2  1 0.1 0
// }
// console.log(even_sum)


// 3. Check for Prime Number
//    Write a function that returns true if the input number is prime, else false. Avoid built-in methods.

//1 and itself 
//2    <itself
// let n=5
// const check_prime=(num)=>{  //5 
//     let factor=0
//     for(let i=2;i<num;i++){
//         if(num%i==0){
//             factor++
//             break
//         }
//     }
//     if(factor===0){
//         return true
//     }
//     else{
//         return false
//     }
// }
// console.log(check_prime(n))






// 4.Reverse a Number
//   Using a loop  reverse the digits of a number.
//   Example: "1234" → "4321"

//madam   amma racecar malayalam radar  mon dad sis anna 
// let num="123456789"//987654321 
// let rev=""
// for (let i=num.length-1;i>=0;i--){
//     rev+=num[i]
// }
// console.log(rev);





// 5.Fibonacci Series
//   Generate the first n Fibonacci numbers using a for or while loop.
//   Example: 0, 1, 1, 2, 3, 5, 8...

// let n=10   ///0 1 1 2 3 5 8 13 21 34 55 89 144 ......


// let f_n=0
// let s_n=1
// for (let i=0;i<n;i++){

//     console.log(f_n)//0
//     let t_n=f_n+s_n 
//     f_n=s_n 
//     s_n=t_n

// }




// 6.Check Armstrong Number
//   A number is Armstrong if the sum of its digits raised to the power of number of digits equals the number.
//   Example: 153 = 1³ + 5³ + 3³ = 153
//    1+125+27=153

// 7.Find Factorial (Loop and Recursion)
//   Write two versions of a factorial function – one using a loop, and another using recursion.

// 8.Count Vowels in a String
//   Write a function that returns the number of vowels (a, e, i, o, u) in a string (case-insensitive).

// 9.Find All Palindromes in an Array
//   Write a function that takes an array of strings and returns all elements that are palindromes.

// 10.Kaprekar Number
//    Write a function to check whether a number is a Kaprekar number or not.
//    A Kaprekar number is a number whose square can be split into two parts that add up to the original number.
//    Example: 45 → 45² = 2025 → 20 + 25 = 45 (Kaprekar number)


// let num=297  //88 209
// let squared=(num**2 )+""//2025 
// let mid=squared.length/2  //2
// console.log(mid);
// let f_h=squared.slice(0,mid) //20     (0,2.5)--->(0,2) 88
// let s_h=squared.slice(mid)  //25      (2.5)---> (2,...) 209 
// let sum= Number(f_h)  +  Number(s_h)  //45 
// if(sum==num){
//     console.log("kaprekar number");
// }else{  
//  console.log("not kaprekar number");
// }





// 11.Find Intersection of Two Arrays
//    Create a function that returns the common elements between two arrays without using filter, includes, or Set.

// 12.Find Duplicates in an Array
//    Write a function that identifies and returns duplicate elements from an array of numbers.

// 13.Write a JavaScript function that takes a string as input and returns the character that appears the most times in the string. 
//    If multiple characters have the same highest frequency, return any one of them.
//    Input: "programming"
//    Output: "g" (since 'g' appears twice, which is the highest)

// 14.Is Anagram?
//    Write a function that checks whether two input strings are anagrams of each other.
//    Example: listen and silent

// 15.Write a JavaScript function to calculate the sum of the series:
//    For n = 6, the sum is 1 - 2 + 3 - 4 + 5 - 6 = -3.
//    Implement the function to return the sum for any given positive integer n.

