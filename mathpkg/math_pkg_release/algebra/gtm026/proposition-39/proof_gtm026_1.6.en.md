---
role: proof
locale: en
of_concept: proposition-39
source_book: gtm026
source_chapter: "1"
source_section: "6.21"
---

By 1.5.40, Set$^S$ may be thought of as $(\Omega, E)$-alg where $\Omega$ has only unary operation labels. Let $X$ be a set and let $(f_u: XS \longrightarrow XS|u \in \Omega)$ be the free S-algebra on $X$, i.e., $XS$ is the free algebra and $(f_u)$ is its $\Omega$-structure. Since every equation in $E$ has form $u_1 \cdots u_n = v_1 \cdots v_m$ or $u_1 \cdots u_n = id$ and $T$ is a functor, $(f_u T: XST \longrightarrow XST)$ is an S-algebra. Since $f_u T: (XST, XS\mu_T) \longrightarrow (XST, XS\mu_T)$ is a T-homomorphism, $XST$ is an S-T bialgebra. Define $\eta: X \longrightarrow XST$ by $= X\eta_S.XS\eta_T$. Let $(Y, \xi, \theta)$ be an S-T bialgebra with S-structure $(\xi_u: Y \longrightarrow Y)$ and let $g: X \longrightarrow Y$ be a function. As shown below let $g_1$ be the S-homomorphic extension of $g$ and let $g_2$ be the T-homomorphic extension of $g_1$. Then $XS\eta_T.g_2.\xi_u = g_1.\xi_u = f_u.g_1 = f_u.XS\eta_T.g_2 = XS\eta_T.f_u.T.g_2$; as $g_2, f_u T$ and $\xi_u$ are T-homomorphisms, $g_2.\xi_u = f_u.T.g_

algebra $(X, \xi)$ the set $A = \{ f : X \longrightarrow Y | f \text{ is a } \mathbf{T} \text{-homomorphism}(X, \xi) \longrightarrow (Y, \theta) \}$ is a subalgebra of $(Y, \theta)^X$.

Assume that $(Y, \theta)$ is completely commutative and let $\alpha$ be an $n$-ary $\mathbf{T}$-operation. By 6.17(2) it suffices to show that $f = (f_i) \tau_\alpha$ is in $A$ if each $f_i$ is in $A$ (where $(Y^X, \tau)$ denotes $(Y, \theta)^X$). Let $\beta$ be an $m$-ary $\mathbf{T}$-operation. Since a $\mathbf{T}$-homomorphism is the same thing as a function which commutes with $\mathbf{T}$-operations (6.8) it suffices to show that $(x_j) \xi_\beta f = (x_j f) \theta_\beta$ for $(x_j) \in X^m$. To this end, first observe that since $\text{pr}_x : (Y, \theta)^X \longrightarrow (Y, \theta)$ is a $\mathbf{T}$-homomorphism, operations on $(Y, \theta)^X$ are “pointwise,” i.e., for $(g_i) \in (Y^X)^n$ and $x \in X$, $x(g_i) \tau_\alpha = (xg_i) \theta_\alpha$. We therefore have

$$(x_j) \xi_\beta f = \langle (x_j) \xi_\beta, (f_i) \tau_\alpha \rangle = \langle (x_j) \xi_\beta f_i, \theta_\alpha \rangle$$
$$= ((x_j f_i : j \in m) \theta_\beta : i \in n) \theta_\alpha \quad \text{(as each } f_i \in A)$$
$$= ((x_j f_i : i \in n) \theta_\alpha : j \in m) \theta_\beta \quad \text{(as } (Y, \theta) \
