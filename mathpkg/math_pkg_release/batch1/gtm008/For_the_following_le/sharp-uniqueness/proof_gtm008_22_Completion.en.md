---
role: proof
locale: en
of_concept: sharp-uniqueness
source_book: gtm008
source_chapter: "22"
source_section: "The Completion of a Boolean Algebra"
---

There are two complete monomorphisms:
$$j: B_{P_0} \rightarrow B_{P_1} \quad \text{associated with } f,$$
and the monomorphism associated with $\#$. Both induce the same complete monomorphism $i$ from $B_0$ to $B_1$.

For all $b_0 \in B_0$ and $b_1 \in B_1$, we have the equivalences:
$$\#(b_1) \leq b_0 \leftrightarrow b_1 \leq i(b_0) \leftrightarrow f(b_1) \leq b_0.$$

The first equivalence is Theorem 22.10(4). The second holds because $f$ induces $i$, meaning that the preimage under $f$ of the basic open $[b_0]$ is $[i(b_0)]$, so $f(b_1) \leq b_0 \leftrightarrow b_1 \leq i(b_0)$.

Since the order relation determines equality in a Boolean algebra, we conclude $\#(b_1) = f(b_1)$ for all $b_1 \in P_1$.
