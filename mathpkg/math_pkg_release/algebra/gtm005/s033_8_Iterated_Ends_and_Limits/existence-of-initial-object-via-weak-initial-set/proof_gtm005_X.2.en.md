---
role: proof
locale: en
of_concept: existence-of-initial-object-via-weak-initial-set
source_book: gtm005
source_chapter: "X"
source_section: "2. Weak Universality"
---

**Proof.** Let $F: S \hookrightarrow D$ be the inclusion of the small full subcategory. Since $D$ is small-complete and $S$ is small, the limit $\mu: v \to F$ exists in $D$. For every $d \in D$, choose an arrow $s \to d$ with $s \in S$ (possible because $S$ is weakly initial), and define $\gamma_d$ as the composite

$$\gamma_d: v \xrightarrow{\mu_s} s \to d.$$

We claim that $\gamma: v \to \mathrm{Id}_D$ is a cone. For any arrow $f: d \to d'$, form the pullback of $s \to d' \leftarrow s'$ with vertex $p$. Since $S$ is full and weakly initial, there is an arrow $v \xrightarrow{\mu_{s''}} s'' \to p$ for some $s'' \in S$. The two composite arrows $s'' \to p \to s$ and $s'' \to p \to s'$ are in $S$ because $S$ is full, the two upper quadrilaterals commute (since $\mu$ is a cone), and the pentagon commutes because $p$ is a pullback. Therefore the required square commutes, proving $\gamma$ is a cone.

If, in defining $\gamma$, we choose the arrow $v \to s \to s$ to be $\mu_s$ (i.e., identity on the second leg), then $\gamma$ satisfies $\gamma F = \mu$, the limiting cone of $F$. By Lemma 1 of Section 1, $v$ is initial in $D$.
