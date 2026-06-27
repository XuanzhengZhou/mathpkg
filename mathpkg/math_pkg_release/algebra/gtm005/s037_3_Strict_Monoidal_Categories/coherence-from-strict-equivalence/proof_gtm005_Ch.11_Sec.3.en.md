---
role: proof
locale: en
of_concept: coherence-from-strict-equivalence
source_book: gtm005
source_chapter: "XI"
source_section: "3. Strict Monoidal Categories"
---

Suppose that $v$ and $w$ are two tensor words in the objects $a_1, \ldots, a_n$ of $M$, with different arrangements of parentheses. Applying the strong monoidal functor $G : M \rightarrow S$ to these words yields two tensor words $Gv$ and $Gw$ in the strict monoidal category $S$. Since $S$ is strict, all associativity maps in $S$ are identities, and therefore $Gv = Gw$ as objects of $S$, with the identity arrow between them.

Now consider the coherence maps in $M$. For any two parenthesizations $v$ and $w$ of the same ordered list of objects, the strong monoidal structure of $G$ provides a comparison isomorphism

$$G(v(a_1, \ldots, a_n)) \cong Gv(G a_1, \ldots, G a_n)$$

in $S$. Since $S$ is strict, any two such parenthesizations are connected by a unique map -- the identity. Pulling back along the equivalence, this uniqueness lifts to $M$, establishing that there is exactly one canonical isomorphism $v(a_1, \ldots, a_n) \cong w(a_1, \ldots, a_n)$ in $M$ built from the associativity isomorphisms $\alpha$. Thus coherence for associativity holds in $M$.
