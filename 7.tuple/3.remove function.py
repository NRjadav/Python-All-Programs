
# modify tuple elements

# Note:==> tuples are immuteble - but if we want to modify it we can convert it into list and after modification  we can reconvert into tuple



t=(12,23,45,85)

l1=list(t)

l1.remove(23)

t=tuple(l1)

print(t)


