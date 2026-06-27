---
role: exercise
locale: en
chapter: "II"
section: "5"
exercise_number: 5.18
---

Vector Bundles. Let $Y$ be a scheme. A (geometric) vector bundle of rank $n$ over $Y$ is a scheme $X$ and a morphism $f: X \rightarrow Y$, together with additional data consisting of an open covering $\{U_i\}$ of $Y$, and isomorphisms $\psi_i: f^{-1}(U_i) \cong \mathbf{A}_{U_i}^n$, such that for any $i, j$, the automorphism $\psi_j \circ \psi_i^{-1}$ of $\mathbf{A}_{U_i \cap U_j}^n$ is linear in the affine coordinates.

(a) For any morphism $f: X \rightarrow Y$, a section of $f$ over an open set $U \subseteq Y$ is a morphism $s: U \rightarrow X$ such that $f \circ s = \operatorname{id}_U$. Show that if $f: X \rightarrow Y$ is a vector bundle of rank $n$, then the sheaf of sections $\mathcal{S}(X/Y)$ has a natural structure of $\mathcal{O}_Y$-module, which makes it a locally free $\mathcal{O}_Y$-module of rank $n$.

(b) Conversely, let $\mathcal{E}$ be a locally free sheaf of rank $n$ on $Y$, let $X = \mathbf{V}(\mathcal{E})$, and let $\mathcal{S} = \mathcal{S}(X/Y)$ be the sheaf of sections of $X$ over $Y$. Show that $\mathcal{S} \cong \mathcal{E}$.

