---
role: proof
locale: en
of_concept: explicit-hull-over-circle
source_book: gtm035
source_chapter: "Chapter 20"
source_section: "20.5"
---
# Proof of Explicit Description of Polynomial Hull Over Circle

**Theorem 20.5.** For each $\lambda \in \Lambda$ (where $\Lambda = \{|\lambda| < 1\}$), we have

(16) $\{w : D(\lambda, w) \geq 0\}$ is a nondegenerate closed disk, and

(17) $\hat{Y}_{\lambda} = \left\{ \frac{P(\lambda)}{Q(\lambda)} + \frac{w}{Q_0(\lambda)} : D(\lambda, w) \geq 0 \right\}$,

where $D(\lambda, w)$ is the determinant matrix function associated with the Pick-Nevanlinna interpolation problem for the points $\lambda_1, \ldots, \lambda_n$ and values $w_1, \ldots, w_n$, and $Q_0(\lambda) = \prod_{i=1}^{n} \frac{\lambda - \lambda_i}{1 - \bar{\lambda}_i \lambda}$.

**Proof.** We first claim that $D(\lambda, w) > 0$ implies

$$\frac{P(\lambda)}{Q(\lambda)} + \frac{w}{Q_0(\lambda)} \in \hat{Y}_{\lambda}.$$

To prove the claim, fix $\lambda \in \Lambda$ and $w$ with $D(\lambda, w) > 0$. Choose $0 < r < 1$ such that the matrix $M^*$ obtained by replacing each entry $\frac{1 - w_i \bar{w}_j}{1 - \lambda_i \bar{\lambda}_j}$ by $\frac{r^2 - w_i \bar{w}_j}{r^2 - \lambda_i \bar{\lambda}_j}$ remains positive definite. Define

$$B_0(\zeta) = r B(\zeta/r)$$

for a suitable $B \in H^\infty$ with $\|B\|_\infty \leq 1$ and $B(\lambda_j/r) = w_j/r$. Then for a.a. $\zeta \in \Gamma$,

$$|B_0(\zeta)| \leq r.$$

Hence $\|B_0\|_\infty \leq r$. Set $w' = (w - P(\lambda)/Q(\lambda)) Q_0(\lambda)$. We then have $B_0(\lambda_j) = w_j$, $1 \leq j \leq n$ and $B_0(\lambda) = w'$. By Pick's Theorem, it follows that

(20) $M(\lambda_1, \ldots, \lambda_n, \lambda \mid w_1, \ldots, w_n, w')$ is positive definite,

and hence $D(\lambda, w') > 0$. The claim is proved.

Further, (20) implies that

(21) $M(\lambda_1, \ldots, \lambda_n \mid w_1, \ldots, w_n)$ is positive definite.

Now fix $w$ with $D(\lambda, w) > 0$. Then the matrix $M(\lambda_1, \ldots, \lambda_n, \lambda \mid w_1, \ldots, w_n, w)$ has all of its principal minors positive, because (20) shows this for all but the $(n+1) \times (n+1)$ minor, which equals $D(\lambda, w)$. It follows that $M(\lambda_1, \ldots, \lambda_n, \lambda \mid w_1, \ldots, w_n, w)$ is positive definite.

By Pick's Theorem, then, there exists $B \in H^\infty$, $\|B\|_\infty < 1$, with $B(\lambda_j) = w_j$, $1 \leq j \leq n$, and $B(\lambda) = w$. By Lemma 20.4, then

$$f = \frac{P}{Q} + \frac{B}{Q_0} \in \mathcal{F},$$

and so

$$\frac{P(\lambda)}{Q(\lambda)} + \frac{w}{Q_0(\lambda)} \in \hat{Y}_{\lambda}.$$

Assume next that $D(\lambda, w) \geq 0$. By the claim, $w = \lim_{n \to \infty} w_n$ for a sequence of points $w_n$ with $D(\lambda, w_n) > 0$. By the previous paragraph, each $\frac{P(\lambda)}{Q(\lambda)} + \frac{w_n}{Q_0(\lambda)} \in \hat{Y}_{\lambda}$, and since $\hat{Y}_{\lambda}$ is closed, the limit $\frac{P(\lambda)}{Q(\lambda)} + \frac{w}{Q_0(\lambda)} \in \hat{Y}_{\lambda}$.

Conversely, let $w \in \hat{Y}_{\lambda}$. By Theorem 20.2, there exists $f \in \mathcal{F}$ with $f(\lambda) = w$. By Lemma 20.4, $f = P/Q + B/Q_0$ with $B \in H^\infty$, $\|B\|_\infty \leq 1$, $B(\lambda_j) = w_j$. Setting $w' = B(\lambda)$, we have $w = P(\lambda)/Q(\lambda) + w'/Q_0(\lambda)$. By Pick's Theorem, the interpolation data yield $D(\lambda, w') \geq 0$. Hence $w$ belongs to the set described in (17).

For the continuity of fibers: consider a sequence $\{z_\nu\}$ in $\Lambda$ approaching $b \in \Gamma$. By Theorem 20.5, the fiber for each $z_\nu$ is a closed disk $D_\nu$. By the compactness of $\hat{Y}$, after passing to a subsequence, these disks converge to a nondegenerate disk $E \subseteq \hat{Y}_b$.

**Claim.** $E = \hat{Y}_b$.

Let $w \in \hat{Y}_b$. By Theorem 20.2, there exists $f \in \mathcal{F}$ such that $f(b) = w$. Also, $f(z_\nu) \in D_\nu$. Since $\lim_{\nu \to \infty} f(z_\nu) = f(b)$, we conclude that $w = f(b) \in E$. This shows that $E \supseteq \hat{Y}_b$ and gives the claim.

Thus we have that the fiber $\hat{Y}_b$ is a nondegenerate disk and that for every sequence $\{z_\nu\}$ in $\Lambda$ there is a subsequence whose fibers converge to $\hat{Y}_b$. This yields the desired continuity of the fibers. ∎
