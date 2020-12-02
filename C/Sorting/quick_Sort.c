#include<stdio.h>

#define N 8

//Function Signature
void quickSort(int*, int, int); //Function to sort the array recursively
int quickSortAux(int*,int, int); //Function to partition the array
void swap(int*, int*); //Function to swap two elements

int main(){
    int myArray[N] = {1, -12, 9, 54, -11, 75, 8, 14};
    int i;
    int arrayLen = N;
    
    quickSort(myArray, 0, arrayLen - 1);
    for(i = 0; i < N; i++){
        printf(" %d ", myArray[i]);
    }
}

void quickSort(int *myArray, int startIdx, int endIdx){
    int partIdx;

    if(startIdx < endIdx){
        partIdx = quickSortAux(myArray, startIdx, endIdx); //Partion index, now at correct place
        quickSort(myArray, startIdx, partIdx - 1); //Sort array before partIdx
        quickSort(myArray, partIdx + 1, endIdx); //Sort array after partIdx
    }
}

int quickSortAux(int *myArray, int startIdx, int endIdx){
    int pivot = myArray[endIdx]; //Pivor is the is placed at the last elemtn
    int i = startIdx - 1;
    int j;

    for(j = startIdx; j <= endIdx - 1; j++){
        //All the smaller elements than pivot to the left
        //All the greater elements than pivot to the right
        if(myArray[j] < pivot){
            //If current element is samller than pivot
            i++; //Increment index
            swap(&myArray[i], &myArray[j]);
        }
    }
    swap(&myArray[i + 1], &myArray[endIdx]);
    return (i + 1); //Partion index 
}

void swap(int *i, int *j){
    int temp = 0; 

    temp = *i;
    *i = *j;
    *j = temp;
}