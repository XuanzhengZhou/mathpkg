---
role: exercise
locale: en
chapter: "1"
section: "2"
exercise_number: 16
---

Let $M$ be a left $R$-module. Let $\mathcal{L}_R(M) = \{l_R(X) \mid X \subseteq M\}$ and $\mathcal{R}_M(R) = \{r_M(A) \mid A \subseteq R\}$. Observe that $A \in \mathcal{L}_R(M)$ if and only if $A = l_R r_M(A)$, and $X \in \mathcal{R}_M(R)$ if and only if $X = r_M l_R(X)$. Now prove that:

(1) Both $\mathcal{L}_R(M)$ and $\mathcal{R}_M(R)$ are closed under arbitrary intersections, whence as posets partially ordered by set inclusion $\mathcal{L}_R(M)$ and $\mathcal{R}_M(R)$ are complete lattices. Moreover, if $\mathcal{A} \subseteq \mathcal{L}_R(M)$ and $\mathcal{X} \subseteq \mathcal{R}_M(R)$, then

$$\inf \mathcal{A} = \bigcap \mathcal{A}, \quad \sup \mathcal{A} = l_R\!\left(r_M\!\left(\sum \mathcal{A}\right)\right),$$

$$\inf \mathcal{X} = \bigcap \mathcal{X}, \quad \sup \mathcal{X} = r_M\!\left(l_R\!\left(\sum \mathcal{X}\right)\right).$$

(2) The maps $l_R$ and $r_M$ induce a lattice anti-isomorphism between $\mathcal{L}_R(M)$ and $\mathcal{R}_M(R)$.
