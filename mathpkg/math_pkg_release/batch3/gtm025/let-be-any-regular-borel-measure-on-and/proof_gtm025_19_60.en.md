---
role: proof
locale: en
of_concept: "let-be-any-regular-borel-measure-on-and"
source_book: gtm025
source_chapter: "Complex Analysis"
source_section: "19.60"
---

Suppose first that $\iota$ and $\lambda$ are not mutually singular. By (19.42), we have $\iota = \iota_1 + \iota_2$, where $\iota_1 \neq 0, \iota_1 \ll \lambda$, and $\iota_2 \perp \lambda$. Then $\iota_1$ is a regular measure, as (19.49) shows.1

Next suppose that $\iota_1 \rightarrow \alpha_1$, i.e., $\iota_1 = \lambda_{\alpha_1}$. Then $\alpha_1$ is absolutely continuous on every interval $[-p, p]$ (19.53), and (19.45) and (18.16) imply that

$$\iota_1([0, x[) = \alpha_1(x

From (18.14) we have

$$\sigma([a, b]) = \int_a^b \alpha'(t) dt \leq \alpha(b) - \alpha(a) = \iota([a, b])$$

for all $a < b$ in $R$. Like $\iota_1$ in the preceding paragraph, $\sigma$ is a regular Borel measure on $R$. It follows from (3), as in the proof of (19.48), that

$$\sigma(E) \leq \iota(E)$$

for all $E \in \mathcal{B}(R)$. Combining (1), (2), (4), and (19.59), we see that $\iota \perp \lambda$ cannot obtain. Thus $\iota \perp \lambda$ implies $\alpha' = 0$ a.e. $\square$.

We now present our main decomposition theorem for regular Borel measures on $R$ and their corresponding nondecreasing functions.
