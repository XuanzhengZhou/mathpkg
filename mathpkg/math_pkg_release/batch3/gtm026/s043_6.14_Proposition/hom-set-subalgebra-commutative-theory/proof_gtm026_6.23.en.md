---
role: proof
locale: en
of_concept: hom-set-subalgebra-commutative-theory
source_book: gtm026
source_chapter: "6"
source_section: "6.23"
---

Assume that $(Y, \theta)$ is completely commutative and let $\alpha$ be an $n$-ary $\mathbf{T}$-operation. By 6.17(2) it suffices to show that $f = (f_i) \tau_\alpha$ is in $A$ if each $f_i$ is in $A$ (where $(Y^X, \tau)$ denotes $(Y, \theta)^X$).

Let $\beta$ be an $m$-ary $\mathbf{T}$-operation. Since a $\mathbf{T}$-homomorphism is the same thing as a function which commutes with $\mathbf{T}$-operations (6.8), it suffices to show that
$$(x_j) \xi_\beta f = (x_j f) \theta_\beta$$
for $(x_j) \in X^m$.

First observe that since $\operatorname{pr}_x \colon (Y, \theta)^X \to (Y, \theta)$ is a $\mathbf{T}$-homomorphism, operations on $(Y, \theta)^X$ are "pointwise," i.e., for $(g_i) \in (Y^X)^n$ and $x \in X$,
$$x(g_i) \tau_\alpha = (x g_i) \theta_\alpha.$$

We therefore have
\[
\begin{aligned}
(x_j) \xi_\beta f &= \langle (x_j) \xi_\beta, (f_i) \tau_\alpha \rangle \\
&= \langle (x_j) \xi_\beta f_i, \theta_\alpha \rangle \\
&= ((x_j f_i : j \in m) \theta_\beta : i \in n) \theta_\alpha \quad \text{(as each } f_i \in A) \\
&= ((x_j f_i : i \in n) \theta_\alpha : j \in m) \theta_\beta \quad \text{(as } (Y, \theta) \text{ is completely commutative)} \\
&= (x_j f) \theta_\beta.
\end{aligned}
\]

Thus $f$ commutes with all $\mathbf{T}$-operations and hence is a $\mathbf{T}$-homomorphism, so $f \in A$. By 6.17(2), $A$ is a subalgebra.
