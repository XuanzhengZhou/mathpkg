---
role: proof
locale: en
of_concept: lemma-0493ceec
source_book: gtm077
source_chapter: "38"
source_section: "Relative Norms of Numbers and Ideals, Relative Differents, and Relative Discriminants"
---
# Proof of Lemma (a)

**Statement.** If $A$ is an integer in $K$ such that $A\mathfrak{D}_k$ is integral, then $A$ can be represented in the form

$$A = \frac{B}{\Phi'(\theta)},$$

where $B$ is a number in $R_k(\theta)$. Consequently, $\Phi'(\theta)$ is divisible by $\mathfrak{D}_k$.

*Proof.* Let $\theta$ be an integer generating the field $K$ over $k$, and let $\Phi(x)$ be the irreducible polynomial over $k$ with leading coefficient $1$ which has $\theta$ as a root. The relative ring $R_k(\theta)$ consists of all numbers of the form

$$\alpha_0 + \alpha_1\theta + \cdots + \alpha_{m-1}\theta^{m-1}$$

where $\alpha_0, \ldots, \alpha_{m-1}$ run through all integers in $k$. The proof proceeds exactly as in §36 for the absolute case: one writes $A$ as a linear combination of the basis $1, \theta, \ldots, \theta^{m-1}$ with coefficients in $k$, then uses the defining property of the relative different $\mathfrak{D}_k$ (that $S_k(\Delta A)$ is integral for all integers $A$ precisely when $\Delta \in \mathfrak{D}_k^{-1}$) together with the trace relations for the basis elements. Solving the resulting linear system yields the representation $A = B/\Phi'(\theta)$ with $B \in R_k(\theta)$. The divisibility of $\Phi'(\theta)$ by $\mathfrak{D}_k$ follows immediately from this representation.
