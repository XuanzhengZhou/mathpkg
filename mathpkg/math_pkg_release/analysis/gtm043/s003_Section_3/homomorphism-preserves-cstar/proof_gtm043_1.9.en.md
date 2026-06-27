---
role: proof
locale: en
of_concept: homomorphism-preserves-cstar
source_book: gtm043
source_chapter: "1"
source_section: "1.9"
---

We prove first that $t1 = 1$. Let $k \in C(Y)$ satisfy $tk = 1$; then
$$t1 = (tk)(t1) = t(k \cdot 1) = tk = 1.$$
It follows that $tn = n$ for each $n \in \mathbf{N}$.

Now, given $f \in C^*(X)$, we are to find $g \in C^*(Y)$ such that $tg = f$. Choose $h \in C(Y)$ for which $th = f$, and choose $n \in \mathbf{N}$ satisfying $|f| \leq n$. Now define
$$g = (-n \lor h) \land n.$$
Then $g \in C^*(Y)$, and, by Theorem 1.6,
$$tg = (-n \lor f) \land n = f.$$
