def eggr(l,m):
	a=sorted(l)[0]
	b=[sorted(l)[0]]
	c=0
	while 1:
		for i in range(len(l)):
			c=a
			for i in range(m):
				if a+(m-(i)) in l:
					a=a+(m-(i))
					b.append(a)
					break
			if a+m>sorted(l)[len(l)-1]:
				break
			if c==a:
				raise SyntaxError("No next index!")
		if b==sorted(b):
			break
	return b
