---
role: proof
locale: en
of_concept: corollary-7-5
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Define $F: [0, 1] \times [0, 1] \rightarrow \Omega$ by $F(s, t) = \gamma(s)$; so $F$ is continuous and $F(0, 0) = \omega_0$. According to Theorem 7.4 there is a unique function $\tilde{F}: [0, 1] \times [0, 1] \rightarrow X$ such that $\tilde{F}(0, 0) = x_0$ and $\rho \circ \tilde{F} = F$. Let $\tilde{\gamma}(s) = \tilde{F}(s, 0)$; then $\tilde{\gamma}$ has initial point $x_0$ and is a lifting of $\gamma$. To prove the uniqueness of $\tilde{\gamma}$, suppose $\tilde{\sigma}$ is also a path in $X$ with initial point $x_0$ and which lifts $\gamma$. Define $\tilde{K}: [0, 1] \times [0, 1] \rightarrow X$ by $\tilde{K}(s, t) = \tilde{\sigma}(s)$. Then $\tilde{K}: (0, 0) = x_0$ and $\rho \circ \tilde{K}(s, t) = \rho \circ \tilde{\sigma}(s) = \gamma(s) = F(s, t)$. By the uniqueness part of Theorem 7.4, $\tilde{F} = \tilde{K}$. Thus $\tilde{\gamma}(s) = \tilde{F}(s, 0) = \tilde{K}(s, 0) = \tilde{\sigma}(s)$.

Proof of Theorem 7.4. Let $\{0 = s_0 < s_1 < \ldots < s_n = 1\}$ and $\{0 = t_0 < t_1 < \ldots < t_n = 1\}$ be partitions of $[0, 1]$ such that for $0 \leq i, j \leq n - 1$,

$$F([s_i, s_{i+1}] \times [t_j, t_{j+1}])$$

is contained in a fundamental open set $\Delta_{ij}$ in $\Omega$. (Verify that this

Let $x_0 \in \rho^{-1}(\omega_0)$ such that $\tilde{\gamma}(0) = \tilde{\sigma}(0) = x_0$. By hypothesis there is a continuous function $F: [0, 1] \times [0, 1] \to \Omega$ such that $F(0, t) = \omega_0, F(1, t) = \omega_1, F(s, 0) = \gamma(s)$, and $F(s, 1) = \sigma(s)$ for all $s$ and $t$ in $[0, 1]$. According to Theorem 7.4 there is a unique continuous function $\tilde{F}: [0, 1] \times [0, 1] \to X$ such that $\tilde{F}(0, 0) = x_0$ and $\rho \circ \tilde{F} = F$. Now $F(\{0\} \times [0, 1]) = \{\omega_0\}$ and $\rho \circ \tilde{F} = F$ implies that $\tilde{F}(\{0\} \times [0, 1]) \subset \rho^{-1}(\omega_0)$. But each component of $\rho^{-1}(\omega_0)$ consists of a single point (Exercise 4) and $\tilde{F}(\{0\} \times [0, 1])$ is connected. Therefore $\tilde{F}(0, t) = x_0$ for all $t$. Similarly, there is a point $x_1$ such that $\tilde{F}(1, t) = x_1$ for all $t$ and $\rho(x_1) = \omega_1$.

By the uniqueness of $\tilde{\gamma}$ and the fact that $s \rightarrow \tilde{F}(s, 0)$ is a path with initial point $x_0$ which lifts $\gamma$, it must be that $\tilde{\gamma}(s) = \tilde{F}(s, 0)$. Similarly, $\tilde{\sigma}(s) = \tilde{F}(s, 1)$. Therefore $\tilde{\gamma}(1) = \tilde{\sigma}(1) = x_1 = F(1, t)$ for all $t$, and $\

that if $(b, [h]_b)$ and $(b, [k]_b) \in \mathcal{U}$ then $[h]_b = [k]_b$. But since $\mathcal{U}$ is arcwise connected, this is exactly the conclusion of Lemma 7.7.

Let us retain the notation of the preceding theorem. Fix $a$ in $D$ and let $\gamma$ and $\sigma$ be paths in $G$ from $a$ to a point $z = b$. Suppose that $\{(f_t, D_t)\}$ and $\{(g_t, B_t)\}$ are continuations of $(f, D)$ along $\gamma$ and $\sigma$ respectively; so $[f_0]_a = [g_0]_a = [f]_a$. Now $\tilde{\gamma}(t) = (\gamma(t), [f_t]_{\gamma(t)})$ and $\tilde{\sigma}(t) = (\sigma(t), [g_t]_{\sigma(t)})$ are paths in $\mathcal{C}$ (see the proof of Theorem 5.10) with the same initial point $(a, [f]_a)$. Moreover $\rho \circ \tilde{\gamma} = \gamma$ and $\rho \circ \tilde{\sigma} = \sigma$; so $\tilde{\gamma}$ and $\tilde{\sigma}$ are the unique liftings of $\gamma$ and $\sigma$ to $\mathcal{C}$. According to the Abstract Monodromy Theorem, if $\gamma \sim \sigma$ (FEP) in $G$ then $\tilde{\gamma}$ and $\tilde{\sigma}$ have the same final point. That is, $(b, [f_1]_b) = \tilde{\gamma}(1) = \tilde{\sigma}(1) = (b, [g_1]_b)$ so that $[f_1]_b = [g_1]_b$. This is precisely the conclusion of Theorem 3.6.

For another application of the Abstract Monodromy Theorem we wish to prove that closed curves in the punctured plane are homotopic iff they have the same winding number about the origin. To do this let $\Gamma = \{z : |z| = 1\}$; as we observed at the beginning

Notice that the rectifiability of $\gamma$ and $\sigma$ was only used to define the winding number of $\gamma$ and $\sigma$ about the origin. It is possible to extend the definition of winding number to non-rectifiable curves.
