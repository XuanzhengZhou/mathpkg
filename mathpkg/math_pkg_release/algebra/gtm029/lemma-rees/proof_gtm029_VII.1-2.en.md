---
role: proof
locale: en
of_concept: lemma-rees
source_book: gtm029
source_chapter: "VII"
source_section: "1-2"
---

It was pointed out above that $R \subset K_0[y, 1/y]$. Now $K_0[y]$ is a polynomial ring over a field $K_0$ and is therefore integrally closed in its quotient field $K_0(y) = K$. The ring $K_0[y, 1/y]$ is the quotient ring of $K_0[y]$ with respect to the multiplicative system formed by the non-negative powers of $y$; this ring $K_0[y, 1/y]$ is therefore also integrally closed in $K$. (Vol. I, Ch. V, § 3, Example 2, p. 261.) Consequently $\bar{R} \subset K_0[y, 1/y] = \sum K_q$ by (3)]. Every element of $\bar{R}$ is therefore a sum of homogeneous elements. In particular, if $R_q = 0$ for all negative $q$, then $R \subset K_0[y]$ and therefore also $\bar{R} \subset K_0[y]$; thus in this special case, every element of $\bar{R}$ is a sum of homogeneous elements of non-negative degree.

Let

(4) $\xi = \xi_s + \xi_{s+1} + \cdots + \xi_t$

($\xi_q \in K_q, t \geq s$) be an element of $\bar{R}$. To complete the proof of the theorem we have only to show that each $\xi_q (q = s, s+1, \cdots, t)$ is itself an element of $\bar{R}$.

We shall first consider the case in which the ring $R$ is noetherian. Since $\bar{R} \subset \sum K_q$, every element of $\bar{R}$ can be written as a quotient of two elements of $\bar{R}$ such that the denominator is a homogeneous element. Since $\xi$ is integral over $R$, the ring $R[\xi]$ is a finite $R$-module. We can therefore find a homogeneous element $d$ in $R$, $d \neq 0$, such that $d.R[\xi] \subset R$. We have therefore, for every integer $i \geq

we denote by $A$ the smallest subring of $R$ containing the elements $x_i$. Then $A = J[x_1, x_2, \cdots, x_N]$ if $R$ is of characteristic zero ($J = \text{ring of integers}$) and $A = \mathcal{J}_p[x_1, x_2, \cdots, x_N]$ if $R$ is of characteristic $p \neq 0$ ($\mathcal{J}_p = \text{prime subfield of } R$). In either case $A$ is a noetherian integral domain. If we set $A_q = A \cap R_q$ then it is immediately seen that $A = \sum A_q$ and that consequently $A$ is a graded subring of $R$. In fact, if $\eta$ is any element of $A$, let $\eta_q$ be the homogeneous component of $\eta$, of a given degree $q$, and let $\eta = f(x_1, x_2, \cdots, x_N)$, where $f(X_1, X_2, \cdots, X_N)$ is a polynomial with coefficients which are integers or integers mod the characteristic $p$ of $R$. If $q_i$ denotes the degree of the homogeneous element $x_i$ of $R$ and $f_q(X_1, X_2, \cdots, X_N)$ denotes the sum of terms $cX_1^{i_1}X_2^{i_2} \cdots X_N^{i_N}$ in $f$ such that $i_1q_1 + i_2q_2 + \cdots + i_Nq_N = q(c \in J \text{ or } c \in \mathcal{J}_p)$, then it is clear that $\eta_q = f_q(x_1, x_2, \cdots, x_N)$ and hence $\eta_q \in A$.

Since the element $d$ and the products $\xi_q d$, $q = s, s + 1, \cdots, t$, are included in the set $\{x_1, x_2, \cdots, x_N\}$, it follows that $\xi$ belongs to the quotient field of $A$. On the other hand,
