#include<iostream>
#include<vector>

using std::cout;
using std::endl;
using std::end;
using std::begin;
int main()
{
    int a[6]  = {5,2,4,6,1,3};
    int lenA = end(a) - begin(a);
    cout << "lenA is" << lenA << endl;
    for(int i = 1 ; i != lenA ; i++ ){
        int key = a[i];
        int j = i-1;
        while( j >= 0 && a[j] > key ){
            a[j+1] =  a[j];
            j--;
        }
        cout << j << endl ;

        a[j+1] = key;
    }
    for(int & i:a){
        cout << i ;
    }




    return 0;
}
