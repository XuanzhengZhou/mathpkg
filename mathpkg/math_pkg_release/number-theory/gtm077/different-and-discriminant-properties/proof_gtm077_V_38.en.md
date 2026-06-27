---
role: proof
locale: en
of_concept: different-and-discriminant-properties
source_book: gtm077
source_chapter: "V"
source_section: "§38"
---
# Proof of Theorem 101: Different and Discriminant Properties (Relative Case)

**Theorem 101** (originally from §36, extended to the relative case in §38). The set of numbers $\Delta$ in $K$ such that for each integer $A$ in $K$ the relative trace $S_k(\Delta A)$ is an integer forms an ideal $\mathfrak{M}$ in $K$. Furthermore,

$$\frac{1}{\mathfrak{M}} = \mathfrak{D}_k$$

is an integral ideal and is called the relative different of $K$ with respect to $k$.

**Proof (sketch, as the full proof in §36 carries over).** The proof that $\mathfrak{M}$ and $\mathfrak{D}_k$ are ideals runs parallel to that of the absolute case (Theorem 101 in §36).

Let $\omega_1, \ldots, \omega_n$ be an integral basis of $K$ (over $k(1)$). An element $\Delta \in K$ belongs to $\mathfrak{M}$ if and only if $S_k(\Delta \omega_i)$ is an integer in $k$ for $i = 1, \ldots, n$. Writing $\Delta = \sum x_j \omega_j^*$ where $\omega_j^*$ is the dual basis with respect to the relative trace form $S_k$, the condition becomes that the coefficients $x_j$ are integers in $k$. Since the change-of-basis matrix between the $\omega_i$ and the $\omega_j^*$ has determinant equal to the relative discriminant (up to a unit), we obtain that $\mathfrak{M}$ is a fractional ideal.

The inverse $\mathfrak{D}_k = \mathfrak{M}^{-1}$ is therefore an integral ideal. The fact that $\mathfrak{D}_k$ is indeed integral follows from the property that $S_k(1 \cdot A) = S_k(A)$ is integral for all integers $A$ in $K$ (since the relative trace of an integer is an integer in $k$), so $1 \in \mathfrak{M}$ and thus $\mathfrak{D}_k = \mathfrak{M}^{-1} \supseteq (1)$, i.e., $\mathfrak{D}_k$ is integral.

The definition in §38 reads:

> The set of numbers $\Delta$ in $K$, such that for each integer $A$ in $K$ the relative trace $S_k(\Delta A)$ is an integer forms an ideal $\mathfrak{M}$ in $K$. Furthermore, $1/\mathfrak{M} = \mathfrak{D}_k$ is an integral ideal and is called the relative different of $K$ with respect to $k$.

This is the relative analogue of the absolute different defined in §36, with the absolute trace $S$ replaced by the relative trace $S_k$, and the rational integers $\mathbb{Z}$ replaced by the ring of integers of $k$.
