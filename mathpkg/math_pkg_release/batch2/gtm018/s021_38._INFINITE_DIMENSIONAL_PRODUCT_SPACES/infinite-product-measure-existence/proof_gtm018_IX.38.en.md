---
role: proof
locale: en
of_concept: infinite-product-measure-existence
source_book: gtm018
source_chapter: "IX"
source_section: "38. Infinite Dimensional Product Spaces"
---

In view of 9.F and 13.A, all we have to prove is that the set function $\mu$ on the algebra $\mathbf{F}$ of all finite dimensional measurable sets is continuous from above at $0$, i.e. that if $\{E_j\}$ is a decreasing sequence of sets in $\mathbf{F}$ such that $0 < \epsilon \leq \mu(E_j)$, $j = 1, 2, \cdots$, then $\bigcap_{j=1}^{\infty} E_j \neq \emptyset$.

If $F_j = \left\{x_1 : \mu^{(1)}(E_j(x_1)) > \frac{\epsilon}{2}\right\}$, then it follows from the relation

$$\mu(E_j) = \int \mu^{(1)}(E_j(x_1)) \, d\mu_1(x_1) = \int_{F_j} \mu^{(1)}(E_j(x_1)) \, d\mu_1(x_1) + \int_{F_j'} \mu^{(1)}(E_j(x_1)) \, d\mu_1(x_1)$$

that $\mu(E_j) \leq \mu_1(F_j) + \frac{\epsilon}{2}$, and therefore that

$$\mu_1(F_j) \geq \frac{\epsilon}{2}.$$

Since $\{F_j\}$ is a decreasing sequence of measurable subsets of $X_1$ (for $\{E_j\}$ is decreasing), and since $\mu_1(F_j) \geq \epsilon/2$, the measure $\mu_1$ being continuous from above at $0$ implies that there exists a point $\bar{x}_1$ belonging to every $F_j$, $j = 1, 2, \cdots$. Consequently

$$\mu^{(1)}(E_j(\bar{x}_1)) \geq \frac{\epsilon}{2}, \quad j = 1, 2, \cdots.$$

Observe next that if $E$ is a $\{1, \cdots, k\}$-cylinder, then $E(x_1)$ is a $\{2, \cdots, k\}$-cylinder in $X^{(1)}$. Applying the same reasoning to the sequence $\{E_j(\bar{x}_1)\}$ in $X^{(1)}$, we obtain a point $\bar{x}_2 \in X_2$ such that

$$\mu^{(2)}(E_j(\bar{x}_1, \bar{x}_2)) \geq \frac{\epsilon}{4}, \quad j = 1, 2, \cdots.$$

Continuing in this manner, we obtain a sequence $\{\bar{x}_1, \bar{x}_2, \cdots\}$ such that $\bar{x}_n \in X_n$, $n = 1, 2, \cdots$, and

$$\mu^{(n)}(E_j(\bar{x}_1, \cdots, \bar{x}_n)) \geq \frac{\epsilon}{2^n}, \quad j = 1, 2, \cdots.$$

The point $(\bar{x}_1, \bar{x}_2, \cdots)$ belongs to $\bigcap_{j=1}^{\infty} E_j$. To prove this assertion, we consider any particular $E_j$ and we select the positive integer $n$ so that $E_j$ is a $\{1, \cdots, n\}$-cylinder. The fact that $\mu^{(n)}(E_j(\bar{x}_1, \cdots, \bar{x}_n)) > 0$ implies that $E_j$ contains at least one point $(x_1, x_2, \cdots)$ such that $x_i = \bar{x}_i$ for $i = 1, \cdots, n$. The fact that $E_j$ is a $\{1, \cdots, n\}$-cylinder implies then that $(\bar{x}_1, \bar{x}_2, \cdots)$ itself belongs to $E_j$.
