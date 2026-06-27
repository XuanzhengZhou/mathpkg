---
role: proof
locale: en
of_concept: equivalent-characterizations-simple-generator
source_book: gtm013
source_chapter: "4"
source_section: "13"
---

(a) $\Leftrightarrow$ (c). This is clear by definition.

(a) $\Rightarrow$ (d). Assume $R$ has a simple left generator $T$. Let $I$ be a proper ideal of $R$. Then $I$ is contained in a maximal left ideal $L$ of $R$, and we have $R/L \cong T$. But clearly ${}_R T$ is faithful. So, since $IR \subseteq L$,
$$I \leq \ell_R(R/L) = \ell_R(T) = 0$$
and $R$ is simple. Since (a) $\Rightarrow$ (c), $R$ is semisimple.

(d) $\Rightarrow$ (b). If ${}_R R$ is a direct sum of simples, it must be a finite direct sum of simples (see Section 7), so ${}_R R$ is artinian (by (10.15)).

(b) $\Rightarrow$ (a). If $R$ is left artinian, then by (10.11) $R$ has a simple left generator.

The right-hand versions follow by symmetry. $\square$
