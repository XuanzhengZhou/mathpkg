---
role: proof
locale: en
of_concept: plh-approximation-2-manifold-boundary-r2
source_book: gtm047
source_chapter: "5"
source_section: "10"
---

If $L$ is a subdivision of $K$, and $\psi \gg 0$ on the $1$-skeleton $|L^1|$, then we can apply the preceding theorem to the restriction $h \mid |L^1|$, getting a PL approximation $f \mid |L^1|$. By the combinatorial Schönflies theorem (Theorem 5.3), together with Theorem 5.4, each PLH $f \mid \operatorname{Bd} \sigma^2$ ($\sigma^2 \in L$) can be extended to give a PLH $f \mid \sigma^2$. Thus we need to choose $L$ and $\psi$ in such a way that (1) the PL homeomorphisms $f \mid \sigma^2$ fit together so as to give a PLH $f: |L| \to \mathbb{R}^2$ and (2) $f$ is a $\phi$-approximation of $h$.

For each $2$-simplex $\sigma$ of a subdivision $L$ of $K$, let $\tau$ be the $2$-simplex of $K$ that contains $\sigma$; let $\varepsilon_\tau = \inf (\phi \mid \tau)$, and let

$$\varepsilon_\sigma = \frac{1}{3} \varepsilon_\tau.$$

We choose $L$ as a sufficiently fine subdivision so that for each $\sigma \in L$,

$$\delta h(\sigma) < \varepsilon_\sigma.$$

Let $A$ and $B$ be sets of points in a metric space. We define the Hausdorff distance as

$$\delta(A, B) = \max \left\{ \sup_{a \in A} d(a, B), \sup_{b \in B} d(A, b) \right\}.$$

Then

$$\delta N(h(\sigma), \varepsilon_{\sigma}) < 3\varepsilon_{\sigma} = \varepsilon_{\tau}.$$

If $P \in \sigma \subset \tau$, then $h(P)$ and $f(P)$ both lie in $N(h(\sigma), \varepsilon_{\sigma})$; and we know that $\phi(P) \geqslant \varepsilon_{\tau}$. It follows that $f$ is a $\phi$-approximation of $h$.

It remains to show that $f$ is a homeomorphism; and for this purpose it will be sufficient to show that different sets $\operatorname{Int} f(\sigma)$, where $\sigma$ is a $2$-simplex of $L$, are disjoint. If $\sigma_1 \neq \sigma_2$, then $\sigma_2$ has a vertex $w$ which does not lie in $\sigma_1$. By the definition of $\psi$, we have

$$f(\sigma_1) \subset N(h(\sigma_1), \theta_{\sigma_1})$$

and

$$\theta_{\sigma_1} \leqslant d(h(\sigma_1), h(K^0 - \sigma_1)).$$

It follows that $w \notin f(\sigma_1)$, and so $\operatorname{Int} f(\sigma_1)$ and $\operatorname{Int} f(\sigma_2)$ are disjoint. This completes the proof.
