role: introduce
locale: en
content_hash: ""
written_against: ""

Dirichlet's evaluation of $L(1,\chi)$ expresses the value at $s=1$ of the L-series attached to a nonprincipal Dirichlet character $\chi$ modulo a prime $\lambda$ as an explicit linear combination of logarithms of cyclotomic units. For each $\nu$, define

$$c_\nu = \frac{1}{\lambda} \sum_{j=1}^{\lambda-1} \chi(j) \alpha^{-j\nu},$$

where $\alpha$ is a primitive $\lambda$th root of unity. Then

$$L(1, \chi) = \sum_{\nu=1}^{\lambda-1} c_\nu \log \frac{1}{1 - \alpha^\nu}.$$

Reordering terms by powers of a primitive root $\gamma$ modulo $\lambda$ and setting $b_k = c_\nu$ with $\nu \equiv \gamma^k \bmod \lambda$, the formula becomes

$$L(1, \chi) = \sum_{k=0}^{\lambda-2} b_k \log \frac{1}{1 - \sigma^k \alpha},$$

where $\sigma$ is the conjugation $\alpha \mapsto \alpha^\gamma$. This explicit formula is a crucial ingredient in Kummer's class number formula for cyclotomic fields.
