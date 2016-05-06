function selectSort(arr){
  // find minimum
   // index of min
  for (var j = 0; j < arr.length -1; j++) {
    var minIndex = j;
    for (var i = j+1; i < arr.length; i++) {
      if (arr[minIndex] > arr[i]){
        minIndex = i;
      } // closes if
    } // closes i loop
    var temp = arr[minIndex];
    arr[minIndex] = arr[j];
    arr[j] = temp;
  } // closes j loop
}
var arr = [3,6,9,-3,12];
selectSort(arr);
console.log(arr);

