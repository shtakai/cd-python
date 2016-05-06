

function selectsort(l){
    for(var j = 0; j < l.length - 1; j++){
        lowestIndex = j;
        for(var i = j + 1; i < l.length; i++){
            if( l[lowestIndex]> l[i]){
                lowestIndex = i;
            }
        }
        [l[lowestIndex], l[j]] = swap(l[lowestIndex],l[j]);

        //var tmp = l[lowestIndex];
        //l[lowestIndex] = l[j];
        //l[j] = tmp;
    }
}
function swap(a,b){
    return [b, a];
}

arr= [532,321,56,234,1,463,342,2];
(selectsort(arr));
console.log(arr);
