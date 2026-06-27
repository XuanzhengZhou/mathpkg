---
role: proof
locale: en
of_concept: forall-x-in-abarx-leq-barb-rightarrow-overlinecupa-leq-overlinea-times-b
source_book: gtm001
source_chapter: "9"
source_section: ""
---

If $(\forall x \in a)[\bar{x} \leq \bar{b}]$, then

$$(\forall x \in a)(\exists \tilde{f}_x)[\tilde{f}_x: x \xrightarrow{1-1} b].$$

By *Theorem 10.46

(1) $(\exists f)(\forall x \in a)[f'x: x \xrightarrow{1-1} b].$

Furthermore, if $x \in \cup(a)$ then

$$(\exists y)[x \in y \wedge y \in a].$$

Again by *Theorem 12.46

(2) $(\exists h)(\forall x \in \cup(a))[x \in h'x \wedge h'x \in a].$

We then define a function $F$ on $\cup(a)$ in the following

But if $h'x = h'y$, then $f'h'x = f'h'y$. Furthermore, since $f'h'x$ is one-to-one
$$(f'h'x)'x = (f'h'y)'y \rightarrow x = y.$$

Thus $F: \cup(a) \xrightarrow{1-1} a \times b$ and so
$$\overline{\cup(a)} \leq \overline{a \times b}.$$
