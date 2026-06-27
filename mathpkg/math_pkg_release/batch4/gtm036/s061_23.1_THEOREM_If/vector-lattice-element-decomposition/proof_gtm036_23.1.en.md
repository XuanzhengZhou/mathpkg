---
role: proof
locale: en
of_concept: vector-lattice-element-decomposition
source_book: gtm036
source_chapter: "23"
source_section: "23.1"
---

Since the ordering is invariant under translation by a member of $E$, the smallest element of $E$ which is greater than both $x + z$ and $y + z$ is $x \vee y + z$. It follows that $x \vee y + z = (x + z) \vee (y + z)$, and a similar relation holds for the meet. Replacing $z$ by $-x - y$ in the preceding equation and rearranging terms, using the definition of the meet of $x$ and $y$, one obtains the identity:

$$x + y = x \vee y + x \wedge y.$$

In particular, $x = x \vee 0 + x \wedge 0$. The first term, $x \vee 0$, is called the positive part of $x$ and is denoted $x^+$. The element $-(x \wedge 0) = (-x) \vee 0$ is called the negative part of $x$ and is denoted $x^-$. Clearly $x^+ \geq 0$, $x^- \geq 0$, and $x = x^+ - x^-$. A particular consequence of this equality is that the positive cone generates $E$.
