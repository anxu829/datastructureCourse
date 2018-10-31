#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <limits.h> /* INT_MAX�� */
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
// ʹ��typedef ������һ���ṹ�� �� ��ָ��BiTree ��ʾָ��ýṹ������ָ��
typedef struct BiTNode{
    TElemType data;
    struct BiTNode *lchild , *rchild;
}BiTNode,*BiTree;


// define method for create
Status CreateBiTree(BiTree &T){

    // ������Ƕ�ָ������ã����Է���Ԫ����ͨ�� T->data �ķ�ʽ����ָ��ָ����������
    string ch;
    // �ӿ���̨��ȡ����
    // c ++ �Ļ�������ʹ��cin ����
    getline(cin,ch);
    //scanf("%c",&ch);
    // ���ﴫ��&T , ��Ϊ���ܶ�ָ��ָ��Ľṹ�����޸�
    // ����ǿ��ַ�������ʾ���뵽Ҷ�ӽڵ���ӽڵ㣬��Ҷ�ӽڵ�����ҽڵ㶼Ӧ���ǿյ�

    if (ch == "None"){
            cout << "time to stop !" << endl;
            T= NULL;
    }// ��ָ��Tָ��յ�ַ
    else{
        cout << "input is not N" << endl ;
        if (!(T = (BiTNode *)malloc(sizeof(BiTNode)))) return ERROR;
        T->data = ch; // ��ch��ֵ��data��Ȼ�����ǰ��ĸ�ֵ����
        cout << "T->data is " << T->data <<  endl;

        cout << "start to do lchild " << endl;
        CreateBiTree(T->lchild);

        cout << "start to do rchild " << endl;
        CreateBiTree(T->rchild);
    }
    return OK;


}

// �����ӡԪ�صķ���
Status printTreeNode(TElemType e){
    // printf ���յ��� char * ���ͣ������ܵ���һ��char���飬���Դ���������Ӧ����һ�� char*
    cout << e ;
    return OK;

}

// define method for traverse
void PreOrderTraverse(BiTree T , Status(*printTree)(TElemType ) ){
    // ���ﲻ������������ã�����Ϊ����Ҫ�޸�����ֵ
    // ��T !=NULL
    if (T){
        // ���룬����ӡ���ҷ����Ƿ��ӡ�ɹ�
        printTreeNode( (T->data)) ;
        PreOrderTraverse(T->lchild , printTree) ;
        PreOrderTraverse(T->rchild , printTree) ;
    }
}


void InOrderTraverse(BiTree T , Status(*printTree)(TElemType ) ){
    // ���ﲻ������������ã�����Ϊ����Ҫ�޸�����ֵ
    // ��T !=NULL
    if (T){
        // ���룬����ӡ���ҷ����Ƿ��ӡ�ɹ�

        InOrderTraverse(T->lchild , printTree) ;
        printTreeNode( (T->data)) ;
        InOrderTraverse(T->rchild , printTree) ;
    }
}

void PostOrderTraverse(BiTree T , Status(*printTree)(TElemType ) ){
    // ���ﲻ������������ã�����Ϊ����Ҫ�޸�����ֵ
    // ��T !=NULL
    if (T){
        // ���룬����ӡ���ҷ����Ƿ��ӡ�ɹ�

        PostOrderTraverse(T->lchild , printTree) ;
        PostOrderTraverse(T->rchild , printTree) ;
        printTreeNode( (T->data)) ;
    }
}


int main()
{
    // ������һ��ָ��ṹ��BiNode��ָ��;
    BiTree T;

    cout << "start to insert" << endl;

    // ע������һ��Ҫ�����������ָ�� ������ &T;
    CreateBiTree(T);

    cout << "now tree is build !"  << endl ;
    // ��ʼ������
    PreOrderTraverse(T,printTreeNode) ;
    InOrderTraverse(T,printTreeNode) ;
    PostOrderTraverse(T,printTreeNode) ;



}
