---
role: proof
locale: en
of_concept: equalizer-as-limit
source_book: gtm026
source_chapter: "1"
source_section: "1.21"
---

Let $\Delta$ have nodes $\{t, u\}$ and edges $\alpha, \beta \in \Delta(t, u)$. A diagram $(\Delta, D)$ assigns objects $D_t = A$ and $D_u = B$ and morphisms $D_\alpha = f: A \to B$ and $D_\beta = g: A \to B$.

The set $F = \{t\}$ is final because $u \notin F$ and $\Delta(t, u) \neq \emptyset$. A lower bound relative to $F$ is a morphism $\psi_t = i: E \to A$ (to $D_t$) satisfying the commutativity condition: since edges $\alpha$ and $\beta$ go from $t$ to $u$, we require $i.f = i.g$. There is only one node in $F$, so no additional compatibility conditions between different nodes of $F$ arise.

Thus a lower bound relative to $\{t\}$ is exactly a morphism equalizing $f$ and $g$. The universal property for limits relative to $F$: for any other lower bound $(L', \psi')$ (i.e., any $i': E' \to A$ with $i'.f = i'.g$), there exists a unique $h: E' \to E$ such that $h.i = i'$. This is precisely the universal property of the equalizer. Hence limits of two-parallel-arrow diagrams are equalizers.
