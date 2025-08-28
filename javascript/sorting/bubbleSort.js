function bubbleSort(arr){

    for (let i = 0; i < arr.length - 1; i++) {
        for (let j = 0; j < arr.length - 1; j++) {
            
            if(arr[j] > arr[j+1]){
                let aux = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = aux;
            }
            
        }        
    }
}

// test
arr = [72, 64, 50, 23, 84, 18, 37, 99, 45, 8];

// print before and after of the ordering
console.log(arr);
bubbleSort(arr);
console.log(arr);

