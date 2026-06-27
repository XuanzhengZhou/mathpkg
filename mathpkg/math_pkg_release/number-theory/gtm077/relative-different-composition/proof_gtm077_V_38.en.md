---
role: proof
locale: en
of_concept: relative-different-composition
source_book: gtm077
source_chapter: "V"
source_section: "§38"
---
# Proof of Theorem 111

**Theorem 111.** If $\mathfrak{D}$ and $\mathfrak{d}$ are the differents of $K$ and $k$ respectively, then for the relative different $\mathfrak{D}_k$ the relation

$$\mathfrak{D} = \mathfrak{D}_k \mathfrak{d}$$

holds.

**Proof.** The meaning of the relative different which already emerges from this simple equation (75) will become yet more evident from the following fact (Theorem 112), which can also serve as the definition of $\mathfrak{D}_k$.

Recall the definition: The set of numbers $\Delta$ in $K$ such that for each integer $A$ in $K$ the relative trace $S_k(\Delta A)$ is an integer forms an ideal $\mathfrak{M}$ in $K$. Furthermore,

$$\frac{1}{\mathfrak{M}} = \mathfrak{D}_k$$

is an integral ideal and is called the relative different of $K$ with respect to $k$.

The proof that $\mathfrak{M}$ and $\mathfrak{D}_k$ are ideals runs parallel to that of Theorem 101 (the absolute case, §36).

For the chain rule itself: If $\Delta$ is a number in $K$ such that $\Delta \mathfrak{D}_k \mathfrak{d}$ is integral, then for any integer $A$ in $K$, the number

$$S(\Delta A) = s(S_k(\Delta A))$$

is a rational integer. Here $S$ is the absolute trace from $K$ to $k(1)$, and $s$ is the absolute trace from $k$ to $k(1)$. The transitivity formula $S = s \circ S_k$ follows from Theorem 59. Since $S_k(\Delta A)$ is an integer in $k$ (because $\Delta \mathfrak{D}_k$ is integral by hypothesis), it follows that $S(\Delta A)$ is integral, hence $\Delta \mathfrak{D}$ is integral. This establishes $\mathfrak{D} = \mathfrak{D}_k \mathfrak{d}$.
