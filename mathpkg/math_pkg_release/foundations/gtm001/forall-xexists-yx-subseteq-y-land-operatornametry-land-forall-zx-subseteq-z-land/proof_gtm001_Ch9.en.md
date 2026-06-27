---
role: proof
locale: en
of_concept: forall-xexists-yx-subseteq-y-land-operatornametry-land-forall-zx-subseteq-z-land
source_book: gtm001
source_chapter: "9"
source_section: ""
---

If $G'x = x \cup (\cup(x))$, then there exists a function $f$ defined by recursion on $\omega$ such that

$$f'0 = x$$
$$f'(n + 1) = G'f'n.$$

Furthermore, if

$$y = \bigcup_{n < \omega} f'n$$

then $x = f'0 \subseteq y$. From the definition of $G$

$$f'n \subseteq f'(n + 1) \land \cup(f'n) \subseteq f'(n + 1).$$

If $a \in b \land b \in y$ then $(\exists n)[b \in f'n]$ and hence

$$a \in \cup(f'n) \subseteq f'(n + 1)$$

i.e., $a \in f'(n + 1)$. Then $a \in y$ and hence $y$ is transitive.

If $x \subseteq z \land \operatorname{Tr}(z)$ then we prove by induction that

$$f'n \subseteq z.$$

$f'0 = x \subseteq z$. If $f'n \subseteq z$ then since $z$ is transitive $\cup(f'n) \subseteq z$, i.e.,

$$a \in \cup(f'n) \land f'n \subseteq z \rightarrow a \in z.$$

Thus $f'(n + 1) = f'n \cup (\cup(f'n)) \subseteq z$.

Consequently $y = \bigcup_{n < \omega} f'n \subseteq z.$
