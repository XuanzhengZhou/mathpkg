---
role: proof
locale: en
of_concept: kernel-pair-coequalizer
source_book: gtm026
source_chapter: "1"
source_section: "1.53"
---

We assume that $p = \operatorname{coeq}(a', b')$ for some $a', b': E' \longrightarrow A$.

Let $a, b: E \longrightarrow A$ be the kernel pair of $p$. Suppose $p'$ is given with $a \cdot p' = b \cdot p'$. Since $a' \cdot p = b' \cdot p$ (because $p$ coequalizes $a', b'$), there exists a unique $g$ with $g \cdot a = a'$ and $g \cdot b = b'$ by the universal property of the kernel pair $(E, a, b)$ applied to $E'$ with morphisms $a', b'$.

Now $a' \cdot p' = (g \cdot a) \cdot p' = g \cdot (a \cdot p') = g \cdot (b \cdot p') = (g \cdot b) \cdot p' = b' \cdot p'$. Since $p = \operatorname{coeq}(a', b')$, there exists a unique $h$ with $p \cdot h = p'$. This shows that $p$ has the universal property of the coequalizer of $(a, b)$, so $p = \operatorname{coeq}(a, b)$.
