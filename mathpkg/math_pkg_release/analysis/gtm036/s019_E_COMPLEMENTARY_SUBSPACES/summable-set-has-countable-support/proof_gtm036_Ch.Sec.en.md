---
role: proof
locale: en
of_concept: summable-set-has-countable-support
source_book: gtm036
source_chapter: ""
source_section: ""
---

For each $n \in \mathbb{N}$, let $A_n = \{\alpha \in A : \|x_\alpha\| > 1/n\}$. By the Cauchy criterion, for $e = 1/n$, there is a finite set $B$ such that for any finite $C \subset A \setminus B$, $\|\sum_{\alpha \in C} x_\alpha\| < 1/n$. In particular, any singleton $\{\alpha\} \subset A \setminus B$ with $\|x_\alpha\| > 1/n$ would violate this (taking $C = \{\alpha\}$ gives $\|x_\alpha\| < 1/n$). Hence $A_n \subset B$, so each $A_n$ is finite. The support $\{\alpha : x_\alpha \neq 0\} = \bigcup_{n=1}^\infty A_n$ is thus countable.

For any enumeration $\alpha_1, \alpha_2, \dots$ of the support, let $s = \sum_{\alpha \in A} x_\alpha$ and $s_n = \sum_{r=1}^n x_{\alpha_r}$. By the Cauchy criterion, for any $e > 0$, there exists a finite $B \subset A$ such that for any finite $C \cap B = \emptyset$, $\|\sum_{\alpha \in C} x_\alpha\| < e$. Choose $N$ large enough that $B \subset \{\alpha_1, \dots, \alpha_N\}$. Then for $n \geq N$, $\|s - s_n\| \leq \|\sum_{\alpha \in \{\alpha_{n+1}, \dots\}} x_\alpha\| < e$, so $s_n \to s$.
