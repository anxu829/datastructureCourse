#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <limits.h> /* INT_MAX等 */
#include <math.h> /* floor(),ceil(),abs() */

#include <string>


#define TRUE 1
#define FALSE 0
#define OK 1
#define ERROR 0
// #define OVERFLOW -2


using namespace std;
using  std::string;


// def elemtype
typedef string TElemType ;
typedef int Status;

// define a struct tree
// 使用typedef 定义了一个结构体 ， 并指定BiTree 表示指向该结构体对象的指针
typedef struct BiTNode{
    TElemType data;
    struct BiTNode *lchild , *rchild;
}BiTNode,*BiTree;


// define method for create
Status CreateBiTree(BiTree &T){

    // 传入的是对指针的引用，所以访问元素是通过 T->data 的方式访问指针指向对象的属性
    string ch;
    // 从控制台读取数据
    // c ++ 的换行输入使用cin 方法
    getline(cin,ch);
    //scanf("%c",&ch);
    // 这里传入&T , 是为了能对指针指向的结构进行修改
    // 如果是空字符串，表示进入到叶子节点的子节点，即叶子节点的左右节点都应该是空的

    if (ch == "None"){
            cout << "time to stop !" << endl;
            T= NULL;
    }// 将指针T指向空地址
    else{
        cout << "input is not N" << endl ;
        if (!(T = (BiTNode *)malloc(sizeof(BiTNode)))) return ERROR;
        T->data = ch; // 把ch赋值给data，然后进行前序的赋值操作
        cout << "T->data is " << T->data <<  endl;

        cout << "start to do lchild " << endl;
        CreateBiTree(T->lchild);

        cout << "start to do rchild " << endl;
        CreateBiTree(T->rchild);
    }
    return OK;


}

// 定义打印元素的方法
Status printTreeNode(TElemType e){
    // printf 接收的是 char * 类型，即接受的是一个char数组，所以传给方法的应该是一个 char*
    cout << e ;
    return OK;

}

// define method for traverse
void PreOrderTraverse(BiTree T , Status(*printTree)(TElemType ) ){
    // 这里不传入对树的引用，是因为不需要修改树的值
    // 当T !=NULL
    if (T){
        // 传入，并打印，且返回是否打印成功
        printTreeNode( (T->data)) ;
        PreOrderTraverse(T->lchild , printTree) ;
        PreOrderTraverse(T->rchild , printTree) ;
    }
}


void InOrderTraverse(BiTree T , Status(*printTree)(TElemType ) ){
    // 这里不传入对树的引用，是因为不需要修改树的值
    // 当T !=NULL
    if (T){
        // 传入，并打印，且返回是否打印成功

        InOrderTraverse(T->lchild , printTree) ;
        printTreeNode( (T->data)) ;
        InOrderTraverse(T->rchild , printTree) ;
    }
}

void PostOrderTraverse(BiTree T , Status(*printTree)(TElemType ) ){
    // 这里不传入对树的引用，是因为不需要修改树的值
    // 当T !=NULL
    if (T){
        // 传入，并打印，且返回是否打印成功

        PostOrderTraverse(T->lchild , printTree) ;
        PostOrderTraverse(T->rchild , printTree) ;
        printTreeNode( (T->data)) ;
    }
}


int main()
{
    // 建立了一个指向结构体BiNode的指针;
    BiTree T;

    cout << "start to insert" << endl;

    // 注意这里一定要传入对于树的指针 而不是 &T;
    CreateBiTree(T);

    cout << "now tree is build !"  << endl ;
    // 开始遍历树
    PreOrderTraverse(T,printTreeNode) ;
    InOrderTraverse(T,printTreeNode) ;
    PostOrderTraverse(T,printTreeNode) ;



}
