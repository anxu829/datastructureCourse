

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <limits.h> /* INT_MAX等 */
#include <math.h> /* floor(),ceil(),abs() */

using namespace std;

#define TRUE 1
#define FALSE 0
#define OK 1
#define ERROR 0
#define OVERFLOW -2

typedef int Status;

// 定长顺序存储表示
#define MAXSTRLEN 255
// sstring 指的是 unsigned char 数组
typedef unsigned char SString[MAXSTRLEN + 1];


Status StrAssign(SString T, char *chars);
Status Concat(SString &T, SString S1, SString S2);
int Index(SString S, SString T, int pos);
int Index_KMP(SString S, SString T, int pos);

Status StrAssign(SString T, char *chars)
{
    // 初始条件：chars是字符串常量
    //操作结果：生成一个其值等于chars的串T
    int len;
    len = strlen(chars);
    if (len > MAXSTRLEN)
        return ERROR;
    T[0] = len;
    for(int i = 1; i <= T[0]; i++)
        T[i] = *(chars + i - 1);
    return OK;
}

// 串的连接操作
Status Concat(SString &T, SString S1, SString S2)
{
    // 用T返回S1和S2连接而成的新串。若未阶段，则返回TRUE，否则返回False
    int i;
    Status uncut;
    if (S1[0] + S2[0] <= MAXSTRLEN) //未截断
    {
        for (i = 1; i <= S1[0]; i++) T[i] = S1[i];
        for (i = 1; i <= S2[0]; i++) T[i+S1[0]] = S2[i];
        T[0] = S1[0] + S2[0];
        uncut = TRUE;
    }
    else if (S1[0] < MAXSTRLEN) // 截断
    {
        for (i = 1; i <= S1[0]; i++) T[i] = S1[i];
        for (i = S1[0] + 1 ;i <= MAXSTRLEN; i++) T[i] = S2[i-S1[0]];
        T[0] = MAXSTRLEN;
        uncut = FALSE;
    }
    else // 截断（仅取S1）
    {
        for (i = 0; i <= MAXSTRLEN; i++) T[i] = S1[i];
        uncut = FALSE;
    }
    return uncut;
} // Concat

// 串的模式匹配算法：简单算法(Brute-Force算法)
int Index(SString S, SString T, int pos)
{
    // 返回子串T在主串S中第pos个字符之后的位置。若不存在，则函数值为0。其中T非空，1<=pos<=StrLength(S)。
    int i = pos;
    int j = 1;
    while (i <= S[0] && j <= T[0])
    {
        if (S[i] == T[j]) // 继续比较后继字符
        {
            ++i;
            ++j;
        }
        else // 指针后退重新开始匹配
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

// 串的模式匹配算法：KMP算法
void get_next(SString T, int *next)
{
    int i = 1;
    next[1] = 0;
    int j = 0;
    while (i < T[0]) // T[0] 为 string 的长度
    {
        // T[i] 表示后缀的单个字符
        // T[j] 表示前缀的单个字符
        if(j == 0 || T[i] == T[j])
        {
            ++i;
            ++j;
            next[i] = j;
        }
        else
            j = next[j]; // 若字符不同，j值回溯
    }
}

int Index_KMP(SString S, SString T, int pos)
{
    // 利用模式串T的next函数求T在主串S中第pos个字符之后的位置的KMP算法
    // 其中T非空，1<=pos<=StrLength(S)。
    int next[255];
    int i = pos;
    int j = 1;
    get_next(T, next);
    while (i <= S[0] && j <= T[0])
    {
        if (j == 0 || S[i] == T[j]) // 继续比较后继字符
        {
            ++i;
            ++j;
        }
        else
            j = next[j]; // 模式串向右移动
    }
    if (j>T[0])
        return i-T[0];
    else
        return 0;
} // Index_KMP

int main()
{
    SString S, T, ST;
    int m, n;
    
    char *str1 = "ababaaba";
    char *str2 = "aba";
    
    StrAssign(S, str1);
    StrAssign(T, str2);
    
    Concat(ST, S, T);
    printf("连接后的字符串为：%s\n", ST);
    
    m = Index(S, T, 0);
    printf("用简单算法求得匹配串始于：%d\n", m);
    n = Index_KMP(S,T,0);
    printf("用KMP算法求得匹配串始于：%d\n",n);
    return 0;
}

