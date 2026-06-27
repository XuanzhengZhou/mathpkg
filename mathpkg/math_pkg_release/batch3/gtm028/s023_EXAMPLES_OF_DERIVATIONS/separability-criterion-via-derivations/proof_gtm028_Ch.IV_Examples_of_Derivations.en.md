---
role: proof
locale: en
of_concept: separability-criterion-via-derivations
source_book: gtm028
source_chapter: "IV"
source_section: "Examples of Derivations"
---

**Necessity.** Suppose $F$ is separable over $K$, i.e., $F$ and $K^{1/p}$ are linearly disjoint over $K$. Then $F^p$ and $K$ are linearly disjoint over $K^p$ (since $x \mapsto x^p$ is an isomorphism). Let $\{u_\alpha\}$ be a basis of $F^p$ as a vector space over $K^p$, with multiplication table $u_\alpha u_\beta = \sum_\gamma c_{\alpha\beta\gamma} u_\gamma$ where $c_{\alpha\beta\gamma} \in K^p$.

Then $\{u_\alpha\}$ is also a basis of the ring $K[F^p]$ as a vector space over $K$. Let $D$ be a derivation of $K$. Every element $x$ of $K[F^p]$ can be written uniquely as $x = \sum_\alpha x_\alpha u_\alpha$ with $x_\alpha \in K$ (finitely many non-zero). Define
$$D'(x) = \sum_\alpha D(x_\alpha) u_\alpha.$$
Then $D'$ is additive. For any two elements $x = \sum_\alpha x_\alpha u_\alpha$ and $y = \sum_\beta y_\beta u_\beta$,
$$D'(xy) = D'\Bigl(\sum_{\alpha,\beta,\gamma} x_\alpha y_\beta c_{\alpha\beta\gamma} u_\gamma\Bigr) = \sum_{\alpha,\beta,\gamma} D(x_\alpha y_\beta c_{\alpha\beta\gamma}) u_\gamma.$$
Since $c_{\alpha\beta\gamma} \in K^p$, we have $D(c_{\alpha\beta\gamma}) = 0$ (as $D$ vanishes on $p$-th powers). Hence
$$D(x_\alpha y_\beta c_{\alpha\beta\gamma}) = D(x_\alpha) y_\beta c_{\alpha\beta\gamma} + x_\alpha D(y_\beta) c_{\alpha\beta\gamma},$$
which yields $D'(xy) = x D'(y) + y D'(x)$. Thus $D'$ is a derivation on $K[F^p]$, and by the quotient rule it extends uniquely to $F$.

**Sufficiency.** Suppose every derivation of $K$ extends to $F$, but $F$ is not separable over $K$. Then $F$ and $K^{1/p}$ are not linearly disjoint over $K$, so there exist elements of $F$ that are linearly dependent over $K$ but not over $K^p$. Choose a minimal dependence relation $\sum_{i=1}^t a_i x_i = 0$ with $a_i \in K$ not all in $K^p$ and $x_i \in F$ linearly independent over $K^p$. By minimality, $t \geq 2$ and all $a_i \neq 0$. We may rescale so that $a_1 = 1$, and by minimality some $a_i \notin K^p$.

Since $a_2 \notin K^p$, there exists a derivation $D$ of $K$ with $D(a_2) \neq 0$ (by the remark after Corollary 5 of Theorem 39, an element annihilated by all derivations lies in $K^p$). Applying the extended derivation $D'$ to the relation $\sum a_i x_i = 0$ yields
$$\sum_i D(a_i) x_i + \sum_i a_i D'(x_i) = 0.$$
If $D(a_i) = 0$ for all $i$, then $D(a_2) = 0$, contradiction. Hence some $D(a_i) \neq 0$. After reindexing, suppose $D(a_2), \ldots, D(a_n) \neq 0$ and $D(a_{n+1}) = \cdots = D(a_t) = 0$. The above relation gives a dependence with fewer terms:
$$\sum_{i=2}^n D(a_i) x_i + \sum_{i=n+1}^t a_i D'(x_i) = 0,$$
contradicting minimality of $t$. Hence $F$ must be separable over $K$.
