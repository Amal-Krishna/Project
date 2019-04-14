

from nltk.tree import Tree

vp = Tree('VP', [Tree('V', ['saw']), Tree('NP', ['him'])])

s = Tree('S', [Tree('NP', ['I']), vp])
 
 
print(s)



dp1 = Tree('dp', [Tree('d', ['the']), Tree('np', ['dog'])])
dp2 = Tree('dp', [Tree('d', ['the']), Tree('np', ['cat'])])
vp = Tree('vp', [Tree('v', ['chased']), dp2])

dp1.draw()

dp2.draw()

vp.draw()

tree = Tree('s', [dp1, vp])

print(tree)
tree.draw()


len(tree)

print(tree.leaves())


tree.label()

dp1.label()

