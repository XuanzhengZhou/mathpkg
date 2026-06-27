---
role: proof
locale: en
of_concept: proposition-7-10
source_book: gtm040
source_chapter: "7"
source_section: "10"
---

**Proof:** We note that hypothesis (3) is equivalent to

(3') For any state 0 and for any given $m$, there exist only finitely many states $j$ for which $F_{0j}^{(k)} \neq 0$ for some $k \leq m$.

If the conclusion about $H_{0j}$ is false, then for some $\epsilon > 0$ and for infinitely many $j$ we have $H_{0j} > \epsilon$. By (1), $N$ is finite-valued. Therefore,

$$\lim_{k \to \infty} P^k N = \lim_{k \to \infty} [N - (I + \cdots + P^{k-1})] = 0$$

and

$$\lim_{k \to \infty} P^k \bar{H} = 0$$

since $\bar{H} \leq H \leq N$. Choose $m$ large enough so that $(P^m \bar{H})_{00} < \epsilon^2$. Since there are infinitely many $j$ such that $H_{0j} > \epsilon$, we can find by (3') such a $j$ with $F_{0j}^{(k)} = 0$ for all $k \leq m$. Then

$$\Pr_0[\text{hit } 0 \text{ after time } m] \geq \Pr_0[\text{ever hit } j \text{ and return to } 0]$$

$$= H_{0j} H_{j0}$$

$$= H_{0j} H_{0j} \quad \text{by (2)}$$

$$> \epsilon^2.$$

But

$$\Pr_0[\text{hit } 0 \text{ after time } m] = (P^m \bar{H})_{00} < \epsilon^2,$$

a contradiction. Therefore $H_{0j} \to 0$.
