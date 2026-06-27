---
role: proof
locale: en
of_concept: theorem-7-17-f-a-1-a-n-m-m-x-x-a-1-a-n-a-m-m-a-a-1-a-n
source_book: gtm008
source_chapter: "5"
source_section: "5 Partial Order Structures and Topological Spaces

In the work"
---
From Theorem 7.16
$$(\exists \beta \geq \alpha)(\forall a_1, \ldots, a_n \in M_\alpha)[\mathbf{M} \models (\exists x) \varphi(x, a_1, \ldots, a_n) \leftrightarrow (\exists a

By Corollary 7.18 there exists a semi-normal function $F_0$ such that

$$\beta = F_0(\beta) \rightarrow (\forall a_1, \ldots, a_n \in M_\beta)[\mathbf{M} \models (\exists x) \psi(x, a_1, \ldots, a_n) \leftrightarrow (\exists a \in M_\beta)[\mathbf{M} \models \psi(a, a_1, \ldots, a_n)]$$

Therefore if $\beta = F_0(\beta) = \cdots = F_m(\beta)$, and $a_1, \ldots, a_n \in M_\beta$ then

$$\mathbf{M} \models \varphi(a_1, \ldots, a_n) \leftrightarrow (\exists a \in M_\beta)[\mathbf{M} \models \psi(a, a_1, \ldots, a_n)]$$
$$\leftrightarrow (\exists a \in M_\beta)[\mathbf{M}_{\beta} \models \psi(a, a_1, \ldots, a_n)]$$
$$\leftrightarrow \mathbf{M}_{\beta} \models (\exists x) \psi(x, a_1, \ldots, a_n)$$
$$\leftrightarrow \mathbf{M}_{\beta} \models \varphi(a_1, \ldots, a_n).$$
