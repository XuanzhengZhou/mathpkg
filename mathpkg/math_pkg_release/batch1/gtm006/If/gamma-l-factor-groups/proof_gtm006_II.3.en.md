---
role: proof
locale: en
of_concept: gamma-l-factor-groups
source_book: gtm006
source_chapter: "II"
source_section: "3"
---

(a) Define $\phi: \Gamma L(V) \to \operatorname{Aut} K$ as follows. Every $\gamma \in \Gamma L(V)$ is semi-linear, so there exists $\alpha \in \operatorname{Aut} K$ such that $(kv)^\gamma = k^\alpha v^\gamma$ for all $k \in K, v \in V$. Set $\phi(\gamma) = \alpha$. One verifies that $\phi$ is a homomorphism: if $\gamma_1$ has associated automorphism $\alpha_1$ and $\gamma_2$ has $\alpha_2$, then their composition has automorphism $\alpha_1 \circ \alpha_2$. The kernel of $\phi$ consists of transformations with $\alpha = 1$, i.e., linear transformations, so $\ker \phi = GL(V)$. Every automorphism of $K$ occurs in some semi-linear transformation (e.g., fix a basis and apply the automorphism to coordinates), so $\phi$ is surjective. Thus $\Gamma L(V)/GL(V) \cong \operatorname{Aut} K$.

(b) From Theorem 2.10, $P\Gamma L(V)/PGL(V) \cong (\Gamma L(V)/N) / ((N \cdot GL(V))/N) \cong \Gamma L(V)/(N \cdot GL(V))$. Writing $A = \operatorname{Aut} K$, we have $\Gamma L(V) = A \cdot GL(V)$ and therefore $\Gamma L(V) = A \cdot N \cdot GL(V)$ since $N \subset \Gamma L(V)$. Hence $\Gamma L(V)/(N \cdot GL(V)) \cong (A \cdot N \cdot GL(V))/(N \cdot GL(V))$. An element $\alpha \in A$ lies in $N \cdot GL(V)$ if and only if it can be expressed as an inner automorphism of $K$ (compose with a scalar transformation), giving $A \cap (N \cdot GL(V)) = \operatorname{In} K$. Therefore $P\Gamma L(V)/PGL(V) \cong \operatorname{Aut} K / \operatorname{In} K$.

(c) For a field $K$, consider the determinant map $\det: PGL(V) \to K^*/(K^*)^2$ defined by $\det(g) = \det(\tilde{g}) \bmod (K^*)^2$, where $\tilde{g} \in GL(V)$ is any representative of $g$. This is well-defined since scaling changes the determinant by a square factor. The kernel is precisely $PSL(V)$, giving $PGL(V)/PSL(V) \cong K^*/(K^*)^2$. $\square$
