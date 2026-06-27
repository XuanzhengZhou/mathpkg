---
role: proof
locale: en
of_concept: coequalizer-mono-factorization-uniqueness
source_book: gtm026
source_chapter: "1"
source_section: "1.49"
---

Suppose $p \cdot i = f = p' \cdot i'$ with $p, p'$ coequalizers and $i, i'$ monomorphisms. There exist $a, b$ with $p = \operatorname{coeq}(a, b)$. As $a \cdot p' \cdot i' = a \cdot p \cdot i = b \cdot p \cdot i = b \cdot p' \cdot i'$ and $i'$ is mono, we have $a \cdot p' = b \cdot p'$. Since $p$ is the coequalizer of $(a, b)$, there exists a unique $g$ such that $p \cdot g = p'$. Since $p$ is epi (every coequalizer is an epimorphism), we also have $g \cdot i' = i$.

Symmetrically, there exists $h: I' \longrightarrow I$ with $p' \cdot h = p$ and $h \cdot i = i'$. Either because $p$ is epi or $i$ is mono, we obtain $g \cdot h = \operatorname{id}_I$. Symmetrically, $h \cdot g = \operatorname{id}_{I'}$. Thus $g$ and $h$ are mutually inverse isomorphisms, establishing the uniqueness of the factorization up to isomorphism.
