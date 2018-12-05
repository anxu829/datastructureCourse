#include<iostream>
#include<string>
#include<cstdlib>
#include<queue>


using namespace std;


// 定义存放数据的类型
typedef string       ElemType ;


// 首先需要定义树的每一个节点
struct treeNode{
    // 首先需要有一个存放数据的位置
    ElemType data;
    // 存放指向第一个子元素的指针
    treeNode * first_child ;
    // 存放指向第一个右兄弟节点的指针
    treeNode * first_sibling ;

};

typedef treeNode* Tree ;



int main(){
    cout << "start to create Tree  !" << endl;

    // 树的创建过程
    cout << "请输入树的头节点元素 ,若不想建立树请输入 # \n" ;
    ElemType head_data ;
    cin >>  head_data;


    if (head_data != "#"){
        // 首先定义头节点
        cout << "now i input an data ! \n" ;
        Tree T;

        // 必须要分配存储空间
        T = new treeNode;
        T->data = head_data;
        T->first_sibling = NULL;

        // 建立一个queue
        queue<Tree> Q;
        Q.push(T) ;

        while(!Q.empty()){
            // 拿到首个元素
            Tree head ;
            head = Q.front() ;
            Q.pop() ;



            cout << "现在为节点 ：  " << head->data <<" 输入子节点数据" << endl;

            string input ;
            cin >> input ;
            if (input != "#"){
                // 这里循环处理

                string first_child(1, input[0]);
                cout << "----> first child is" << first_child << endl;

                // 建立一个子节点
                Tree subtree;
                // 必须要分配存储空间
                subtree =new treeNode;
                subtree->data = first_child;
                subtree->first_child = NULL;
                subtree->first_sibling = NULL;

                head->first_child = subtree;
                Q.push(subtree) ;
                cout << "----> now back is " << Q.back()->data << endl;

                // 把余下的子节点接到后面去
                Tree cur = subtree;
                for (unsigned int i = 1 ; i < input.size() ; i ++){
                    Tree nxtsubtree =new treeNode;
                    nxtsubtree->data = input[i];
                    nxtsubtree->first_child = NULL;
                    nxtsubtree->first_sibling = NULL;

                    Q.push(nxtsubtree) ;
                    cout << "----> now back is " << Q.back()->data << endl;

                    cur->first_sibling = nxtsubtree;

                    cur = nxtsubtree;

                }


            }
            else{
                cout << head->data << " is leaf node" << endl;
                head->first_child = NULL;
            }

        }






    }
    return  0;
}
