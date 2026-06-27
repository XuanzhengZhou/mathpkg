---
role: proof
locale: en
of_concept: tensor-product-unary-theories
source_book: gtm026
source_chapter: "6"
source_section: "6.21"
---

By 1.5.40, $\mathbf{Set}^S$ may be thought of as $(\Omega, E)$-alg where $\Omega$ has only unary operation labels. Let $X$ be a set and let $(f_u \colon XS \to XS \mid u \in \Omega)$ be the free $S$-algebra on $X$, i.e., $XS$ is the free algebra and $(f_u)$ is its $\Omega$-structure.

Since every equation in $E$ has the form $u_1 \cdots u_n = v_1 \cdots v_m$ or $u_1 \cdots u_n = \operatorname{id}$ and $T$ is a functor, $(f_u T \colon XST \to XST)$ is an $S$-algebra. Since $f_u T \colon (XST, XS\mu_T) \to (XST, XS\mu_T)$ is a $T$-homomorphism, $XST$ is an $S$-$T$ bialgebra.

Define $\eta \colon X \to XST$ by $\eta = X\eta_S \cdot XS\eta_T$. Let $(Y, \xi, \theta)$ be an $S$-$T$ bialgebra with $S$-structure $(\xi_u \colon Y \to Y)$ and let $g \colon X \to Y$ be a function. Let $g_1$ be the $S$-homomorphic extension of $g$ and let $g_2$ be the $T$-homomorphic extension of $g_1$.

Then
\[
XS\eta_T \cdot g_2 \cdot \xi_u = g_1 \cdot \xi_u = f_u \cdot g_1 = f_u \cdot XS\eta_T \cdot g_2 = XS\eta_T \cdot f_u T \cdot g_2
\]
and as $g_2$, $f_u T$, and $\xi_u$ are $T$-homomorphisms, $g_2 \cdot \xi_u = f_u T \cdot g_2$. This establishes the universal property, so $S \otimes T$ exists.
