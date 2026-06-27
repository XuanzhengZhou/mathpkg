---
locale: en
of_concept: the-properties-textsw-0-to-textsw-3-completely-determine-the
role: proof
source_book: gtm020
source_chapter: 17. Chern Classes and Stiefel-Whitney Classes
source_section: '1'
---

Let $w_i$ and $\bar{w}_i$ be two sets of Stiefel-Whitney classes, and let $\xi^n$ be a vector bundle with splitting map $f: B_1 \rightarrow B$. Since $w_1$ is uniquely determined for line

$$0 \rightarrow \lambda_{\xi} \rightarrow q^*(\xi) = q^*(\lambda_1) \oplus \cdots \oplus q^*(\lambda_n) \rightarrow \sigma \rightarrow 0$$

and

$$0 \rightarrow \theta^1 = \lambda_{\xi}^* \otimes \lambda_{\xi} \rightarrow [\lambda_{\xi}^* \otimes q^*(\lambda_i)] \oplus \cdots \oplus [\lambda_{\xi}^* \otimes q^*(\lambda_n)] \rightarrow \lambda_{\xi}^* \otimes \sigma \rightarrow 0$$

Therefore, $\lambda_{\xi}^* \otimes q^*(\xi)$ has a cross section $s$ which is everywhere nonzero and projects to a cross section $s_i$ in $\lambda_{\xi}^* \otimes q^*(\lambda_i)$. Let $V_i$ be the open subset over which $s_i \neq 0$. The image of $x_1(\lambda_{\xi}^* \otimes q^*(\lambda_i))$ is zero in $H^c(V_i, K_c)$, and therefore it can be pulled back to $H^c(E(P\xi), V_i; K_c)$. Moreover, the cup product $x_1(\lambda_{\xi}^* \otimes q^*(\lambda_1)) \cdots x_1(\lambda_{\xi}^* \otimes q^*(\lambda_n))$ is an element of $H^c(E(P\xi), \bigcup_{1 \leq i \leq n} V_i; K_c) = H^*(E(P\xi), E(P\xi); K_c) = 0$. Therefore, we have the relation

$$\prod_{1 \leq i \leq n} [q^*(x_1(\lambda_i)) + x_1(\lambda_{\xi}^*)] = 0$$

For $a_{\xi} = x_1(\lambda_{\xi}^*)$, this is just the equation $a_{\xi}^n + q^*x_1(\xi)a_{\xi}^{n-1} + \cdots + q^*x_n(\xi) = 0$. Therefore, we have $x(\xi) = x

7.2 Example. Every restriction of a complex vector bundle to a real vector bundle is orientable and has a natural orientation because $U(n) \subset SO(2n) \subset O(2n)$.

The next theorem contains the fundamental construction of this section.
