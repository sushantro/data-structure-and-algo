// function linearSearch(arr, val){
//     for(var i = 0; i < arr.length; i++){
//         if(arr[i] === val) return i;
        
//     }
//     return -1;
// }


//   const bata=linearSearch([34,51,1,2,3,45,56,687], 1)
//   console.log(bata);


const linear=(arr,val)=>{
    for(let i=0;i<arr.length;i++){
        if (arr[i]===val) return i ;

    }
    return -1



}
const bata=linear([24,45,1,3,45],45)
console.log(bata); 