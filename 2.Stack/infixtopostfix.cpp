
#include<iostream>
using namespace std;

 

class Stack
{
    int size;
    int *arr;
    int top;
public:
    Stack();
    Stack(int);
    void push(int);
    int pop();
    int peek();
    bool isfull();
    bool isempty();
};

 

int Stack::peek()
{
    return arr[top];
}

 


Stack::Stack()
{
    size=5;
    arr=new int[size];
    top=-1;    
}

 


Stack::Stack(int s)
{
    size=s;
    arr=new int[size];
    top=-1;    
}

 


void Stack::push(int val)
{
    if(!isfull())
        arr[++top]=val;
    else
        throw "stack is full!";
}

 


int Stack::pop()
{
    if(!isempty())
        return arr[top--];
    else
        throw "stack is empty!";
}

 


bool Stack::isfull()
{
    return top==size-1;
}

 


bool Stack::isempty()
{
    return top==-1;
}

 

int findprecedence(char ch)
{
    switch(ch)
    {
        case '+':
        case '-':
            return 1;
        case '*':
        case '/':
            return 2;
    }
    return 0;
}

 


int main()
{
    int i=0, j=0;
    char ch;
    char infix[100], postfix[100];
    Stack s1(50);
    
    cout<<"Enter fully paranthesized infix string-"<<endl;
    cin>>infix;
    
    while(infix[i]!='\0')
    {
        if(infix[i]=='(')
        {
            s1.push(infix[i]);
        }
        else if(infix[i]>='a' && infix[i]<='z')
        {
            postfix[j++]=infix[i];
        }
        else if(infix[i]=='+' || infix[i]=='-' || infix[i]=='*' || infix[i]=='/')
        {
            while(s1.peek()=='+' || s1.peek()=='-' || s1.peek()=='*' || s1.peek()=='/')
            {
                if(findprecedence(s1.peek())>=findprecedence(infix[i]))    
                {
                    postfix[j++]=s1.pop();
                }    
                else
                    break;
            }
        
            s1.push(infix[i]);
        }
        else if(infix[i]==')')
        {
            while((ch=s1.pop())!='(')
            {
                postfix[j++]=ch;
            }
        }
        i++;
    }
    postfix[j]='\0';
    cout<<"The postfix form of given infix expression  - "<<postfix<<endl;
        
    return 0;
}