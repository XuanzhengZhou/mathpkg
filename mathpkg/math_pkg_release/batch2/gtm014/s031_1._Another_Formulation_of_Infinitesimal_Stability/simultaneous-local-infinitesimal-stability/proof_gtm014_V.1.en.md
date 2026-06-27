---
role: proof
locale: en
of_concept: simultaneous-local-infinitesimal-stability
source_book: gtm014
source_chapter: "V"
source_section: "§1"
---

**Proof of Proposition 1.5.** For $S$ consisting of a single point this result is given by Corollary 1.3.

The proof for general $S$ is exactly as in the single point case except that we substitute Lemma 1.4 and the subsequent remark for the Generalized Malgrange Preparation Theorem. In particular, choose coordinates on $X$ at $p_1,\ldots,p_k$ (with disjoint domains) and coordinates on $Y$ at $q$, and write down the equations generalizing $(**)$ to solve the local infinitesimal stability condition simultaneously to order $m$ at $p_1,\ldots,p_k$.

Let
\[
M_f^S = \bigoplus_{i=1}^{k} M_f^{p_i},
\]
where $M_f^{p_i} = C^\infty(f^*TY)_{p_i} / (df)C^\infty(TX)_{p_i}$ as before. Then $M_f^S$ is a $C_S^\infty(X)$-module, and via $f^*$ it becomes a $C_q^\infty(Y)$-module. The condition of simultaneous solvability to order $m$ asserts that $M_f^S$ is finitely generated over $C_q^\infty(Y)$. By Lemma 1.4, this is equivalent to each $M_f^{p_i}$ being finitely generated over $C_q^\infty(Y)$, which by Corollary 1.3 is equivalent to the jet-space equality at each $p_i$. Summing these equalities gives the stated jet-space equality over $S$. $\square$
