---
role: proof
locale: en
of_concept: cotangent-space-germ-isomorphism
source_book: gtm014
source_chapter: "III"
source_section: "3. The Generalized Malgrange Preparation Theorem"
---

The map $\psi: M_p(X) \to T_p^*X$ is defined by $\psi([f]_p) = (df)(p)$, the differential of $f$ at $p$. First, $\psi$ is well-defined because if $[f]_p = [g]_p$, then $f = g$ on a neighborhood of $p$, so their differentials agree at $p$. The map $\psi$ is clearly $\mathbf{R}$-linear and surjective: given any cotangent vector, we can represent it as $(df)(p)$ for some smooth function $f$ vanishing at $p$ (for instance, a coordinate function composed with a bump function).

We claim $\operatorname{Ker} \psi = M_p^2(X)$. The ideal $M_p^2(X)$ consists of finite sums of products $[f]_p [g]_p$ where $f(p) = g(p) = 0$. If $[h]_p \in M_p^2(X)$, then $h = \sum f_i g_i$ with $f_i(p) = g_i(p) = 0$, so by the Leibniz rule, $(dh)(p) = \sum (f_i(p) \, dg_i(p) + g_i(p) \, df_i(p)) = 0$, hence $M_p^2(X) \subseteq \operatorname{Ker} \psi$.

Conversely, let $[f]_p \in \operatorname{Ker} \psi$, so $f(p) = 0$ and $(df)(p) = 0$. Choose local coordinates $x_1, \ldots, x_n$ centered at $p$. By II, Lemma 6.10, we can write

$$f(x) = \sum_{i=1}^{n} x_i f_i(x)$$

where $f_i(0) = \frac{\partial f}{\partial x_i}(0)$. Since $(df)(p) = 0$, each $\frac{\partial f}{\partial x_i}(0) = 0$, so $f_i(0) = 0$. Thus each $f_i \in M_p(X)$, and $[f]_p = \sum [x_i]_p [f_i]_p$ is a sum of products of elements of $M_p(X)$, i.e., $[f]_p \in M_p^2(X)$. This proves $\operatorname{Ker} \psi = M_p^2(X)$.

By the First Isomorphism Theorem, $\psi$ induces an isomorphism $M_p(X) / M_p^2(X) \xrightarrow{\cong} T_p^*X$.
