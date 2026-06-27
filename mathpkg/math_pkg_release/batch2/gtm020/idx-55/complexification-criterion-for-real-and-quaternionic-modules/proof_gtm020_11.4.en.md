---
role: proof
locale: en
of_concept: complexification-criterion-for-real-and-quaternionic-modules
source_book: gtm020
source_chapter: "11"
source_section: "11"
---

Decompose $M$ as the direct sum $M_1 \oplus \cdots \oplus M_r$ where $u^2$ has the eigenvalue $\lambda_i$ on $M_i$. The $\lambda_i$ are real, and we can suppose that $\lambda_i \neq \lambda_j$ for $i \neq j$. This implies that $\eta(M_i, M_j) = 0$ for $i \neq j$. The relation $u^2(x) = \lambda_i x$ yields the relation $u^2(u(x)) = \lambda_i u(x)$, and we have $u(M_i) \subset M_i$. Since
$$\eta(u(x), u(x)) = \varepsilon \eta(u^2(x), x) = \varepsilon \lambda_i \eta(x, x) > 0$$
for $x \in M_i$, we have $\operatorname{sgn} \varepsilon = \operatorname{sgn} \lambda_i$ for all $i$. We replace $\eta$ on $M$ by $\eta^*$, where $\eta^*|_{M_i \times M_i}$ equals $\sqrt{|\lambda_i|}(\eta|_{M_i \times M_i})$, and we replace $u$ by $u^*$, where $u^*|_{M_i}$ equals $(1/\sqrt{|\lambda_i|})(u|_{M_i})$. Therefore, we have $(u^*)^2 = \varepsilon$ on $M$.

For $\varepsilon = +1$, let $M_+$ be the eigenspace of $+1$ and $M_-$ of $-1$ for $u^*$. Since $u^*(ix) = -iu^*(x)$, we have $iM_\pm = M_\mp$. Then the scalar multiplication function $\mathbb{C} \otimes_{\mathbb{R}} M_+ \to M$ defines a $G$-isomorphism.

For $\varepsilon = -1$, let $j(x) = u^*(x)$. Then $M$ admits $\mathbb{H}$ as a field of scalars extending the action of $\mathbb{C}$ so that $M$ is a $G$-module over $\mathbb{H}$. This proves the theorem.
