---
role: proof
locale: en
of_concept: example-4-non-minimal-boundary-point
source_book: gtm040
source_chapter: "10"
source_section: "13"
---

Define the state space $S = \{a_i, a'_i, b_i \mid i = 0, 1, 2, \ldots\}$ with non-zero transition probabilities

$$P_{a_{i-1}a_i} = p_i, \quad P_{a_{i-1}b_{i-1}} = q_i = 1 - p_i,$$
$$P_{b_{i-1}b_i} = r_i,$$
$$P_{a'_{i-1}a'_i} = p_i, \quad P_{a'_{i-1}b_{i-1}} = q_i.$$

Set $\pi a_0 = \pi a'_0 = 1/2$, so that $\pi N > 0$. Since the process visits each state at most once, $H = N$.

The three sequences $\{a_i\}$, $\{a'_i\}$, and $\{b_i\}$ are each Cauchy. Computing $K(\cdot, a_j)$ for large $j$ gives $K(a'_i, a_j) = K(b_i, a_j) = 0$ and for $i \leq j$,

$$K(a_i, a_j) = \frac{H_{a_i a_j}}{H_{\pi a_j}} = \frac{2}{\beta_i}.$$

Hence $a_\infty = \lim a_j$ satisfies $K(a_i, a_\infty) = 2/\beta_i$. Similarly $a'_\infty$ satisfies $K(a'_i, a'_\infty) = 2/\beta_i$.

For the $b$-sequence, computing $K(a_i, b_j)$ for $i \leq j$ yields

$$K(a_i, b_j) = \frac{1}{\beta_i}\left(1 + \frac{\sigma_i}{\sigma_j}\right),$$

and taking the limit as $j \to \infty$ (using $\sigma_\infty = +\infty$), we obtain

$$K(a_i, b_\infty) = \frac{1}{\beta_i} = \frac{1}{2} \cdot \frac{2}{\beta_i} = \frac{1}{2}K(a_i, a_\infty) + \frac{1}{2}K(a_i, a'_\infty).$$

Thus there are exactly three boundary points, with

$$K(\cdot, b_\infty) = \frac{1}{2}K(\cdot, a_\infty) + \frac{1}{2}K(\cdot, a'_\infty),$$

so $b_\infty$ is not extreme. By the representation theorem, $B_e = \{a_\infty, a'_\infty\}$, and both are minimal.

The condition $\sigma_\infty = +\infty$ can be satisfied with either $\beta_\infty = 0$ (take $p_j = q_j = r_j = 1/2$) or $\beta_\infty > 0$ (take $p_j = \frac{j(j+2)}{(j+1)^2}$, $q_j = \frac{1}{(j+1)^2}$, $r_j = \frac{j+1}{j+2}$).
