---
role: proof
locale: en
of_concept: projective-space-is-proper
source_book: gtm052
source_chapter: "II"
source_section: "4"
---

Let $X = \mathbf{P}_{\mathbb{Z}}^n$. The open affines $V_i = D_+(x_i)$ cover $X$, and each $V_i \cong \operatorname{Spec} \mathbb{Z}[x_0/x_i, \ldots, x_n/x_i]$, so $X$ is of finite type over $\operatorname{Spec} \mathbb{Z}$. To show $X$ is proper, we apply the valuative criterion (Theorem 4.7). Let $R$ be a valuation ring with quotient field $K$, and suppose given morphisms $U = \operatorname{Spec} K \to X$ and $T = \operatorname{Spec} R \to \operatorname{Spec} \mathbb{Z}$.

Let $\xi_1 \in X$ be the image of the unique point of $U$. By induction on $n$, we may assume $\xi_1 \notin X \setminus V_i$ for any $i$, i.e., $\xi_1 \in \bigcap V_i$. Thus all functions $x_i/x_j$ are invertible in $\mathcal{O}_{\xi_1}$.

The morphism $U \to X$ induces an inclusion $k(\xi_1) \subseteq K$. Let $f_{ij} \in K$ be the image of $x_i/x_j$. Then $f_{ij} \neq 0$ in $K$, and $f_{ik} = f_{ij} f_{jk}$. Let $v: K^* \to G$ be the valuation of $R$ and set $g_i = v(f_{i0})$ for $i = 0, \ldots, n$. Choose $k$ such that $g_k$ is minimal in $\{g_0, \ldots, g_n\}$. Then $v(f_{ik}) = g_i - g_k \geq 0$, so $f_{ik} \in R$ for all $i$.

Define a homomorphism $\varphi: \mathbb{Z}[x_0/x_k, \ldots, x_n/x_k] \to R$ sending $x_i/x_k \mapsto f_{ik}$. This gives a morphism $T \to V_k \subseteq X$ whose restriction to $U$ is the original map. Thus a lift exists, and by the separatedness criterion, it is unique. Therefore $\mathbf{P}_{\mathbb{Z}}^n$ is proper.

For any projective morphism $f: X \to Y$, $X$ is a closed subscheme of $\mathbf{P}_Y^n = \mathbf{P}_{\mathbb{Z}}^n \times_{\operatorname{Spec} \mathbb{Z}} Y$. Since $\mathbf{P}_{\mathbb{Z}}^n \to \operatorname{Spec} \mathbb{Z}$ is proper, its base change $\mathbf{P}_Y^n \to Y$ is proper by Corollary 4.8. A closed immersion is proper, and the composition $X \hookrightarrow \mathbf{P}_Y^n \to Y$ is therefore proper.
