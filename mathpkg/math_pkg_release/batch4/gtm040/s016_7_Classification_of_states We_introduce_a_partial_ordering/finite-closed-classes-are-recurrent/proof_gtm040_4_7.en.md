---
role: proof
locale: en
of_concept: finite-closed-classes-are-recurrent
source_book: gtm040
source_chapter: "4"
source_section: "7. Classification of states"
---

**Proof:** Let the states of the class be the first $n$ positive integers, and suppose the class is transient. Then by Corollary 4-21, $N_{ij}$ is finite for every $i$ and $j$ in the class. Therefore,
$$c = M_i\left[\sum_{j=1}^{n} n_j\right] = \sum_{j=1}^{n} N_{ij}$$
is finite.

But $c$ is the mean total number of steps taken in the class starting from $i$. Since the class is closed, the process can never leave, so the total number of steps taken in the class is infinite with probability one. Therefore $c$ must be infinite, yielding a contradiction.

This contradiction shows that the class cannot be transient, hence it must be recurrent.
