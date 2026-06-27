---
role: proof
locale: en
of_concept: fiber-cardinality-bound-theorem
source_book: gtm035
source_chapter: "11"
source_section: "11.12"
---
# Proof of Fiber Cardinality Bound Theorem

**Theorem 11.12.** Let $(A, X, \mathcal{M})$ be a uniform algebra and $f \in A$. Let $\mathcal{U}$ be a component of $\mathbb{C} \setminus f(X)$ and let $\alpha$ be a boundary arc of $\mathcal{U}$ such that $f^{-1}(\alpha)$ lies at most $n$-sheeted over $\alpha$. Suppose there exists a subset $E$ of $\alpha$ of positive linear measure such that $\# f^{-1}(\lambda) \cap \hat{X} \leq n$ for all $\lambda \in E$. Then $\# f^{-1}(\lambda) \cap \hat{X} \leq n$ for all $\lambda \in \mathcal{U}$.

*Proof.* Recall the $k$-diameter $d_k$ as in Definition 11.2. Suppose that $\# f^{-1}(\zeta) > n$ for some $\zeta \in \mathcal{U}$. We construct a region $\mathcal{U}_0$, with a piecewise smooth boundary, such that $\mathcal{U}_0$ contains $\alpha$ as a part of its boundary and with $\zeta \in \mathcal{U}_0 \subseteq \mathcal{U}$.

**Claim.** Fix $\lambda_0 \in E$. Fix $g \in A$. Put

$$F(\lambda) = \log d_{n+1}(g(f^{-1}(\lambda))), \quad \lambda \in \mathcal{U}_0.$$

Then

$$\limsup_{\lambda \to \lambda_0, \, \lambda \in \mathcal{U}_0} F(\lambda) = -\infty.$$

*Proof of Claim.* Denote by $q_1(\lambda_0), \ldots, q_k(\lambda_0)$ the points of $f^{-1}(\lambda_0) \cap \hat{X}$. By choice of $\lambda_0 \in E$, $k \leq n$. Consider the points $g(q_j(\lambda_0))$, $j = 1, \ldots, k$, in $\mathbb{C}$. Take closed disks $\Delta_j$ with center $g(q_j(\lambda_0))$ and radius $\epsilon > 0$ small, where the disks are disjoint or coincide according to whether the points $g(q_j(\lambda_0))$ are distinct or not.

Let $\{\lambda_\nu\}$ be a sequence in $\mathcal{U}_0$ converging to $\lambda_0$. Choose a neighborhood $\mathcal{N}$ of $f^{-1}(\lambda_0) \cap \hat{X}$ in $\mathcal{M}$ such that $g(\mathcal{N}) \subset \bigcup_{j=1}^k \Delta_j$. For $\nu$ sufficiently large, $f^{-1}(\lambda_\nu) \cap \hat{X} \subset \mathcal{N}$, since otherwise a subsequence would have a limit point outside $f^{-1}(\lambda_0) \cap \hat{X}$. Hence for large $\nu$, each point of $g(f^{-1}(\lambda_\nu) \cap \hat{X})$ lies in some $\Delta_j$. Since there are at most $n$ distinct disks and $f^{-1}(\lambda_\nu)$ contains at least $n+1$ points, two points must lie in the same disk, so their distance is at most $2\epsilon$. Therefore $d_{n+1}(g(f^{-1}(\lambda_\nu))) \leq 2\epsilon \cdot M^{n(n-1)-1}$, where $M$ bounds $|g|$. Taking $\epsilon \to 0$ and then $\log$, we obtain the claim.

Now we apply the following proposition (a property of subharmonic functions):

**Proposition.** Given $\mathcal{U}_0$, $\alpha$, $E$ as above, and a subharmonic function $\chi$ on $\mathcal{U}_0$, if

$$\limsup_{\lambda \to \lambda_0, \, \lambda \in \mathcal{U}_0} \chi(\lambda) = -\infty$$

for each $\lambda_0 \in E$, then $\chi \equiv -\infty$ in $\mathcal{U}_0$.

By hypothesis, there exist $n+1$ distinct points $p_1, \ldots, p_{n+1} \in f^{-1}(\zeta) \cap \hat{X}$. Choose $g \in A$ with $g(p_1), \ldots, g(p_{n+1})$ distinct. Define $F(\lambda) = \log d_{n+1}(g(f^{-1}(\lambda) \cap \hat{X}))$ for $\lambda \in \mathcal{U}_0$. By Theorem 11.7 (applied to the maximum modulus algebra obtained via Theorem 11.9), $F$ is subharmonic in $\mathcal{U}_0$.

Since $g(p_1), \ldots, g(p_{n+1})$ are distinct, $d_{n+1}(g(f^{-1}(\zeta) \cap \hat{X})) \neq 0$, so $F(\zeta) > -\infty$.

On the other hand, by the Claim and the Proposition, $F \equiv -\infty$ in $\mathcal{U}_0$, and in particular $F(\zeta) = -\infty$. This is a contradiction. Hence $\# f^{-1}(\zeta) \cap \hat{X} \leq n$ for all $\zeta \in \mathcal{U}$. $\square$
