#include<iostream>
#include<string>
#include<cstdlib>
#include<queue>


using namespace std;


// ���������ݵ�����
typedef string       ElemType ;


// ������Ҫ��������ÿһ���ڵ�
struct treeNode{
    // ������Ҫ��һ��������ݵ�λ��
    ElemType data;
    // ���ָ���һ����Ԫ�ص�ָ��
    treeNode * first_child ;
    // ���ָ���һ�����ֵܽڵ��ָ��
    treeNode * first_sibling ;

};

typedef treeNode* Tree ;



int main(){
    cout << "start to create Tree  !" << endl;

    // ���Ĵ�������
    cout << "����������ͷ�ڵ�Ԫ�� ,�����뽨���������� # \n" ;
    ElemType head_data ;
    cin >>  head_data;


    if (head_data != "#"){
        // ���ȶ���ͷ�ڵ�
        cout << "now i input an data ! \n" ;
        Tree T;

        // ����Ҫ����洢�ռ�
        T = new treeNode;
        T->data = head_data;
        T->first_sibling = NULL;

        // ����һ��queue
        queue<Tree> Q;
        Q.push(T) ;

        while(!Q.empty()){
            // �õ��׸�Ԫ��
            Tree head ;
            head = Q.front() ;
            Q.pop() ;



            cout << "����Ϊ�ڵ� ��  " << head->data <<" �����ӽڵ�����" << endl;

            string input ;
            cin >> input ;
            if (input != "#"){
                // ����ѭ������

                string first_child(1, input[0]);
                cout << "----> first child is" << first_child << endl;

                // ����һ���ӽڵ�
                Tree subtree;
                // ����Ҫ����洢�ռ�
                subtree =new treeNode;
                subtree->data = first_child;
                subtree->first_child = NULL;
                subtree->first_sibling = NULL;

                head->first_child = subtree;
                Q.push(subtree) ;
                cout << "----> now back is " << Q.back()->data << endl;

                // �����µ��ӽڵ�ӵ�����ȥ
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
