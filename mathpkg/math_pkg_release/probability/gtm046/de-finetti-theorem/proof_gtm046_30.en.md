---
role: proof
locale: en
of_concept: de-finetti-theorem
source_book: gtm046
source_chapter: "VIII"
source_section: "30"
---

Let $G_m = F_{k_1 \cdots k_m}$ and set, for every $x \in R$, $$\xi_n(x) = \frac{1}{n} \sum_{j=1}^{n} I_{[X_{k_j} < x]}.$$ Since, as $m, n \to \infty$, $$E(\xi_m(x) - \xi_n(x))^2 = \frac{|m-n|}{mn} (G_1(x) - G_2(x, x)) \to 0,$$ it follows that there exists a r.v. $\xi(x)$ such that $E(\xi_n(x) - \xi(x))^2 \to 0$, and hence $\xi_n(x) \xrightarrow{P} \xi(x)$. Since the $\xi_n(x)$ are bounded by 1, it follows, by the dominated convergence theorem and a.s. invariance under finite permutations of $X$'s of $B \in \mathcal{B} = \mathcal{B}(\xi(x), x \in R)$, that $$E(\xi(x_1) \cdots \xi(x_m) I_B) \leftarrow E(\xi_n(x_1) \cdots \xi_n(x_m) I_B) \rightarrow P([X_1 < x_1, \cdots, X_m < x_m] I_B).$$ Thus $P^{\mathcal{B}}[X_1 < x_1, \cdots, X_m < x_m] = \xi(x_1) \cdots \xi(x_m)$ a.s. Finally, since $\xi_n(\omega, x)$ is a d.f. in $x$, $\xi(\omega, x)$ has a.s. the properties of a d.f. in $x$.
