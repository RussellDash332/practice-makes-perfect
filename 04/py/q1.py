def new_if(predicate, then, otherwise):
    if predicate:
        then
    else:
        otherwise

def p(x):
    new_if(x > 5, print(x), p(x+1))

p(1) # what happens here?