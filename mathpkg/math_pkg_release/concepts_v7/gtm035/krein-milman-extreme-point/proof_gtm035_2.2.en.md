---
role: proof
locale: en
of_concept: krein-milman-extreme-point
source_book: gtm035
source_chapter: "2"
source_section: "2.2"
---

# Proof of Krein-Milman Extreme Point Proposition

**Proposition 2.2 (Krein-Milman).** Let $B$ be a real Banach space and $B^*$ its dual space taken in the weak-$^*$ topology. Let $K$ be a nonempty compact convex subset of $B^*$. Then $K$ has an extreme point.

Recall: If $W$ is a real vector space, $S$ a subset of $W$, and $p$ a point of $S$, then $p$ is called an **extreme point** of $S$ provided

$$p = \frac{1}{2}(p_1 + p_2), \quad p_1, p_2 \in S \implies p_1 = p_2 = p.$$

## Proof

We give the proof for the case that $B$ is separable.

Let $\{L_n\}$ be a countable dense subset of $B$. For $y \in B^*$, put $L_n(y) = y(L_n)$.

Define

$$\ell_1 = \sup_{x \in K} L_1(x).$$

Since $K$ is compact and $L_1$ continuous, $\ell_1$ is finite and attained; i.e., there exists $x_1 \in K$ with $L_1(x_1) = \ell_1$.

Next, define

$$\ell_2 = \sup \{ L_2(x) : x \in K,\; L_1(x) = \ell_1 \}.$$

Again the supremum is taken over a compact set, so there exists $x_2 \in K$ with $L_2(x_2) = \ell_2$ and $L_1(x_2) = \ell_1$.

Continuing inductively, we obtain a sequence $\{x_n\} \subset K$ such that for each $n$:

$$L_1(x_n) = \ell_1,\; L_2(x_n) = \ell_2,\; \ldots,\; L_n(x_n) = \ell_n,$$

and

$$\ell_{n+1} = \sup \{ L_{n+1}(x) : x \in K,\; L_1(x) = \ell_1,\; \ldots,\; L_n(x) = \ell_n \}.$$

Let $x^*$ be an accumulation point of $\{x_n\}$ (which exists by compactness of $K$). Then $x^* \in K$ and $L_j(x^*) = \ell_j$ for all $j$, since $L_j(x_n) = \ell_j$ for all sufficiently large $n$.

We claim that $x^*$ is an extreme point of $K$. Suppose

$$x^* = \frac{1}{2}y_1 + \frac{1}{2}y_2, \quad y_1, y_2 \in K.$$

Then

$$\ell_1 = L_1(x^*) = \frac{1}{2}L_1(y_1) + \frac{1}{2}L_1(y_2).$$

Since $L_1(y_j) \leq \ell_1$ for $j = 1, 2$ (by definition of $\ell_1$), we must have $L_1(y_1) = L_1(y_2) = \ell_1$.

Similarly,

$$\ell_2 = L_2(x^*) = \frac{1}{2}L_2(y_1) + \frac{1}{2}L_2(y_2).$$

Since $L_1(y_1) = \ell_1$ and $y_1 \in K$, we have $L_2(y_1) \leq \ell_2$; similarly $L_2(y_2) \leq \ell_2$. Hence $L_2(y_1) = L_2(y_2) = \ell_2$.

Proceeding inductively, we obtain $L_n(y_1) = L_n(y_2) = \ell_n$ for all $n$. Since $\{L_n\}$ is dense in $B$, this implies $y_1 = y_2$ as elements of $B^*$. Thus $y_1 = y_2 = x^*$, and $x^*$ is an extreme point of $K$. $\square$
