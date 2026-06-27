---
locale: en
of_concept: let-u-xin-to-etam-be-a-b-morphism-of-vector-bundles-of-const
role: proof
source_book: gtm020
source_chapter: 3. Vector Bundles
source_section: '7'
---

Since the statement refers to a local question, $u, \xi^n$, and $\eta^m$ can be restricted to a coordinate neighborhood. Consequently, there is a $B$-morphism $u: B \times F^n \to B \times F^m$, and it has the form $u(b, x) = (b, u_b(x))$, where $b \mapsto u_b$ is a map $B \to \mathbf{L}(F^n, F^m)$. For each $b \in B$, the rank of $u_b$ is $k$.

At $a \in B$, $u_a: F^n = V_1 \oplus V_2 \to F^m = W_1 \oplus W_2$, where $V_2 = \ker u_a$, $W_1 = \imaginary u_a$, $\dim V_1 = \dim W_1 = k$, $\dim V_2 = n - k$, and $\dim W_2 = m - k$. For each $b \in B$, we define

$$V = F^n \oplus W_2 = V_1 \oplus V_2 \oplus W_2 \xrightarrow{w_b} W_1 \oplus W_2 \oplus V_2 = F^m \oplus V_2 = W$$

by the requirement that $w_b|V_1$ be $(u_b|V_1) \oplus 0$, $w_b|V_2$ be $(u_b|V_2) \oplus 1_{V_2}$, and $w_b|W_2$ be $0 \oplus 1_{W_2} \oplus 0$. Since $u_a|V_1: V_1 \to W_1$ is an isomorphism, the linear transformation $w_a$ is an isomorphism. Since the isomorphisms form an open subset of $\mathbf{L}(V, W)$ and since $
