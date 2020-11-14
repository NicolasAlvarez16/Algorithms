//Best Case: O(n) Time complexity | O(1) Space complexity
//Average Case: O(n^2) Time complexity | O(1) Space complexity 
//Worst Case: O(n^2) Time complexity | O(1) Space complexity 

#include<stdio.h>
#include<stdbool.h>

#define N 8

//Function Signature
int  * bubbleSort(int*); //Function to implement bubble sort algorithm
void swap(int*, int*); //Function to swap two elements

int main(){
    int myArray[N] = {1, -12, 9, 54, -11, 75, 8, 14};
    int i = 0;
    int *ptr;

    ptr = bubbleSort(myArray);
    for(i = 0; i < N; i++){
        printf(" %d ", *(ptr + i));
    }
    return 0;
}

int  * bubbleSort(int *myArray){
    bool isSorted = false;
    int counter = 0;
    int i = 0;
    int lenArray = N;

    while(!isSorted){
        isSorted = true; //Assume is sorted
        for(i = 0; i < lenArray - 1 - counter; i++){
            //Check if actual element is greater than following element
            if(*(myArray + i) > *(myArray + (i + 1))){
                swap(&*(myArray + i), &*(myArray + (i + 1)));
                isSorted = false;
            }
        }
        counter++;    
    }
    return myArray;
}

void swap(int *i, int *j){
    int temp = 0; 

    temp = *i;
    *i = *j;
    *j = temp;
}