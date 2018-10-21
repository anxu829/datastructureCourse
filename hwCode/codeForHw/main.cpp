#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <limits.h> /* INT_MAX�� */
#include <math.h> /* floor(),ceil(),abs() */


// ����һЩ��Ҫ�ı���
#define TRUE 1
#define FALSE 0
#define OK 1
#define ERROR 0
#define OVERFLOW -2
#define MAXSTRLEN 255


// ����status���򻯽ṹ
typedef int Status;
// sstring ָ���� unsigned char ����
typedef unsigned char SString[MAXSTRLEN + 1];


using namespace std;

// ������Ҫʵ�ֵķ���
Status StrAssign(SString T, char *chars);
Status Concat(SString &T, SString S1, SString S2);
int Index(SString S, SString T, int pos);
int Index_KMP(SString S, SString T, int pos);


// �����ľ���ʵ��
// ������������ַ���������һλ������һλ�ַ����ĳ��ȣ������������
Status StrAssign(SString T, char *chars)
{
    // ��ʼ������chars���ַ�������
    //�������������һ����ֵ����chars�Ĵ�T
    int len;
    len = strlen(chars);
    if (len > MAXSTRLEN)
        return ERROR;
    T[0] = len;
    for(int i = 1; i <= T[0]; i++)
        T[i] = *(chars + i - 1);
    return OK;
}


// �������Ӳ���
// ����Դ�T������ ���ڶ�ֵ�����޸�
Status Concat(SString &T, SString S1, SString S2)
{
    // ��T����S1��S2���Ӷ��ɵ��´�����δ�׶Σ��򷵻�TRUE�����򷵻�False
    int i;
    Status uncut;
    if (S1[0] + S2[0] <= MAXSTRLEN) //δ�ض�
    {
        for (i = 1; i <= S1[0]; i++) T[i] = S1[i];
        for (i = 1; i <= S2[0]; i++) T[i+S1[0]] = S2[i];
        T[0] = S1[0] + S2[0];
        uncut = TRUE;
    }
    else if (S1[0] < MAXSTRLEN) // �ض�
    {
        for (i = 1; i <= S1[0]; i++) T[i] = S1[i];
        for (i = S1[0] + 1 ;i <= MAXSTRLEN; i++) T[i] = S2[i-S1[0]];
        T[0] = MAXSTRLEN;
        uncut = FALSE;
    }
    else // �ضϣ���ȡS1��
    {
        for (i = 0; i <= MAXSTRLEN; i++) T[i] = S1[i];
        uncut = FALSE;
    }
    return uncut;
} // Concat



// ����ģʽƥ���㷨�����㷨
int Index(SString S, SString T, int pos)
{
    // �����Ӵ�T������S�е�pos���ַ�֮���λ�á��������ڣ�����ֵΪ0������T�ǿգ�1<=pos<=StrLength(S)��
    int i = pos;
    int j = 1;
    while (i <= S[0] && j <= T[0])
    {
        if (S[i] == T[j]) // �����ȽϺ���ַ�
        {
            ++i;
            ++j;
        }
        else // ָ��������¿�ʼƥ��
        {
            i = i - j + 2;
            j = 1;
        }
    }
    if (j > T[0])
        return i - T[0];
    else
        return 0;
} // Index


//KMP
void get_next(SString T, int *next)
{
    int i = 1;
    next[1] = 0;
    int j = 0;
    while (i < T[0]) // T[0] Ϊ string �ĳ���
    {
        // T[i] ��ʾ��׺�ĵ����ַ�
        // T[j] ��ʾǰ׺�ĵ����ַ�
        if(j == 0 || T[i] == T[j])
        {
            ++i;
            ++j;
            next[i] = j;
        }
        else
            j = next[j]; // ���ַ���ͬ��jֵ����
    }
}

int Index_KMP(SString S, SString T, int pos)
{
    // ����ģʽ��T��next������T������S�е�pos���ַ�֮���λ�õ�KMP�㷨
    // ����T�ǿգ�1<=pos<=StrLength(S)��
    int next[255];
    int i = pos;
    int j = 1;
    get_next(T, next);
    while (i <= S[0] && j <= T[0])
    {
        if (j == 0 || S[i] == T[j]) // �����ȽϺ���ַ�
        {
            ++i;
            ++j;
        }
        else
            j = next[j]; // ģʽ�������ƶ�
    }
    if (j>T[0])
        return i-T[0];
    else
        return 0;
} // Index_KMP



int main()
{

    // ����������
    char *str1 = "ababaaba";
    char *str2 = "abaa";

    SString S, T, ST;
    int m, n;

    // assign to str
    StrAssign(S, str1);
    StrAssign(T, str2);

    // concat
    Concat(ST, S, T);
    printf("after concat %s\n", ST);

    m = Index(S, T, 0);
    printf("BF at  %d\n", m);
    n = Index_KMP(S,T,0);
    printf("KMP at  %d\n",n);
    return 0;

}
