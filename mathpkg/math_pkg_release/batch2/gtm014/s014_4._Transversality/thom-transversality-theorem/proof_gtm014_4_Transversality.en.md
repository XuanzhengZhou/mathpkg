---
role: proof
locale: en
of_concept: thom-transversality-theorem
source_book: gtm014
source_chapter: "1"
source_section: "4. Transversality"
---

**Proof of Theorem 4.9 (Thom Transversality Theorem).** 

Choose open sets $W_r$ in $W$ satisfying:
(a) Each $\overline{W}_r$ is compact;
(b) The sets $\overline{W}_r$ cover $W$;
(c) For each $r$, there exist coordinate patches $U_r$ in $X$ and $V_r$ in $Y$ such that $\overline{W}_r \subset \pi^{-1}(U_r \times V_r)$, where $\pi: J^k(X, Y) \to X \times Y$ is the natural projection.

Let
$$T_{W_r} = \{f \in C^\infty(X, Y) \mid j^k f \pitchfork \overline{W}_r\}.$$

Since $T_W = \bigcap_{r=1}^\infty T_{W_r}$, it suffices to show that each $T_{W_r}$ is open and dense.

We first show $T_{W_r}$ is dense. Choose charts $\psi: U_r \to \mathbf{R}^n$ and $\eta: V_r \to \mathbf{R}^m$ and smooth cutoff functions $\rho: \mathbf{R}^n \to [0, 1]$ and $\rho': \mathbf{R}^m \to [0, 1]$ such that
$$\rho = \begin{cases} 1 & \text{on a neighborhood of } \psi \circ \alpha(\overline{W}_r) \\ 0 & \text{off } \psi(U_r) \end{cases}$$
and
$$\rho' = \begin{cases} 1 & \text{on a neighborhood of } \eta \circ \beta(\overline{W}_r) \\ 0 & \text{off } \eta(V_r) \end{cases}$$
where $n = \dim X$, $m = \dim Y$, $\alpha$ is the source map, and $\beta$ is the target map. The choice of $\rho$ and $\rho'$ is possible since $\overline{W}_r$ is compact.

We perturb $f$ locally using polynomial data. Let $B'$ be the space of polynomial mappings of $\mathbf{R}^n \to \mathbf{R}^m$ of degree $\leq k$. For $b \in B'$, define $g_b: X \to Y$ by
$$g_b(x) = \begin{cases} f(x) & \text{if } x \notin U_r \text{ or } f(x) \notin V_r \\ \eta^{-1}\bigl(\rho(\psi(x))\,\rho'(\eta f(x))\,b(\psi(x)) + \eta f(x)\bigr) & \text{otherwise.} \end{cases}$$

The choice of $\rho$ and $\rho'$ guarantees that $g_b$ is a smooth function from $X$ to $Y$, equal to $f$ off the domain of perturbation. Moreover,
$$\Phi: X \times B \to J^k(X, Y)$$
defined by $\Phi(x, b) = j^k(g_b)(x)$ is locally a diffeomorphism near $(x, b)$. For let $\sigma$ be in $J^k(X, Y)$ near $\Phi(x, b)$, let $x' = \alpha(\sigma)$, and let $b'$ be the unique polynomial mapping of degree $\leq k$ such that $\sigma = j^k(\eta(b'\cdot \psi + \eta \circ f))(x')$. Then $\sigma \mapsto (b', x')$ is a smooth mapping and is the inverse of $\Phi$.

By Corollary 4.8 (or the parametrized transversality lemma), since $\Phi \pitchfork \overline{W}_r$, the set of $b$ for which $g_b \pitchfork \overline{W}_r$ is dense in $B$. For $b$ sufficiently close to $0$, $g_b$ is in any given neighborhood of $f$, so $T_{W_r}$ is dense.

The openness of $T_{W_r}$ when $\overline{W}_r$ is compact follows from a lemma about the openness of the transversality condition for compact submanifolds (Proposition 4.5 adapted to jet bundles, or Lemma 4.14 for the multijet case). Since $C^\infty(X, Y)$ is a Baire space, $T_W = \bigcap T_{W_r}$ is residual.

Moreover, if $W$ is closed, then each $W_r$ can be chosen so that the condition for openness propagates to the intersection, making $T_W$ open.
