---
role: proof
locale: en
of_concept: lemma-on-projections
source_book: gtm036
source_chapter: "5"
source_section: "5.10"
---

The straightforward proof of this lemma is omitted in the text. The argument proceeds as follows:

Define $\varphi: E \to R \times N$ by $\varphi(x) = (T(x), x - T(x))$. This map is clearly linear. Its inverse is given by $\psi: R \times N \to E$ with $\psi(r, n) = r + n$. To verify these are mutual inverses:

- For $x \in E$: $\psi(\varphi(x)) = T(x) + (x - T(x)) = x$.
- For $(r, n) \in R \times N$ with $r = T(y)$ for some $y$ and $n \in N$: $\varphi(\psi(r, n)) = \varphi(r + n) = (T(r + n), r + n - T(r + n)) = (T(r) + T(n), r + n - T(r) - T(n))$. Since $T$ is a projection, $T(r) = r$ (as $r \in R$) and $T(n) = 0$ (as $n \in N$). Thus $\varphi(r + n) = (r, n)$.

Hence $\varphi$ is a linear isomorphism. For continuity: $T$ is continuous by hypothesis, and the identity map $x \mapsto x$ is continuous, so $\varphi$ is continuous. Its inverse $\psi(r, n) = r + n$ is addition, which is continuous in a linear topological space. Thus $\varphi$ is a homeomorphism, hence a topological isomorphism.
