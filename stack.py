#stack using python list
'''stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

print(stack.pop(),stack[-1],len(stack),len(stack)==0)'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.Top=None 
        
    def push(self,data):
        node=Node(data)
        if self.Top is None:
            self.Top=node    
            return   
        node.next=self.Top
        self.Top=node
    def pop(self):
        if self.Top is None:
            print("Stack is underflow")
            return
        value=self.Top.data
        self.Top=self.Top.next
        return value
    def peek(self): 
        if self.Top is None:
           print("Stack is underflow")
           return   
        return self.Top.data
    def isEmpty(self):
        if self.Top is None:
            print("Stack is empty")
        else:
            print("stack is not empty")
    def size_display(self):
        if self.Top is None:
            print("Stack is underflow")
            return      
        current=self.Top
        count=0
        while current is not None:
            count+=1
            print(f"{current.data}")  
            current=current.next
        print(f"size of stack is {count}")    
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.size_display()  
s.isEmpty()      
print(s.peek()) 
print(s.pop())       
s.size_display()  

def is_balanced(s):
    if s:
        stack=[]
        pairs={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if top !=pairs[ch]:
                    return False  
        return len(stack)==0
    
print(is_balanced('{[(}]}'))   


def precence(op):
    if op=='+' or op=='-':
        return 1
    elif op=="*" or op=='/' or op=='%':
        return 2
    elif op=='^':
        return 3
    return 0
def infix_to_postfix(exp):
    stack=[]
    postfix=''
    if exp is not None and exp!='':
        for ch in exp:
            if ch.isalnum():
                postfix+=ch
            elif ch=='(':
                stack.append(ch)
            elif ch==')':
                while stack and stack[-1]!='(':
                    postfix+=stack.pop()
                stack.pop()
            else:
                while (stack and stack[-1]!='(' and  precence(stack[-1])>=precence(ch)):
                     postfix+=stack.pop()
                stack.append(ch)
        while stack:
            postfix+=stack.pop()
        return postfix                                             
print(infix_to_postfix('(a+b)*c/h-o+h*k'))    

def infix_to_prefix(exp):
    print("inside in the function",exp)
    if exp is not None and exp != '':
        print("inside in the condition")
        stack=[]
        print("stack",stack)
        postfix=''
        print("postfix",postfix)
        exp=exp[::-1]
        print("exp",exp)
        temp=''
        for ch in exp:
            if ch=='(':
                temp+=')'
            elif ch==')':
                temp+='('
            else:
                temp+=ch
        print("temp",temp)
        for ch in temp:
            if ch.isalnum():
                postfix+=ch
            elif ch=='(':
                stack.append(ch)
            elif ch==')':
                while stack and stack[-1]!='(':
                    postfix+=stack.pop()
                stack.pop()
            else:
                while (stack and stack[-1]!='(' and  precence(stack[-1])>precence(ch)):
                        postfix+=stack.pop()
                stack.append(ch)
        while stack:
            postfix+=stack.pop()
        return postfix[::-1]
print(infix_to_prefix('(a+b)*c/h-o+h*k'))                  

def postfix_to_infix(exp):
    if exp is not None and exp != '':
        stack=[]
        for ch in exp:
            if ch.isalnum():
                stack.append(ch)
            else:
                if stack and len(stack)>=2:
                    op2=stack.pop()  
                    op1=stack.pop()
                    if op1 and op2:
                        exp="("+op1+ch+op2+")"
                        stack.append(exp)
        return stack                
print(postfix_to_infix('ab+b/c*f/e-'))      

def prefix_to_infix(exp):
    if exp is not None and exp!='':
        stack=[]
        exp=exp[::-1]
        for ch in exp:
            if ch.isalnum():
                stack.append(ch)
            else:
                if stack and len(stack)>=2:
                    op1=stack.pop()
                    op2=stack.pop()
                    if op1 and op2:
                        exp="("+op1+ch+op2+")"
                        stack.append(exp)
        return stack[::-1]
print(prefix_to_infix('-*+/A^BC-DE+F*G^HI%JK'))    

def postfix_to_prefix(exp):
    if exp is not None and exp != '':
        stack=[]
        for ch in exp:
            if ch.isalnum():
                stack.append(ch)
            else:
                right=stack.pop()
                left=stack.pop()
                if left and right:
                    exp="("+ch+left+right+")"
                stack.append(exp)
        return stack
print(postfix_to_prefix('ab+cd-*ef+gh-*+'))                    
        
                
def prefix_to_postfix(exp):
    if exp is not None and exp != '':
        stack=[]
        for ch in exp[::-1]:
            if ch.isalnum():
                stack.append(ch)
            else:
                left=stack.pop()
                right=stack.pop()
                if left and right:
                    exp="("+left+right+ch+")"
                stack.append(exp)
        return stack
print(prefix_to_postfix("+*+ab-cd*+ef-gh"))                               

def next_first_greater_element(arr):
    if arr is None or len(arr) == 0:
        return []

    answer = [-1] * len(arr)
    stack = []
    # Traverse from right to left
    for i in range(len(arr) - 1, -1, -1):

        # Remove all elements smaller than or equal to the current element
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # If the stack is not empty, the top is the next greater element
        if stack:
            answer[i] = stack[-1]

        # Push the current element onto the stack
        stack.append(arr[i])

    return answer


# Example
arr = [4, 5, 2,25]
print(next_first_greater_element(arr))

def stock_span(stocks):
    if stocks is not None and len(stocks)!=0:
        span=[0]*len(stocks)
        stack=[]
        for i in range(len(stocks)):
            while stack and stocks[stack[-1]]<=stocks[i]:
                stack.pop()
            if not stack:
                span[i]=i+1
            else:
                span[i]=i-stack[-1]
            stack.append(i)
        return span
stocks=[60, 70, 80, 100, 90, 75, 80, 120]    
span=stock_span(stocks)
print(f"The Span of {stocks} is {span}")  

def daily_temperatures(temperatures):
      if temperatures is not None and len(temperatures)!=0:   
          warmerdays=[0]*len(temperatures)
          stack=[]
          for i in range(len(temperatures)-1,-1,-1):
              while stack and temperatures[stack[-1]]<=temperatures[i]:
                  stack.pop()
              if stack:
                  warmerdays[i]=stack[-1]-i
              stack.append(i)
          return warmerdays
temperatures=[120,60, 70, 80, 100, 90, 75, 80]    
warmerdays=daily_temperatures(temperatures)
print(f"The Span of {temperatures} is {warmerdays}")      


def maximum_rectangle(histograms):
        if histograms is not None and len(histograms)!=0:       
            stack=[]
            histograms.append(0)
            max_area=0
            height=0
            for i in range(len(histograms)):
                while stack and histograms[stack[-1]] >=histograms[i]:
                    height=histograms[stack.pop()]                    
                    if stack:
                     width=i-stack[-1]-1
                    else:
                     width=i
                    area=height*width
                    max_area=max(max_area,area)
                stack.append(i)
        return max_area
    
print(maximum_rectangle([2, 1, 5, 6, 2, 3]))                        
                        