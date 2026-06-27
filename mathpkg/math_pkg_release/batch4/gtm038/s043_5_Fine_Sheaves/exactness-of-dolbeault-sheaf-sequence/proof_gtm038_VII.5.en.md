---
role: proof
locale: en
of_concept: exactness-of-dolbeault-sheaf-sequence
source_book: gtm038
source_chapter: "VII"
source_section: "5. Fine Sheaves (Theorems of Dolbeault and de Rham)"
---

**Proof.** The exactness is verified at each stalk.

1. **Exactness at $\Omega^p$:** The map $\varepsilon$ is an injection by definition, since holomorphic forms are in particular smooth forms.

2. **Exactness at $\mathcal{A}^{p,0}$:** Let $\sigma \in \mathcal{A}^{p,0}_x$ satisfy $d''\sigma = 0$. Choose a neighborhood $U$ of $x$ and a representative $\varphi \in A^{p,0}(U)$ with $\sigma = r\varphi(x)$. Then $d''\sigma = r(d''\varphi)(x) = 0$ implies $d''\varphi = 0$ near $x$, so without loss of generality on $U$. By the local $d''$-Poincaré lemma (Dolbeault lemma), $d''\varphi = 0$ means that $\varphi$ is holomorphic near $x$, hence $\sigma \in \Omega^p_x$. Conversely, if $\sigma \in \Omega^p_x$, then $d''\sigma = 0$ by holomorphy. Thus $\operatorname{Ker} d'' = \operatorname{Im} \varepsilon$ at $\mathcal{A}^{p,0}_x$.

3. **Exactness at $\mathcal{A}^{p,q}$ for $q \geqslant 1$:** Let $\sigma \in \mathcal{A}^{p,q}_x$, $U$ a neighborhood of $x$, and $\varphi \in A^{p,q}(U)$ be such that $\sigma = r\varphi(x)$. If $d''\sigma = 0$, then $r(d''\varphi)(x) = 0$, so $d''\varphi = 0$ near $x$, and without loss of generality on $U$. By the Dolbeault lemma, there exists a neighborhood $U'(x) \subset U$ and a form $\psi \in A^{p,q-1}(U')$ with $d''\psi = \varphi|_{U'}$. Then $\sigma = r\varphi(x) = r(d''\psi)(x) = d''(r\psi)(x)$, showing $\sigma \in \operatorname{Im} d''$. Conversely, $d'' \circ d'' = 0$ gives $\operatorname{Im} d'' \subset \operatorname{Ker} d''$. Hence the sequence is exact at every $\mathcal{A}^{p,q}$.
