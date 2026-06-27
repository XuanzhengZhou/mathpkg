---
role: proof
locale: en
of_concept: lemma-0493ceec2a
source_book: gtm077
source_chapter: "V"
source_section: "§38"
---
# Proof of Lemma (a)

If $A$ is an integer in $K$ such that $A\mathfrak{D}_k$ is integral, then $A$ can be represented in the form

$$A = \frac{B}{\Phi'(\theta)},$$

where $B$ is a number in $R_k(\theta)$. Thus $\Phi'(\theta)$ is divisible by $\mathfrak{D}_k$.

**Proof.** The proof runs parallel to the proof of the corresponding lemma in §36 (absolute case). Let $\theta$ be an integer generating the field $K$ over $k$, and let $\Phi(x)$ be the irreducible polynomial over $k$ with leading coefficient $1$ which has the root $\theta$. The relative ring $R_k(\theta)$ is the set of all numbers

$$\alpha_0 + \alpha_1\theta + \cdots + \alpha_{m-1}\theta^{m-1}$$

where $\alpha_0, \ldots, \alpha_{m-1}$ run through all integers in $k$.

Let $\omega_1, \ldots, \omega_m$ be a basis of $R_k(\theta)$. If $A\mathfrak{D}_k$ is integral, then for every integer $\Delta$ in $K$, the relative trace $S_k(A\mathfrak{D}_k\Delta)$ is integral. In particular, for $\Delta$ ranging over the dual basis with respect to the trace form, we obtain a representation of $A$ as a $k$-linear combination of the dual basis elements with integral coefficients. The dual basis elements are precisely $\omega_i^* = \frac{\omega_i'}{\Phi'(\theta)}$ where the $\omega_i'$ are certain polynomials in $\theta$ with coefficients in $k$. Therefore

$$A = \frac{B}{\Phi'(\theta)}$$

with $B \in R_k(\theta)$. Consequently, $\Phi'(\theta) = B A^{-1}$ and since $A\mathfrak{D}_k$ is integral, we have $\mathfrak{D}_k \mid \Phi'(\theta)$.
