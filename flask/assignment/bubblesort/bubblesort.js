function bubbleSort(arr) {
  var resultArray = [];
  var searchDepth = arr.length
  while(searchDepth > 0){
    for (var i = 0; i < searchDepth; i++) {
      if (arr[i] > arr[i + 1]) {
        [arr[i], arr[i+1]] = swap(arr[i],arr[i+1]);
      }
    }
    resultArray.unshift(arr.pop());
    searchDepth -= 1;
  }
  return resultArray;
}

function swap(a,b) {
  return [b,a];
}
var array = [];

for(var i = 0; i < 100; i++){
  array.push(parseInt(Math.random()*10000));
}

console.log(bubbleSort(array));
