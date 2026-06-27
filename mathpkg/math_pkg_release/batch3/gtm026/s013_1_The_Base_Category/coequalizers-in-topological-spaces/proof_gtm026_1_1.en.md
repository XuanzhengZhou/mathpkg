---
role: proof
locale: en
of_concept: coequalizers-in-topological-spaces
source_book: gtm026
source_chapter: "1"
source_section: "1. The Base Category"
---

Construct the set-theoretic coequalizer $q_{\mathbf{Set}}: B \to Q$ as in 1.30: let $R$ be the intersection of all equivalence relations on $B$ containing $\{(f(a), g(a)) : a \in A\}$, set $Q = B/R$, and let $q_{\mathbf{Set}}$ be the canonical projection. Endow $Q$ with the quotient topology: $U \subseteq Q$ is open iff $q_{\mathbf{Set}}^{-1}(U)$ is open in $B$. Set $q = q_{\mathbf{Set}}$ as a continuous map.

Then $q \circ f = q \circ g$ as in the set-theoretic case. For any continuous $q': B \to Q'$ with $q' \circ f = q' \circ g$, the set-theoretic construction yields a unique function $h: Q \to Q'$ with $q \circ h = q'$. To verify continuity of $h$: for any open $V \subseteq Q'$, $q'^{-1}(V)$ is open in $B$ (continuity of $q'$), and $q'^{-1}(V) = q^{-1}(h^{-1}(V))$ since $q \circ h = q'$. By definition of the quotient topology, $h^{-1}(V)$ is open in $Q$. Thus $h$ is continuous and is the unique morphism in $\mathbf{Top}$ satisfying $q \circ h = q'$.
