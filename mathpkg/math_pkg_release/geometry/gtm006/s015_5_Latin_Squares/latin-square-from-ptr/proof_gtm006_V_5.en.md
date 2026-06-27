---
role: proof
locale: en
of_concept: latin-square-from-ptr
source_book: gtm006
source_chapter: "V"
source_section: "5"
---

**Proof of Lemma 5.7.**

(1) We first show that $\{x\}$ is a Latin square. For fixed row $i$, the entries in columns $j$ and $k$ are $T(x,i,j)$ and $T(x,i,k)$ respectively. By axiom (D) of Theorem 5.1 (the planar ternary ring axioms), $T(x,i,j) = T(x,i,k)$ if and only if $j = k$. Thus every row contains each element of $R$ at most once; since there are $n$ columns, each row is a permutation of $R$. For fixed column $j$, consider $T(x,i,j) = T(x,k,j)$ with $i \neq k$. By axiom (C) of Theorem 5.1, there exists a unique $x$ satisfying this equality. If $x = 0$, then $T(0,i,j) = j = T(0,k,j)$ for all $i,k$, which would contradict uniqueness. Hence for $x \neq 0$, the equality $T(x,i,j) = T(x,k,j)$ implies $i = k$. Thus every column also contains each element exactly once. Therefore $\{x\}$ is a Latin square.

(2) We now show that $\{x\}$ and $\{y\}$ are orthogonal when $x \neq y$. Suppose that the ordered pair $(T(x,i,j), T(y,i,j))$ equals $(T(x,p,q), T(y,p,q))$ for two positions $(i,j)$ and $(p,q)$. By the definition of a PTR and its axioms, this forces $(i,j) = (p,q)$. Consequently, the $n^2$ ordered pairs obtained by superimposing $\{x\}$ and $\{y\}$ are all distinct. Since there are exactly $n^2$ possible ordered pairs, every pair must occur exactly once. Hence $\{x\}$ is orthogonal to $\{y\}$.

The construction produces $n-1$ squares $\{x\}$ for $x = 1, 2, \dots, n-1$, each of which is a Latin square and pairwise orthogonal. Together with the trivial square $\{0\}$ defined by $T(0,i,j) = j$, this yields a complete set of $n-1$ mutually orthogonal Latin squares of order $n$.
