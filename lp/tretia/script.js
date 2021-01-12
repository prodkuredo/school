alert('хочу значения(10) не больше 1500')
let arr = []
for(let i = 0 ; i <10; i++){
    let a = +prompt()
    arr.push(a)
}
// alert(arr)
var min = 1501
for(let i = 0; i < arr.length; i++){
    if(arr[i] % 3== 0){
        if(arr[i] < min){
            min = arr[i]
        }
    }
}
if(min == 1501){
    alert(arr)
}
else{
    for(let i = 0; i < arr.length; i++){
    if(arr[i] % 2 == 0){
        arr[i] -= min
    }
}
}
alert(arr)