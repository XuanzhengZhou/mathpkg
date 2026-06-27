---
role: proof
locale: en
of_concept: theorem-111
source_book: gtm077
source_chapter: "38"
source_section: "Relative Norms of Numbers and Ideals, Relative Differents, and Relative Discriminants"
---
# Proof of Theorem 111

**Statement.** If $\mathfrak{D}$ and $\mathfrak{d}$ are the differents of $K$ and $k$ respectively, then for the relative different $\mathfrak{D}_k$ the relation

$$\mathfrak{D} = \mathfrak{D}_k \mathfrak{d}$$

holds.

*Proof.* Let $S$, $s$, and $S_k$ denote the trace from $K$ to $\mathbb{Q}$, the trace from $k$ to $\mathbb{Q}$, and the relative trace from $K$ to $k$, respectively. By the transitivity of the trace (Theorem 59),

$$S(A) = s(S_k(A))$$

for any $A \in K$.

Recall that the different $\mathfrak{D}$ is defined as the inverse of the ideal $\mathfrak{M} = \{ \Delta \in K : S(\Delta A) \text{ is integral for all integers } A \in K \}$. Similarly, $\mathfrak{d}$ is the inverse of $\{ \delta \in k : s(\delta \alpha) \text{ is integral for all integers } \alpha \in k \}$, and $\mathfrak{D}_k$ is the inverse of $\{ \Delta \in K : S_k(\Delta A) \text{ is integral for all integers } A \in K \}$.

Now, if $\Delta \in \mathfrak{D}^{-1}$, then $S(\Delta A)$ is integral for all integers $A \in K$. Writing $S = s \circ S_k$, this means $s(S_k(\Delta A))$ is integral. This condition can be analyzed through the tower property: for $\Delta$ to belong to $\mathfrak{D}^{-1}$, we need $S_k(\Delta A)$ to be such that its trace down to $\mathbb{Q}$ is always integral. This happens exactly when $S_k(\Delta A) \in \mathfrak{d}^{-1}$, which is equivalent to $\Delta \in \mathfrak{D}_k^{-1} \mathfrak{d}^{-1}$. Therefore

$$\mathfrak{D}^{-1} = \mathfrak{D}_k^{-1} \mathfrak{d}^{-1},$$

and taking inverses yields $\mathfrak{D} = \mathfrak{D}_k \mathfrak{d}$.
