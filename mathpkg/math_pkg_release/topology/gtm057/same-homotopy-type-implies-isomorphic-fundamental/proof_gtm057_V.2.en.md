---
role: proof
locale: en
of_concept: same-homotopy-type-implies-isomorphic-fundamental
source_book: gtm057
source_chapter: "V"
source_section: "2"
---

If $X$ and $Y$ are of the same homotopy type, there exist maps $f: X \to Y$ and $g: Y \to X$ such that $gf \simeq 1_X$ and $fg \simeq 1_Y$. Then $(gf)_* = g_* f_* \simeq (1_X)_* = 1_{\pi(X)}$, and similarly $f_* g_* \simeq 1_{\pi(Y)}$. By Lemma (1.2) (or directly from the properties of homotopic maps), homotopic maps induce the same homomorphism on fundamental groups (up to conjugation by a path). More precisely, if $H: X \times I \to X$ is a homotopy from $1_X$ to $gf$, then for each $p$, the path $t \mapsto H(p,t)$ gives a conjugation isomorphism, so $g_* f_*$ is an isomorphism. Hence $f_*$ is injective and $g_*$ is surjective; by symmetry, $f_*$ and $g_*$ are isomorphisms.
