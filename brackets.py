 stack=[]
        for c in s:
            if c in ['(','[','{']:
                stack.appned(c)
            elif c==')' and len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            elif c==']' and len(stack)!=0 and stack[-1]=='[':
                stack.pop()
            elif c=='}' and len(stack)!=0 and stack[-1]=='{':
                stack.pop()
            else:
                return False
            
        return stack ==[]