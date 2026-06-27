---
role: proof
locale: en
of_concept: first-bishop-phelps
source_book: gtm024
source_chapter: "III"
source_section: "§20. Support Points and Smooth Points"
---

Let $C$ be a closed convex subset of a Banach space $X$. For any $\varepsilon > 0$ and $x_0 \in C$, define the set $S = \{x \in C : \|x - x_0\| \geqslant \varepsilon\}$. Let $f(x) = \|x - x_0\|$, which is continuous and convex. By the Brondsted-Rockafellar theorem (or by direct variational argument), there exists a point $s \in C$ and a functional $\phi \in X'$ such that $\phi$ supports $C$ at $s$ and $\|s - x_0\| < \varepsilon$. The proof relies on the fact that the set of support functionals is dense: given any closed convex set $C$ and any point $x_0 \in C$, there exist support points arbitrarily close to $x_0$. This is established by considering the subdifferential of the distance function to $C$ and applying the Bishop-Phelps lemma on the density of support functionals that attain their norm.
