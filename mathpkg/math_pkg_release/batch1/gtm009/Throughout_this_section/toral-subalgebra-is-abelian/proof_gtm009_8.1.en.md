---
role: proof
locale: en
of_concept: toral-subalgebra-is-abelian
source_book: gtm009
source_chapter: "8"
source_section: "8.1"
---

Let $T$ be toral. We have to show that $\mathrm{ad}_T x = 0$ for all $x$ in $T$. Since $x$ is diagonalizable (ad $x$ being semisimple and $\mathbb{F}$ being algebraically closed), this amounts to showing that $\mathrm{ad}_T x$ has no nonzero eigenvalues. Suppose, on the contrary, that $[xy] = ay$ ($a \neq 0$) for some nonzero $y$ in $T$. Then $\mathrm{ad}_T y(x) = -ay$ is itself an eigenvector of $\mathrm{ad}_T y$, of eigenvalue $0$. On the other hand, we can write $x$ as a linear combination of eigenvectors of $\mathrm{ad}_T y$ ($y$ being semisimple also); after applying $\mathrm{ad}_T y$ to $x$, the term $-ay$ would have to be a linear combination of eigenvectors of eigenvalue $0$, which forces $a = 0$, contradiction. Therefore $\mathrm{ad}_T x = 0$ for all $x \in T$, so $T$ is abelian.
