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
