//Best Case: O(n) Time Complexity | O(1) Space Complexity
//Average Case: O(n^2) Time Complexity | O(1) Space Complexity
//Worst Case: O(n^2) Time Complexity | O(1) Space Complexity

#include<stdio.h>

#define N 8

//Function Signature
int  * insertionSort(int*); //Function to implment insertion sort algorithm
void swap(int*, int*); //Function to swap two elements

int main(){
    int myArray[N] = {1, -12, 9, 54, -11, 75, 8, 14};
    int i = 0;
    int *ptr;

    ptr = insertionSort(myArray);
    for(i = 0; i < N; i++){
        printf(" %d ", *(ptr + i));
    }
    return 0;
}

int * insertionSort(int *myArray){
    int i = 0;
    int lenArray = N;
    int valueSort = 0;

    for(i = 1; i < lenArray; i++){
        //Loop through the array once
        valueSort = *(myArray + i); //Select the first unsorted element
        while(*(myArray + (i - 1)) > valueSort && i > 0){
            swap(&*(myArray + i), &*(myArray + (i - 1))); //Swapping other elements to the right to shift unsorted array
            i = i - 1;
        }
    }
    return myArray;   
}

void swap(int *i, int *j){
    int temp =0; 

    temp = *i;
    *i = *j;
    *j = temp;
}