---
role: proof
locale: en
of_concept: harvey-lawson-boundary-theorem
source_book: gtm035
source_chapter: "Chapter 19"
source_section: "19.1"
---

# Proof of Harvey-Lawson Theorem on Boundaries of Analytic Varieties

*The following is a proof sketch of Theorem 19.1, as presented in the book. The full technical details (concerning exceptional points and the boundary of $\Sigma$ in the sense of Stokes' Theorem) are referred to the original paper [HarL2].*

## Construction of the candidate analytic variety

The orientation of an analytic variety in $\mathbb{C}^2$ is always taken to be the "natural" one induced by the complex structure. It is clear that if a simple closed oriented curve $\gamma$ satisfies the moment condition, then, if we reverse the orientation of $\gamma$, the moment condition is still satisfied. This explains the need for the "$\pm$" in the statement of the theorem.

We define $U_0$ to be the unbounded component of $\mathbb{C} \setminus \pi(\gamma)$ and denote by $U_1, U_2, \ldots$ the bounded components of $\mathbb{C} \setminus \pi(\gamma)$. We put

$$U = \bigcup_{j \geq 0} U_j,$$

that is, $U = \mathbb{C} \setminus \pi(\gamma)$. For each $U_j$, $j = 0, 1, \ldots$, set $n_j$ equal to the winding number of $\pi(\gamma)$ about points of $U_j$. We have seen above that $n_j$ also equals the number of sheets of $\Sigma$ over $U_j$, a nonnegative integer. Thus we have $n_j \geq 0$, for $j = 0, 1, \ldots$.

Now we shall assume the moment condition and our objective is to produce an analytic variety $\Sigma$ such that $\gamma = b\Sigma$, in the sense of Stokes' Theorem, after a possible change of orientation of $\gamma$.

Fix $R > 0$ as above. We define

$$\Phi(z, w) = \frac{1}{2\pi i} \int_{\gamma} \frac{\log(w - \eta)}{\zeta - z} d\zeta$$

for $z \in U$ and $|w| > R$, and also

$$F(z, w) = e^{\Phi(z, w)},$$

for $z \in U$ and $|w| > R$. For each $i$, $i = 0, 1, \ldots$, we define $F_i$ as the restriction of $F$ to $U_i$.

## Rationality of each $F_s$ in $w$

**Plemelj's Theorem.** $G^+$ and $G^-$ have continuous extensions to $\alpha$, again denoted $G^+$ and $G^-$. On $\alpha$ we have

$$G^+(z) - G^-(z) = g(z), \quad z \in \alpha.$$

**Lemma 19.2** (Jump Formula Across Smooth Boundary Arc). Let $i, j$ be indices such that the regions $U_i, U_j$ have a common smooth (open) boundary arc $\alpha$, with $\alpha$ positively oriented for $U_j$. Then:

(i) $F_i$ has a continuous extension to $(U_i \cup \alpha) \times \{|w| > R\}$ and $F_j$ has a continuous extension to $(U_j \cup \alpha) \times \{|w| > R\}$;

(ii) $F_j(a, w) = (w - f(a))F_i(a, w)$, $a \in \alpha$, $|w| > R$, where $(a, f(a))$ is the unique point on $\gamma$ over $a$.

**Lemma 19.3** (Analytic Extension from Boundary). Let $G$ be a function continuous on $(\Omega \cup \alpha) \times \{|w| > R\}$ and analytic on $\Omega \times \{|w| > R\}$, and let $N$ be a nonnegative integer such that

$$G(z, w) = \sum_{k=-\infty}^{N} g_k(z)w^k \quad z \in \Omega \cup \alpha, \; |w| > R,$$

where each $g_k$ lies in $\mathfrak{A}$. Assume that for each $a \in \alpha$, the function $w \mapsto G(a, w)$ is rational of order at most $M$, for some positive integer $M$. Then there exist functions

$$P(z, w) = \sum_{j=0}^{k} p_j(z)w^j, \quad Q(z, w) = \sum_{j=0}^{l} q_j(z)w^j$$

with each $p_j \in \mathfrak{A}$, $q_j \in \mathfrak{A}$, such that $G = P/Q$ on $\Omega \times \{|w| > R\}$.

## Propagation of rationality

Let $\alpha$ be a common boundary arc of two regions $U_j$ and $U_k$ which is positively oriented with respect to $U_j$, that is, $n_j = n_k + 1$. We want to show that if the conclusion of Lemma 19.3 holds for one of $F_j, F_k$, then it holds for the other. By Lemma 19.2 we know that both $F_k$ and $F_j$ have continuous extensions to $\alpha$. Suppose that we know that $F_j$ is rational in $w$ on $U_j$. It follows by continuity that $F_j$ is rational in $w$ on $\alpha$. By Lemma 19.2, $F_j(a, w) = (w - f(a))F_k(a, w)$, for all $a \in \alpha$, $|w| > R$. Therefore, $F_k(a, w) = F_j(a, w)/(w - f(a))$ is rational in $w$. Now Lemma 19.3 yields that $F_k$ is rational in $w$ on $U_k$. In the same way, one shows that if $F_k$ is rational in $w$ on $U_k$, then $F_j$ is rational in $w$ on $U_j$.

For any $s$ we choose a sequence of indices

$$i_0 = 0, i_1, \ldots, i_{m-1}, i_m = s$$

such that $U_{i_{j-1}}$ and $U_{i_j}$ share a common boundary arc for $j = 1, 2, \ldots, m$. Now starting from $U_0$ and applying the previous paragraph, it follows by induction on the length $m$ of the sequence that $F_s$ is rational in $w$ on $U_s$.

## Irreducibility of $\Sigma$

Until now we have not used the hypothesis that $\gamma$ is a single curve and we know only that $\Sigma$ is a finite union of branches each with positive or negative orientation. Suppose, by way of contradiction, that $\Sigma$ had more than one branch (irreducible component). Consider an arc $\alpha$ on the boundary of the unbounded component $U_0$. Then, since the winding number changes by $\pm 1$ as we cross $\alpha$, there is only one of the irreducible components of $\Sigma$ that contains limit points on the part of $\gamma$ over $\alpha$. This means that one of the branches $V$ of $\Sigma$ has as its boundary a proper compact subset $\tau$ of $\gamma$. In particular, $\tau$ is contained in a Jordan arc. The maximum principle shows that $V$ is contained in the polynomial hull of $\tau$. But the proof of Theorem 12.4 (basically, the argument principle) implies that $\tau$ is polynomially convex. This is the desired contradiction!

Thus $\Sigma$ is irreducible, i.e., it consists of a single branch whose boundary is contained in $\gamma$. From this one can deduce that, by reversing the orientation of $\Sigma$ if necessary in order that the orientation of $\Sigma$ be positive, $b\Sigma = \pm \gamma$.

**Remark.** As noted in the proof, the argument used in Theorem 19.1 applies when $\gamma$ is only assumed to be a finite union of disjoint simple closed oriented curves, of course satisfying the moment condition. The conclusion is then that there exists a holomorphic chain $V$ such that $bV = \gamma$.

For a complete proof, one still needs to show that the boundary of $\Sigma$ in the sense of Stokes' Theorem is precisely equal to $\gamma$. In particular, one must discuss the exceptional points. For these rather technical issues, we refer to the original paper [HarL2].
