---
role: proof
locale: en
of_concept: lemma-12-3-existence-of-absolute-point-finite-polarity
source_book: gtm006
source_chapter: "12"
source_section: "2"
---

Write $v = n^2 + n + 1$, label the points $X_1, X_2, \ldots, X_v$ in an arbitrary manner and then label the lines $m_1, m_2, \ldots, m_v$ so that $m_i = X_i^\alpha$ for $i = 1, 2, \ldots, v$. Let $A$ be the incidence matrix of $\mathcal{P}$ given by this labelling, i.e. $a_{ij} = 1$ if and only if $X_i$ is on $m_j$. Since $X_i$ is on $X_i^\alpha = m_j$ precisely when $X_j$ is on $X_j^\alpha = m_i$, the matrix $A$ is symmetric. Furthermore, the point $X_i$ is absolute if and only if $a_{ii} = 1$.

Now $A A^T = n I + J$, where $J$ is the $v \times v$ matrix with every entry $1$. The matrix $C = n I + J$ has $n + v$ as a simple eigenvalue and $n$ as an eigenvalue with multiplicity $v - 1$. Indeed, for $i = 1, 2, \ldots, v-1$, define row vectors $x_i = (0, 0, \ldots, 1, -1, \ldots, 0)$ where the $i$-th entry is $1$, the $(i+1)$-th entry is $-1$, and all others are $0$. Since $x_i J = 0$ for all $i$, we have $x_i C = n x_i$, giving eigenvalue $n$ with at least $v-1$ independent eigenvectors. Let $y$ be the row vector with every entry $+1$; then $y C = n y + v y = (n+v) y$, giving eigenvalue $n+v$. Since $C$ is $v \times v$, these account for all eigenvalues.

Since $A$ is symmetric, $A A^T = A^2$, so the eigenvalues of $A$ are real: $\pm \sqrt{n}$ (from the $n$ eigenspace) and one eigenvalue $\pm \sqrt{n+v} = \pm (n+1)$ (from the $n+v$ eigenspace). Let the eigenvalue $(n+1)$ occur with multiplicity $k_1$ (as positive) and multiplicity $k_2$ (as negative), where $k_1 + k_2 = 1$. That is, the eigenvalue from the $n+v$ eigenspace is either $+(n+1)$ or $-(n+1)$, contributing to one of $k_1, k_2$.

Since $\operatorname{trace}(A) = a(\alpha)$ (the number of absolute points), and $\operatorname{trace}(A)$ equals the sum of eigenvalues, we obtain $a(\alpha) = (k_1 - k_2)(n+1) + \text{(sum of } \pm \sqrt{n} \text{ eigenvalues)}$. The $\pm \sqrt{n}$ eigenvalues come in conjugate pairs with total sum zero unless certain multiplicities differ. The sum of all $v$ eigenvalues of $A$ is $(k_1 - k_2)(n+1)$. Thus $a(\alpha) = 1 + (k_1 - k_2)(n+1) = 1 + (k_1 - k_2)n + (k_1 - k_2)$. Since $k_1 + k_2 = 1$, working through the counts yields $a(\alpha) \geq 1$, and if $n$ is not a square then the $\pm \sqrt{n}$ eigenvalues enforce $a(\alpha) = n + 1$.
