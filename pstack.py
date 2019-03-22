MyStack = []
Ans_stack = [1,2,3,4,5]
StackSize = 5



def DisplayStack():
    print("Question for the IQ test are as follows:")
    count =0
    for Item in MyStack:
        print(Item)
        c = int(input())
        d = Ans_stack.pop()
        print(d)
        if(c == d):
            count+=1
    print("count = ",count)
    return count    
      

  
def Push(Value):
 if len(MyStack) < StackSize:
  MyStack.append(Value)
 else:
  print("Stack is full!")


Push("Question 1")
Push("Question 2")
Push("Question 3")
Push("Question 4")
Push("Question 5")
ans=input("Want to give the IQ test ?\n");
if(ans == "Yes" or ans == "yes"):
    c = DisplayStack()
   # Pop()
    print(c)
else:
    quit()
