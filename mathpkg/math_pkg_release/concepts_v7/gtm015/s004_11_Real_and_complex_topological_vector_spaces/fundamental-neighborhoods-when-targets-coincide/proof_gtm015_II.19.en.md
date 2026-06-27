---
role: proof
locale: en
of_concept: fundamental-neighborhoods-when-targets-coincide
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "19. Initial topologies"
---

# Proof of Fundamental System of Neighborhoods for Coinciding Target TVS

**Theorem (19.6).** If $E$ is a vector space over $\mathbb{K}$, $G$ is a TVS over $\mathbb{K}$, and $f_\iota : E \to G$ ($\iota \in I$) is a family of linear mappings, then the initial TVS topology on $E$ has as a fundamental system of neighborhoods of $\theta$ the sets

$$\bigcap_{\iota \in J} f_\iota^{-1}(V),$$

where $J$ is a finite subset of $I$ and $V$ is a neighborhood of $\theta$ in $G$.

*Proof.* In the general case (where the target spaces may differ), a basic neighborhood of $\theta$ in the initial topology is given by

$$\bigcap_{\iota \in J} f_\iota^{-1}(V_\iota),$$

where $J$ is a finite subset of $I$ and, for each $\iota \in J$, $V_\iota$ is a neighborhood of $\theta$ in the target space of $f_\iota$.

Since all target spaces coincide (each $f_\iota$ maps into the same TVS $G$), we can set

$$V = \bigcap_{\iota \in J} V_\iota,$$

which is also a neighborhood of $\theta$ in $G$ (as a finite intersection of neighborhoods). Then

$$\bigcap_{\iota \in J} f_\iota^{-1}(V) \subset \bigcap_{\iota \in J} f_\iota^{-1}(V_\iota),$$

so the sets $\bigcap_{\iota \in J} f_\iota^{-1}(V)$ form a fundamental system of neighborhoods of $\theta$ in $E$ (since every basic neighborhood of the original form contains one of the simplified form). $\square$
