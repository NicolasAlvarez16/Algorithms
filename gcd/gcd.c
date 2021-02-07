#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<string.h>

int gcd(int, int); //Find greates common divisor between two nums
int *extendedGcd(int, int); //Gcd reverse
void swap(int*, int*);
int mod(int, int);

bool option = false;

int main(int argc, char **argv){
    if(argc < 3 || argc > 4){
        printf("Usage: 2 argument only, a and b\n");
        exit(-1);   
    }
    
    if(argc > 3){
        if(strcmp(argv[3], "-e") == 0 || strcmp(argv[3], "--equations") == 0){
            option = true;
        }
        else{
            printf("Error");
        }
    }

    int *ptr; 
    int arg1 = atoi(argv[1]);
    int arg2 = atoi(argv[2]);

    printf("gcc(%d, %d) = %d\n", arg1, arg2, gcd(arg1, arg2));
    printf("---------------------------------------\n");
    ptr = extendedGcd(atoi(argv[1]), atoi(argv[2]));
    printf("gcd(%d, %d) = %d(%d) + %d(%d) -> m = %d, n = %d\n", arg1, arg2, arg1, ptr[0], arg2, ptr[1], ptr[0], ptr[1]);
}

void swap(int *swapA, int *swapB){
    int aux = *swapA;
    *swapA = *swapB;
    *swapB = aux;
}

int mod(int a, int b){
    return a%b;
}

int gcd(int a, int b){
    int q; 
    int r;
    
    if(b > a){
        swap(&a, &b);
    }

    if(b == 0){
        return a;
    }

    q = a / b;
    r = a - (q * b);
    
    if(option){
        printf("%d = %d(%d) + %d\n", a, q, b, r);
    }

    if(r != 0){
        a = b;
        b = r;
        return gcd(a, b);
    }
    else{
        printf("---------------------------------------\n");
        return b;
    }
}

int *extendedGcd(int a, int b){
    int *results = malloc(sizeof(int) * 2);

    if(b == 0){
        results[0] = 1;
        results[1] = 0;

        return results;
    }
    else{
        int m, n;

        results = extendedGcd(b, mod(a, b));
        m = results[0];
        n = results[1];
        results[0] = results[1];
        results[1] = m - a/b * n;
        return results;      
    }
} 


