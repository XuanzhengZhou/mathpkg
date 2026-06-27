---
role: proof
locale: en
of_concept: dual-tensor-action-of-algebraic-group
source_book: gtm021
source_chapter: "10"
source_section: "Automorphisms and Derivations"
---
For the dual representation: the group action $\varphi^*: G \to \operatorname{GL}(V^*)$ is given by $\varphi^*(x)(f) = f \circ \varphi(x^{-1})$. Differentiating at $e$, for $X \in \mathfrak{g}$,
$$d\varphi^*(X)(f) = f \circ (-d\varphi(X)) = -f \circ (X \cdot (-)),$$
so $(X \cdot f)(v) = -f(X \cdot v)$.

For the tensor product: choose bases $\{v_r\}$ of $V$ and $\{w_s\}$ of $W$. Let $\varphi(x)$ have matrix $(a_{ir}(x))$ and $\psi(x)$ have matrix $(b_{js}(x))$. The representation $\tau: G \to \operatorname{GL}(V \otimes W)$ has matrix entries $a_{ir} b_{js}$ in the $(i,j; r,s)$ position (with basis $v_r \otimes w_s$).

Differentiating: if $d\varphi(X) = (c_{ir})$ and $d\psi(X) = (d_{js})$, where $c_{ir} = X(a_{ir})$ and $d_{js} = X(b_{js})$, then the differential $d\tau(X)$ in the $(i,j; r,s)$ entry is
$$X(a_{ir} b_{js}) = X(a_{ir}) b_{js}(e) + a_{ir}(e) X(b_{js}) = \delta_{js} c_{ir} + \delta_{ir} d_{js},$$
using $a_{ir}(e) = \delta_{ir}$ and $b_{js}(e) = \delta_{js}$. This is precisely the rule $X \cdot (v_r \otimes w_s) = (X \cdot v_r) \otimes w_s + v_r \otimes (X \cdot w_s)$, extended linearly.
