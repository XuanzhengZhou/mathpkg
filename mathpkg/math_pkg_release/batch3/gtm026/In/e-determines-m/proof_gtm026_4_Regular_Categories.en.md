---
role: proof
locale: en
of_concept: e-determines-m
source_book: gtm026
source_chapter: "4"
source_section: "Regular Categories"
---

Let $(e, m)$ be the $E$-$M$ factorization of $t$, so $t = e \cdot m$ with $e: C \longrightarrow \mathrm{Im}(t)$ in $E$ and $m: \mathrm{Im}(t) \longrightarrow D$ in $M$. Apply the diagonal fill-in hypothesis to the square:

$$\xymatrix{
C \ar[r]^{e} \ar[d]_{\mathrm{id}_C} & \mathrm{Im}(t) \ar[d]^{m} \\
C \ar[r]_{t} & D
}$$

which commutes because $e \cdot m = t = \mathrm{id}_C \cdot t$. By hypothesis, there exists $h: \mathrm{Im}(t) \longrightarrow C$ such that $e \cdot h = \mathrm{id}_C$. Since $e$ is an epimorphism (4.3), from $e \cdot h = \mathrm{id}_C$ we deduce that:

$h \cdot t = h \cdot e \cdot m = \mathrm{id}_{\mathrm{Im}(t)} \cdot m = m$ (using $h \cdot e = \mathrm{id}$ derived from $e \cdot h = \mathrm{id}$ and $e$ being epic).

Now compute $h \cdot e \cdot m = h \cdot t = m$. Since $e$ is epic, we have $h \cdot e = \mathrm{id}_{\mathrm{Im}(t)}$. Therefore $h$ is an isomorphism (with inverse $e$ restricted appropriately). Using axiom (4.4) (every isomorphism is in both $E$ and $M$) and axiom (4.2) ($M$ is a subcategory, hence closed under composition), we have:

$t = h^{-1} \cdot m \in M$.

(Here $h^{-1}$ denotes the inverse of the isomorphism $h$ restricted to the appropriate domain; by (4.4), $h^{-1} \in M$, and $m \in M$, so their composition $t$ is in $M$.)
