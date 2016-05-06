

array = [1,2,3,4,5,6]

console.log(shuffle(array));

function shuffle(l) {
     //if list.len ==0
       //return head
     //else
       //get one element randomly  and  call shuffle(remain of the list)


    [head, list] = head_list(l);
    console.log('haad:',head,'list',list);

    if(list.length == 0){
        console.log('list is empty return head',head);
        return head;
    }else{
        index = Math.floor(Math.random() *(list.length - 1));
        console.log('random index:', index);
        swap(list[index], index[list.length - 1]);
        [list[index], list[list.length - 1]] = swap(list[index], list[list.length - 1]);
        return([list.pop(), shuffle(list)]);
    }

}

function swap(a,b) {
    return [b, a];
}

function head_list(l){
    head = null
    list = []
    for( var i in l ){
        if(i == 0){
            head = l[i];
        }else{
            list.push(l[i]);
        }
    }
    return[head, list];
}
