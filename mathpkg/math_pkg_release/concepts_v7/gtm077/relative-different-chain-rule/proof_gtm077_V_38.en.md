---
role: proof
locale: en
of_concept: relative-different-chain-rule
source_book: gtm077
source_chapter: "V"
source_section: "§38"
---
# Proof of Theorem 111: Chain Rule for Differents

**Theorem 111.** If $\mathfrak{D}$ and $\mathfrak{d}$ are the differents of $K$ and $k$ respectively, then for the relative different $\mathfrak{D}_k$ the relation

$$\mathfrak{D} = \mathfrak{D}_k \mathfrak{d}$$

holds.

**Proof.** Let $\Delta$ be a number in $K$ such that $\Delta \mathfrak{D}_k$ is integral. By definition of the relative different, this means that for every integer $A$ in $K$, the relative trace $S_k(\Delta A)$ is an integer in $k$.

Now consider the absolute trace $S(\Delta A)$. By Theorem 59 (transitivity of the trace),

$$S(\Delta A) = s(S_k(\Delta A)),$$

where $s$ denotes the trace from $k$ to $k(1)$ (the rational numbers). Since $S_k(\Delta A)$ is an integer in $k$, its absolute trace $s(S_k(\Delta A))$ is a rational integer. Therefore $\Delta$ also satisfies the condition that for all integers $A$ in $K$, $S(\Delta A)$ is integral — which means $\Delta \mathfrak{D}$ is integral, where $\mathfrak{D}$ is the absolute different of $K$.

Conversely, if $\Delta \mathfrak{D}$ is integral, then for all integers $A$ in $K$, $S(\Delta A)$ is an integer. But $S(\Delta A) = s(S_k(\Delta A))$. Since this holds for all $A$, and $s$ is a non-degenerate trace form on $k$, it follows that $S_k(\Delta A)$ must be integral in $k$ for all $A$. Hence $\Delta \mathfrak{D}_k \mathfrak{d}$ is integral.

The reciprocal relationship between these integrality conditions yields $\mathfrak{D} = \mathfrak{D}_k \mathfrak{d}$.
