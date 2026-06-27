---
role: proof
locale: en
of_concept: identity-theorem-for-analytic-manifolds
source_book: gtm011
source_chapter: "6"
source_section: "6.1"
---

Define the subset $A$ of $X$ by

$$A = \{x : f \text{ and } g \text{ agree on a neighborhood of } x\}.$$

This set $A$ will be shown to be non-empty and the reader will be required to prove that $A$ is both open and closed in $X$. By hypothesis there is a point $a$ in $X$ such that for every neighborhood $U$ of $a$ there is a point $x$ in $U$ with $x \neq a$ and $f(x) = g(x)$. It is easy to conclude that $f(a) = g(a) = \alpha$. If $(\Lambda, \psi) \in \Psi$ and $\alpha \in \Lambda$ then there is a patch $(U, \varphi)$ in $\Phi$ such that $f(U)$ and $g(U)$ are contained in $\Lambda$ with both $\psi \circ f \circ \varphi^{-1}$ and $\psi \circ g \circ \varphi^{-1}$ analytic in a disk $D$ about $z_0 = \varphi(\alpha)$. But the hypothesis gives that $z_0$ is a limit point of

$$\{z \in D : \psi \circ f \circ \varphi^{-1}(z) = \psi \circ g \circ \varphi^{-1}(z)\} = F.$$

In fact, if $f(x) = g(x)$ then $\varphi(x) \in F$. Thus $\psi \circ f \circ \varphi^{-1}(z) = \psi \circ g \circ \varphi^{-1}(z)$ for all $z$ in $D$; or $f(x) = g(x)$ for all $x$ in $U \cap \varphi^{-1}(D)$. Hence $a \in A$ and $A \neq \square$.
