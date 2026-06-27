---
role: proof
locale: en
of_concept: lemma-5-3-quasi-coherent-section-extension
source_book: gtm052
source_chapter: "II"
source_section: "5"
---

First we note that since $\mathcal{F}$ is quasi-coherent, $X$ can be covered by open affine subsets of the form $V = \operatorname{Spec} B$, such that $\mathcal{F}|_V \cong \tilde{M}$ for some $B$-module $M$. Now the open sets of the form $D(g)$ form a base for the topology of $X$ (see \S 2), so we can cover $V$ by open sets of the form $D(g)$, for various $g$.

(a) If $s \in \Gamma(X, \mathcal{F})$ restricts to $0$ on $D(f)$, then on each $D(g_i)$ in a covering, the restriction $s|_{D(g_i)}$ can be considered as an element of $M_{g_i}$. Since $f$ is invertible on $D(f)$, the vanishing condition means that for each $i$, the image of $s$ in the localization is zero, so $f^{n_i} s = 0$ in $M_{g_i}$ for some $n_i$. Choosing $n$ large enough to work for all $i$, we get $f^n s = 0$ globally.

(b) Given $t \in \mathcal{F}(D(f))$, we can write $t$ as an element of $M_f$ for some module $M$ on each affine piece. Then $t = m/f^k$ for some $m \in M$, and multiplying by a sufficiently high power of $f$ clears denominators, giving a global section. By taking $n$ large enough to work for all affine pieces in a covering, $f^n t$ extends to a global section.
