---
role: proof
locale: en
of_concept: uniform-structure-completion-existence
source_book: gtm015
source_chapter: "2"
source_section: "24"
---

# Proof of Existence of uniform structure completion

This is a standard construction. Given a separated uniform structure $(X, \mathcal{U})$, one considers the set of all minimal Cauchy filters on $X$. Define $Y$ as the set of equivalence classes of Cauchy filters (where two Cauchy filters are equivalent if their intersection is also a Cauchy filter). For each entourage $U \in \mathcal{U}$, define an entourage $\hat{U}$ on $Y$ by: $(\mathcal{F}, \mathcal{G}) \in \hat{U}$ iff there exist sets $A \in \mathcal{F}$, $B \in \mathcal{G}$ with $A \times B \subset U$. The collection $\{\hat{U} : U \in \mathcal{U}\}$ forms a base for a uniform structure $\mathcal{V}$ on $Y$. Define $f: X \rightarrow Y$ by sending each $x \in X$ to the equivalence class of the principal filter at $x$.

Then (i) $f$ is injective because $\mathcal{U}$ is separated; (ii) $f(X)$ is dense in $Y$ by construction; (iii) $f: X \rightarrow f(X)$ is a unimorphism because $\hat{U} \cap [f(X) \times f(X)]$ corresponds precisely to $U$ under $(f \times f)^{-1}$. The space $(Y, \mathcal{V})$ is complete because every Cauchy filter in $X$ corresponds to a convergent filter in $Y$.
