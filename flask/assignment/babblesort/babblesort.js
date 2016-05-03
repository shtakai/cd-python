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

console.log(bubbleSort([5, 4, 6, 2, 7, 8, 1]));
