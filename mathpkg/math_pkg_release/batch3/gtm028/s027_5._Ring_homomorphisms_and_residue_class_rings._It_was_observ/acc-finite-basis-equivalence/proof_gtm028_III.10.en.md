---
role: proof
locale: en
of_concept: acc-finite-basis-equivalence
source_book: gtm028
source_chapter: "III"
source_section: "§10"
---

Suppose every submodule of $M$ has a finite basis. If $\{N_i\}$ is an ascending sequence of submodules of $M$, then the union $N$ (in the set-theoretic sense) of all $N_i$ is clearly a submodule of $M$. By hypothesis, $N$ has a finite basis, say $N = (x_1, x_2, \cdots, x_h)$. Since each $x_j$ is in $N$, it is in some $N_i$, hence there is an integer $n$ such that $x_j \in N_n$, $j = 1, \cdots, h$. Thus $N \subset N_n$, so that $N_i = N_n$ for $i > n$. Thus the a.c.c. is proved.

Conversely, let us assume the a.c.c. If $N$ is an arbitrary (but fixed) submodule of $M$, then in the collection of all submodules of $N$ having finite basis (such exist, for example, $(0)$) let $N'$ be a maximal element (Theorem 15). If $x$ is any element of $N$, then $N' + (x)$ has a finite basis, since $N'$ does. By the maximality of $N'$, $N' + (x) = N'$, so that $x \in N'$. Thus $N = N'$, and $N$ has a finite basis, as required.
