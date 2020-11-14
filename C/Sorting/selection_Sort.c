// O(n^2) Time Complexity | O(1) Space Complexity

#include<stdio.h>

#define N 8

//Function Signature
int * selectionSort(int*); //Function to implement selection sort algorithm
void swap(int*, int*); //Function to swap two elements

int main(){
    int myArray[N] = {1, -12, 9, 54, -11, 75, 8, 14};
    int i = 0;
    int *ptr;

    ptr = selectionSort(myArray);
    for(i = 0; i < N; i++){
        printf(" %d ", *(ptr + i));
    }
    return 0;
}

int * selectionSort(int *myArray){
    int currentIdx = 0;
    int lenArray = N;
    int smallestIdx = 0;
    int i = 0;

    while(currentIdx < lenArray - 1){
        smallestIdx = currentIdx;
        for(i  = currentIdx + 1; i < lenArray; i++){
            if(*(myArray + smallestIdx) > *(myArray + i)){
                smallestIdx = i; //Update smaller index
            }
        }
        swap(&*(myArray + currentIdx), &*(myArray + smallestIdx)); //Swap elements to their right position
        currentIdx++; 
    }
    return myArray;
}

void swap(int *i, int *j){
    int temp =0; 

    temp = *i;
    *i = *j;
    *j = temp;
}