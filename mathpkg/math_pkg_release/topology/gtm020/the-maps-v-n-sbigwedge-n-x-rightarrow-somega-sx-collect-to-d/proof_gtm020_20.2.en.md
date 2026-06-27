---
locale: en
of_concept: the-maps-v-n-sbigwedge-n-x-rightarrow-somega-sx-collect-to-d
role: proof
source_book: gtm020
source_chapter: 20. General Theory of Characteristic Classes
source_section: '2'
---

By (1.3), $H_*(\Omega S(X)) = TH_*(X)$ over any field. Since $\bar{H}_*(\bigwedge_n X) = \bar{H}_*(X)^{\otimes n}$ over a field, we see that

$$H_*(v_n): S\bar{H}_*(X)^{\otimes n} = \bar{H}_*(S(\bigwedge_n X)) \rightarrow \bar{H}_*(S\Omega S(X))$$

maps isomorphically onto the suspension of the $n$th summand in $\bar{H}_*(\Omega S(X)) = \bigve

3.4 Remark. With the above notations for a map $f: S^r \rightarrow S^r$ of degree $q$, it follows that $\beta_n(f \times \dots \times f) = \Omega S(f)$,

$$\Omega S(f)_*: H_{nr}(\Omega S^{r+1}) \rightarrow H_{nr}(\Omega S^{r+1})$$

is multiplication by $q^r$, and the following diagram is commutative up to homotopy

$$\bigvee_{1 \leq n} S^{nr+1} \xrightarrow{v} S\Omega(S^{r+1})$$

$S(f) \wedge f \wedge \dots \wedge f \downarrow S^{nr+1} \xrightarrow{v} S\Omega(S^{r+1})$

Let $u: S\Omega S^{n+1} \rightarrow \bigvee_{1 \leq i} S^{ni+1}$ be a homotopy inverse of $v: \bigvee_{1 \leq i} S^{ni+1} \rightarrow S\Omega S^{n+1}$ considered in (3.3), and let $p_{(q)}: \bigvee_{1 \leq i} S^{ni+1} \rightarrow S^{nq+1}$ be the restriction to the wedge of the projection onto the $q$th factor. Form the composite $p_{(q)}u: S\Omega S^{n+1} \rightarrow S^{nq+1}$, take the adjoint map $\Omega S^{n+1} \rightarrow \Omega S^{nq+1}$, and make it into a fibre map which we will denote $f_{(q)}: \Omega S^{n+1} \rightarrow \Omega S^{nq+1}$ with $f_{(q)}(S^n) = *$. Let $F_n(q)$ denote the fibre of the map $f_{(q)}$. In fact $f_{(q)}: \Omega SX \rightarrow \Omega S(\bigwedge^q X)$ can be defined for any space $X$ where the map $v$

form $x = p^i \frac{a}{b}$ and $a, b$ are integers not divisible by the prime $p$. If $[x]$ denotes the largest integer $\leq x$, then one shows easily that

$$\text{ord}_p(k!) = \left[ \frac{k}{p} \right] + \left[ \frac{k}{p^2} \right] + \cdots + \left[ \frac{k}{p^i} \right] + \cdots$$

which is a finite sum terminating when $k < p^i$. When $q = p^j$ in (3.5) we calculate that

$$\text{ord}_p[k!(q!)^k/(qk)!] = \text{ord}_p(k!) + k \text{ord}_p(p^j!) - \text{ord}_p(p^jk!)$$

$$= \left[ \frac{k}{p} \right] + \left[ \frac{k}{p^2} \right] + \cdots + k(1 + p + \cdots + p^{j-1})$$

$$- \left( \left[ \frac{p^jk}{p} \right] + \cdots + \left[ \frac{p^jk}{p} \right] + \cdots \right) = 0$$

This means that $[k!(q!)^k/(qk)!]$ is a unit over any $Z_{(p)}$ - algebra $R$ and $(f_{(pj)})^*$: $H^{2knq}(\Omega S^{2nq+1}, R) \rightarrow H^{2knq}(\Omega S^{2n+1}, R)$ is an isomorphism. Moreover

$$\text{Tor}^{H*(\Omega S^{2nq+1}, R)}(R, H^*(\Omega S^{2n+1}, R)) = R \otimes_{H^*(\Omega S^{2nq+1}, R)} H^*(\Omega S^{2n+1}, R)$$

and this is the cohomology of the fibre $F_n(q)$ of $f_{(q)}$:

Proof. For $n$ odd, $n + 1$ is even and $H^*(\Omega S^{n+1}, R) = E(y, n) \otimes S'(z, 2n)$ and $f^*_2: H^*(\Omega S^{2n+1}, R) = S'(x, 2n) \rightarrow H^*(\Omega S^{n+1}, R)$ carries $H^*(\Omega S^{2n+1}, R)$ isomorphically onto the factor $S'(z, 2n)$, and $H^*(F_n, R) = E(y, n)$ so that $j^*: H^*(F_n, R) \rightarrow H^*(S^n, R)$ and $j^*_2: H^*(S^n, R) \rightarrow H^*(F_n, R)$ are isomorphisms for all $R$. This proves the first statement.

For $n$ even, $n + 1$ is odd and $j^*_2: H^*(S^n, R) \rightarrow H^*(F_n, R)$ is an isomorphism for each $Z_{(2)}$-algebra by (3.6). This proves the theorem.

The fibre map $f_{(2)}: (\Omega S^{n+1}, F_n(2)) \rightarrow (\Omega S^{2n+1}, *)$ induces an isomorphism $\pi^*_2(\Omega S^{n+1}, F_n(2)) \rightarrow \pi^*_2(\Omega S^{2n+1}, *)$ and leads to the following diagram with an exact triangle

$$\pi^*_2(S^n) \rightarrow \pi^*_2(F_n(2)) \rightarrow \pi^*_2(\Omega S^{n+1})$$

$$\pi^*_2(\Omega S^{2n+1}, F) \rightarrow \pi^*_2(\Omega S^{2n+1})$$

From this and (4.1) we deduce the single suspension sequences immediately. These are also called the $EHP$ sequences.

4

we see that $h(\alpha) = H(\alpha)\gamma_2(x)$ up to sign for any $\alpha \in \pi_{2n-1}(S^n) = \pi_{2n-2}(\Omega S^n, S^{n-1})$ and this provides an alternative formulation for the Hopf invariant $H: \pi_{2n-1}(S^n) \rightarrow Z$.
