---
role: proof
locale: en
of_concept: pseudocompact-square-counterexample
source_book: gtm043
source_chapter: "9"
source_section: "9.15"
---

First, we define a homeomorphism $\tau$ of $\beta N$ onto itself, as follows. As we saw in 6.10, $\beta N$ is the union of two disjoint copies of itself, $\beta N_1$ and $\beta N_2$. We choose any homeomorphism of $\beta N_1$ onto $\beta N_2$, and define $\tau$ to agree on $\beta N_1$ with this homeomorphism, and on $\beta N_2$ with its inverse. Thus, $\tau$ has no fixed point, and $\tau \circ \tau$ is the identity on $\beta N$.

The subspace $G$ will be defined inductively. Let $\mathcal{S}$ denote the family of all countably infinite subsets of $\beta N$. Since $|\beta N| = 2^{\mathfrak{c}}$, the family $\mathcal{S}$ can be well-ordered. One constructs $G$ by transfinite induction so that $G$ contains, for each $S \in \mathcal{S}$, a limit point of $S$ (ensuring countable compactness), while ensuring that $G$ does not contain both $p$ and $\tau p$ for any $p \in \beta N$.

The key property is that $G \times G$ contains the set
$$D = G \times G \cap \{(p, \tau p) : p \in \beta N\},$$
which is an infinite closed discrete subset of $G \times G$. Since $\{(p, \tau p) : p \in \beta N\}$ is the graph of the continuous mapping $\tau$, it is closed in $\beta N \times \beta N$ (6.13(c)). Therefore $D$ is closed in $G \times G$. The set $D$ is infinite and discrete because $G$ was constructed so that it never contains both $p$ and $\tau p$ for the same $p$. An infinite closed discrete set in a completely regular space witnesses that the space is not pseudocompact (one can construct an unbounded continuous function on it and extend by Tietze-Urysohn). Hence $G \times G$ is not pseudocompact.
