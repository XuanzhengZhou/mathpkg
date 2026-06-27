---
role: proof
locale: en
of_concept: flat-family-hilbert-polynomial-constancy
source_book: gtm052
source_chapter: "III"
source_section: "9"
---

(i) $\Rightarrow$ (ii). We compute $H^i(X, \mathcal{F}(m))$ by Čech cohomology using the standard open affine cover $\mathfrak{U}$ of $X$. Then

$$H^i(X, \mathcal{F}(m)) = h^i(C^\bullet(\mathfrak{U}, \mathcal{F}(m))).$$

Since $\mathcal{F}$ is flat, each term $C^i(\mathfrak{U}, \mathcal{F}(m))$ of the Čech complex is a flat $A$-module. On the other hand, if $m \gg 0$, then $H^i(X, \mathcal{F}(m)) = 0$ for $i > 0$, by (5.2). Thus the complex $C^\bullet(\mathfrak{U}, \mathcal{F}(m))$ is a resolution of the $A$-module $H^0(X, \mathcal{F}(m))$: we have an exact sequence

$$0 \rightarrow H^0(X, \mathcal{F}(m)) \rightarrow C^0(\mathfrak{U}, \mathcal{F}(m)) \rightarrow C^1(\mathfrak{U}, \mathcal{F}(m)) \rightarrow \ldots \rightarrow C^n(\mathfrak{U}, \mathcal{F}(m)) \rightarrow 0.$$

Splitting this into short exact sequences, using (9.1Ae) and the fact that the $C^i$ are all flat, we conclude that $H^0(X, \mathcal{F}(m))$ is a flat $A$-module. But it is also finitely generated (5.2), and hence free of finite rank by (9.1Af).

(ii) $\Rightarrow$ (i). Let $S = A[x_0, \ldots, x_n]$, and let $M$ be the graded $S$-module

$$M = \bigoplus_{m \geqslant m_0} H^0(X, \mathcal{F}(m)).$$

Then $M$ is a finitely generated $S$-module, and $\mathcal{F} = \widetilde{M}$. For $m \gg 0$, $H^0(X, \mathcal{F}(m)) = M_m$. The hypothesis (ii) says that $M_m$ is a flat $A$-module, and hence free over $A$ of finite rank.

(iii) $\Rightarrow$ (ii). According to (II, 8.9) we can check the freeness of $H^0(X, \mathcal{F}(m))$ by comparing its rank at the generic point and the closed point of $T$. Hence the argument of (ii) $\Rightarrow$ (iii) above is reversible.

Thus all three conditions are equivalent.
