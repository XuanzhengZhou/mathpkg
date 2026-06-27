---
role: proof
locale: en
of_concept: tower-degree-theorem
source_book: gtm077
source_chapter: "20"
source_section: "20"
---
# Proof of Theorem 59: Tower Law for Relative Degrees

**Theorem 59 (Tower Degree Theorem).** Let $k$ be a field and let $K = K(\alpha; k)$ be an extension of relative degree $m$. Let $\beta$ be an algebraic number over $K$ of relative degree $q$. Then the composed field $K(\alpha, \beta; k)$ has relative degree

$$[K(\alpha, \beta; k) : k] = mq.$$

Moreover, if $\theta$ is a generating element of $K(\alpha, \beta; k)$ over $k$ and $\theta_1, \ldots, \theta_n$ (with $n = mq$) are its $n$ conjugates with respect to $k$, then these conjugates decompose into $m$ sequences of $q$ elements each, where the $q$ numbers of a given sequence are precisely the conjugates of $\theta$ (and hence of $\beta$) with respect to $K(\alpha_i; k)$, for $\alpha_1, \ldots, \alpha_m$ the $m$ conjugates of $\alpha$ over $k$.

*Proof.* By the primitive element theorem (Theorem 52), the field $K(\alpha, \beta; k)$ is a simple extension of $k$: there exists $\theta$ such that $K(\alpha, \beta; k) = K(\theta; k)$. Let the degree of this extension be $n$.

Consider the tower of fields:

$$k \subset K(\alpha; k) \subset K(\alpha, \beta; k).$$

We have $[K(\alpha; k) : k] = m$ by hypothesis, and $[K(\alpha, \beta; k) : K(\alpha; k)] = q$ because $\beta$ has degree $q$ over $K(\alpha; k)$. By the standard degree formula for finite extensions (composition of basis extensions), an $m$-element basis of $K(\alpha; k)$ over $k$ and a $q$-element basis of $K(\alpha, \beta; k)$ over $K(\alpha; k)$ produce an $mq$-element basis of $K(\alpha, \beta; k)$ over $k$. Hence $n = mq$.

Explicitly, let $1, \alpha, \ldots, \alpha^{m-1}$ be a basis of $K(\alpha; k)$ over $k$ (after reduction modulo the minimal polynomial of $\alpha$, by Theorem 53). Let $1, \beta, \ldots, \beta^{q-1}$ be a basis of $K(\alpha, \beta; k)$ over $K(\alpha; k)$. Then the $mq$ products $\alpha^i \beta^j$ ($0 \leq i < m$, $0 \leq j < q$) span $K(\alpha, \beta; k)$ over $k$. Moreover, these $mq$ numbers are linearly independent over $k$: a relation

$$\sum_{i=0}^{m-1} \sum_{j=0}^{q-1} c_{ij} \alpha^i \beta^j = 0 \qquad (c_{ij} \in k)$$

can be rewritten as $\sum_{j=0}^{q-1} (\sum_i c_{ij} \alpha^i) \beta^j = 0$, where the coefficients $\sum_i c_{ij} \alpha^i$ lie in $K(\alpha; k)$. By linear independence of $1, \beta, \ldots, \beta^{q-1}$ over $K(\alpha; k)$, each $\sum_i c_{ij} \alpha^i = 0$. Then by linear independence of $1, \alpha, \ldots, \alpha^{m-1}$ over $k$, each $c_{ij} = 0$. Thus $n = mq$.

For the decomposition of conjugates, let $\alpha_1 = \alpha, \alpha_2, \ldots, \alpha_m$ be the conjugates of $\alpha$ over $k$. For each $i$, let $K_i = K(\alpha_i; k)$ be the isomorphic copy of $K(\alpha; k)$. The minimal polynomial of $\beta$ over $K(\alpha; k)$, say $\varphi(x) \in K(\alpha; k)[x]$, has degree $q$. Applying the isomorphism $\sigma_i : K(\alpha; k) \to K_i$, we obtain conjugated polynomials $\varphi_i(x) \in K_i[x]$, each of degree $q$. The $mq$ roots of all $\varphi_i(x)$ together (counting multiplicities) form the complete set of conjugates of $\theta$ (or of a suitable primitive element) over $k$. For each fixed $i$, the $q$ roots of $\varphi_i(x)$ are the conjugates of $\beta$ with respect to $K_i = K(\alpha_i; k)$. Thus the $n = mq$ conjugates decompose into $m$ blocks of $q$ elements each, corresponding to the $m$ embeddings of $K(\alpha; k)$.

An alternative constructive proof: Let $\omega^{(1)}, \ldots, \omega^{(m)}$ be a fundamental system of $K(\alpha; k)$ over $k$, and let $\eta^{(1)}, \ldots, \eta^{(q)}$ be a fundamental system of $K(\alpha, \beta; k)$ over $K(\alpha; k)$. Then the $mq$ products $\omega^{(i)} \eta^{(j)}$ form a fundamental system of $K(\alpha, \beta; k)$ over $k$, confirming $n = mq$. $\square$
