---
role: proof
locale: en
of_concept: double-dual-natural-transformation
source_book: gtm005
source_chapter: "I. Categories, Functors, and Natural Transformations"
source_section: "4. Natural Transformations"
---

For each $g \in G$, define $\tau_G g: DG \rightarrow \mathbf{R}/\mathbf{Z}$ by $(\tau_G g)(t) = t(g)$ for all $t \in DG$. This is a homomorphism because $(\tau_G g)(t_1 + t_2) = (t_1 + t_2)(g) = t_1(g) + t_2(g) = (\tau_G g)(t_1) + (\tau_G g)(t_2)$. Thus $\tau_G g \in D(DG)$. The map $\tau_G: G \rightarrow D(DG)$ is a homomorphism because $(\tau_G(g_1 + g_2))(t) = t(g_1 + g_2) = t(g_1) + t(g_2) = (\tau_G g_1)(t) + (\tau_G g_2)(t)$.

To verify naturality, let $f: G \rightarrow H$ be any homomorphism of abelian groups. We must check the commutativity of the square

$$
\begin{array}{ccc}
G & \xrightarrow{\tau_G} & D(DG) \\
{\scriptstyle f}\downarrow & & \downarrow {\scriptstyle D(Df)} \\
H & \xrightarrow{\tau_H} & D(DH)
\end{array}
$$

Recall that $Df: DH \rightarrow DG$ sends a character $u: H \rightarrow \mathbf{R}/\mathbf{Z}$ to $u \circ f: G \rightarrow \mathbf{R}/\mathbf{Z}$. Then $D(Df): D(DG) \rightarrow D(DH)$ sends $\varphi \in D(DG)$ to $\varphi \circ Df$. For any $g \in G$, we compute:
$$
D(Df)(\tau_G g) = \tau_G g \circ Df \in D(DH).
$$
For any character $u \in DH$, we have $(\tau_G g \circ Df)(u) = (\tau_G g)(u \circ f) = (u \circ f)(g) = u(f(g))$. On the other hand, $(\tau_H(f(g)))(u) = u(f(g))$. Therefore $D(Df) \circ \tau_G = \tau_H \circ f$, establishing the naturality of $\tau$.
