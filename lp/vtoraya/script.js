alert('хочу значения(10)')
let arr = []
for(let i = 0 ; i <10; i++){
    let a = +prompt()
    arr.push(a)
}
alert(arr)
var max = -101
for(let i = 0; i < arr.length; i++){
    if(arr[i] % 2== 0){
        if(arr[i] > max){
            max = arr[i]
        }
    }
}

for(let i = 0; i < arr.length; i++){
    if(arr[i] % 2 == 0){
        arr[i] = max
    }
}
alert(arr)