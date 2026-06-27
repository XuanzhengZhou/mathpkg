---
role: proof
locale: en
of_concept: weak-mackey-continuity-openness-dual
source_book: gtm036
source_chapter: "21"
source_section: "21.3"
---

**Proof of (i):** If $T$ is weakly continuous, then there is a dual $T'$ of $T$, $T'$ is automatically weakly continuous, and the image under $T'$ of a weakly compact subset of $H$ is therefore weakly compact. Therefore, by the criterion 21.3(i), $T$ is Mackey continuous. Conversely, if $T$ is Mackey continuous, then for each $h$ in $H$ the functional $x \mapsto \langle T(x),h \rangle$ is Mackey continuous, and is hence represented by a member of $F$ (theorem 18.8). Therefore $x \mapsto \langle T(x),h \rangle$ is weakly continuous for every $h$ in $H$, and, by theorem 21.1, $T$ is weakly continuous.

**Proof of (ii):** First assume that $T'$ exists and the range of $T'$ is weakly closed. In view of 21.3(iii), $T$ is weakly relatively open if for each finite subset $A$ of $F$ there is a finite subset $B$ of $T'[H]$ such that $A_0^\circ \cap T'[H] \subset B_0^\circ$, and the latter is easily seen to be the case (see the proof of 16.11(ii)). The existence of $T'$ implies the weak continuity of $T$ (21.1). Conversely, if $T$ is weakly continuous and relatively open, then 21.3(ii) implies that the range of $T'$ is weakly closed.

**Proof of (iii):** If $T$ is weakly continuous and open, then by (ii) the range of $T'$ is weakly closed, and the openness implies that $T'$ is injective and its inverse (on the range) is weakly continuous, so $T'$ is a weak topological isomorphism onto a weakly closed subspace. The converse follows from similar reasoning using 21.3.

**Proof of (iv):** By (i), Mackey continuity is equivalent to weak continuity. The "open" part follows from the equivalence of Mackey and weak topologies on equicontinuous sets and the fact that Mackey-openness of $T$ implies weak openness under the separation hypotheses.

**Proof of (v):** Proposition (v) is a direct application of 21.3(i) to the strong topologies of $H$ and $F$.
