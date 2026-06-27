---
role: proof
locale: en
of_concept: exactness-of-dolbeault-sheaf-sequence
source_book: gtm038
source_chapter: "VII"
source_section: "5. Fine Sheaves (Theorems of Dolbeault and de Rham)"
---

**Theorem (Exactness of the Dolbeault sequence).** The sequence of sheaves

$$0 \to \mathcal{O} \to \mathcal{A}^{0,0} \xrightarrow{d''} \mathcal{A}^{0,1} \xrightarrow{d''} \cdots \xrightarrow{d''} \mathcal{A}^{0,n} \to 0$$

is exact, where $\mathcal{O}$ is the sheaf of holomorphic functions and $\mathcal{A}^{p,q}$ is the sheaf of $\mathcal{C}^{\infty}$ differential forms of type $(p,q)$.

**Proof.** The inclusion $\mathcal{O} \hookrightarrow \mathcal{A}^{0,0}$ is the natural one. The kernel of $d'': \mathcal{A}^{0,0} \to \mathcal{A}^{0,1}$ consists precisely of functions $f$ with $\partial f/\partial \bar{z}_v = 0$ for all $v$, i.e., holomorphic functions. Thus the sequence is exact at $\mathcal{A}^{0,0}$.

For $q \geq 1$, Dolbeault's Lemma (Theorem 4.1) states that every $d''$-closed form of type $(p,q)$ on a polycylinder is $d''$-exact. Since exactness of a sequence of sheaves is a local property, and every point has a neighborhood basis of polycylinders, Dolbeault's Lemma implies $\ker d'' = \operatorname{im} d''$ at each stalk for $q \geq 1$. Hence the sequence is exact everywhere.
