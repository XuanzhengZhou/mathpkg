---
role: exercise
locale: en
chapter: "2"
section: "2.3"
exercise_number: "2b"
---

Let $G$ act on the product $X \times X$ by the formula $s(x,y) = (sx, sy)$. Show that the character of the corresponding permutation representation is equal to $\chi^2$.

**Solution.** Let $\chi$ be the character of the permutation representation on $X$, so $\chi(s) = |\{x \in X : s x = x\}|$, the number of fixed points of $s$ on $X$.

For the action on $X \times X$, the character $\tilde{\chi}$ at $s$ counts fixed points in $X \times X$:
$$\tilde{\chi}(s) = |\{(x,y) \in X \times X : s(x,y) = (x,y)\}| = |\{(x,y) \in X \times X : sx = x \text{ and } sy = y\}|.$$

Since the conditions on $x$ and $y$ are independent,
$$\tilde{\chi}(s) = |\{x : sx = x\}| \cdot |\{y : sy = y\}| = \chi(s) \cdot \chi(s) = \chi(s)^2.$$

Thus $\tilde{\chi} = \chi^2$. $\square$
