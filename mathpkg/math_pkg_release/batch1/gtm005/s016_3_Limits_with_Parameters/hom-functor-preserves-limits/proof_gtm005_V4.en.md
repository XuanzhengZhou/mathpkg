---
role: proof
locale: en
of_concept: hom-functor-preserves-limits
source_book: gtm005
source_chapter: "V"
source_section: "4. Preservation of Limits"
---

Let $J$ be any category and $F : J \rightarrow C$ a functor with limiting cone $\nu : b \rightarrow F$ in $C$. For any object $c \in C$, we must show that $C(c, \nu) : C(c, b) \rightarrow C(c, F-)$ is a limiting cone in $\mathbf{Set}$.

Take any set $X$ and any cone $\tau : X \rightarrow C(c, F-)$ in $\mathbf{Set}$. For each element $x \in X$ and each $i \in J$, $\tau_i(x) : c \rightarrow F_i$ is an arrow in $C$. The naturality of $\tau$ means that for each $u : i \rightarrow j$ in $J$, $F_u \circ \tau_i(x) = \tau_j(x)$. Hence for each fixed $x \in X$, the arrows $\tau_i(x) : c \rightarrow F_i$ form a cone $\tau(x) : c \rightarrow F$ in $C$.

Since $\nu : b \rightarrow F$ is a limiting cone, there exists a unique arrow $h_x : c \rightarrow b$ in $C$ such that $\nu_i \circ h_x = \tau_i(x)$ for all $i$. Define $k : X \rightarrow C(c, b)$ by $k(x) = h_x$. Then $C(c, \nu_i) \circ k = \tau_i$ for all $i$. The uniqueness of $h_x$ ensures uniqueness of $k$. Hence $C(c, \nu)$ is a limiting cone.

Equivalently, using the adjunction $\operatorname{Cone}(X, S) \cong \mathbf{Set}(X, \operatorname{Lim} S)$ in $\mathbf{Set}$ for $S : J \rightarrow \mathbf{Set}$, we have:
\begin{align*}
\operatorname{Cone}(X, C(c, F-)) &\cong \mathbf{Set}(X, \operatorname{Cone}(*, C(c, F-))) \\
&= \mathbf{Set}(X, \operatorname{Cone}(c, F)) \\
&\cong \mathbf{Set}(X, C(c, \operatorname{Lim} F))
\end{align*}
where the last isomorphism uses the definition of $\operatorname{Lim} F$. The Yoneda lemma then yields $\operatorname{Lim} C(c, F-) \cong C(c, \operatorname{Lim} F)$.
