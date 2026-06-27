---
role: proof
locale: en
of_concept: constant-rank-kernel-image-cokernel-are-bundles
source_book: gtm020
source_chapter: "3"
source_section: "8"
---

Since the statement is local in the base, we may restrict $u$, $\xi^n$, and $\eta^m$ to a coordinate neighborhood. Consequently, there is a $B$-morphism $u: B \times F^n \to B \times F^m$ of the form $u(b, x) = (b, u_b(x))$, where $b \mapsto u_b$ is a map $B \to \mathbf{L}(F^n, F^m)$. For each $b \in B$, the rank of $u_b$ is $k$.

Fix a point $a \in B$. Decompose the domain and codomain as
$$
F^n = V_1 \oplus V_2, \qquad F^m = W_1 \oplus W_2,
$$
where $V_2 = \ker u_a$, $W_1 = \operatorname{im} u_a$, $\dim V_1 = \dim W_1 = k$, $\dim V_2 = n-k$, and $\dim W_2 = m-k$.

For each $b \in B$, define a linear map
$$
w_b: V = F^n \oplus W_2 = V_1 \oplus V_2 \oplus W_2 \longrightarrow W_1 \oplus W_2 \oplus V_2 = F^m \oplus V_2 = W
$$
by the following block requirements:
\begin{itemize}
\item $w_b|_{V_1} = (u_b|_{V_1}) \oplus 0$,
\item $w_b|_{V_2} = (u_b|_{V_2}) \oplus 1_{V_2}$,
\item $w_b|_{W_2} = 0 \oplus 1_{W_2} \oplus 0$.
\end{itemize}

At $a$, the restriction $u_a|_{V_1}: V_1 \to W_1$ is an isomorphism (since it is injective and both spaces have dimension $k$). Consequently, $w_a$ is an isomorphism of $V$ onto $W$. The isomorphisms form an open subset of $\mathbf{L}(V, W)$, and since $b \mapsto w_b$ is continuous, there exists a neighborhood $N$ of $a$ such that $w_b$ is an isomorphism for all $b \in N$.

For $b \in N$, the isomorphism $w_b$ identifies $\ker u_b$ with $V_2$ and $\operatorname{im} u_b$ with $W_1$. More precisely, since $w_b$ maps $V_2$ isomorphically onto the second summand and the kernel of $(u_b|_{V_2}) \oplus 1_{V_2}$ is zero on $V_2$, we have $\ker u_b \cong V_2$; similarly $w_b$ sends $V_1$ onto $W_1$, giving $\operatorname{im} u_b \cong W_1$.

Thus, over $N$, the subspaces $\ker u$ and $\operatorname{im} u$ are trivial bundles with fibres $V_2$ (dimension $n-k$) and $W_1$ (dimension $k$) respectively. This provides local trivializations for $\ker u$ and $\operatorname{im} u$, proving they are vector bundles.

For $\operatorname{coker} u$, note that $w_b$ identifies the quotient $F^m / \operatorname{im} u_b$ with $W_2$ (the complement of $W_1$ in $F^m$), so $\operatorname{coker} u$ is locally trivial with fibre $W_2$ of dimension $m-k$. Hence $\operatorname{coker} u$ is also a vector bundle over $B$.
