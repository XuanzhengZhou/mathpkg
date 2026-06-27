---
role: proof
locale: en
of_concept: composition-of-coequalizers
source_book: gtm026
source_chapter: "1"
source_section: "1.4"
---

We prove (2) first. Let $g = p \cdot i$ be a coequalizer-mono factorization, and then let $f \cdot p = p' \cdot i'$ be a coequalizer-mono factorization. As $p' \cdot (i' \cdot i)$ is a coequalizer-mono factorization of $f \cdot g$, $i' \cdot i$ is an isomorphism by 1.49. Since $i$ is both split epi and mono, it follows from 1.50 that $i$ is an isomorphism.

To prove (1), let $f = \text{coeq}(a, b)$ and let $p \cdot i$ be a coequalizer-mono factorization of $f \cdot g$. Since $i$ is mono we have $a \cdot p = b \cdot p$ which induces unique $h$ with $f \cdot h = p$. As $f$ is epi, $h \cdot i = g$. By (2), $i$ is a coequalizer and hence, by 1.50, an isomorphism. $\square$
