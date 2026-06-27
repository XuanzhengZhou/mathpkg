---
role: proof
locale: en
of_concept: prop-for-random-walk-satisfying-a-b
source_book: gtm034
source_chapter: "4"
source_section: "009"
---

Proof: First we obtain the limit behavior of $u(x)$ which is quite independent of conditions (b) and (c). One simply goes back to P18.8 to obtain

$$\lim_{x \to +\infty} u(x) = \frac{\sqrt{c}}{\mathbf{E}[-\bar{Z}]} = k_1 > 0,$$

provided that $\mathbf{E}[-\bar{Z}] < \infty$. But by P18.2 $\mathbf{E}[Z] < \infty$ for random walk with finite positive mean, and therefore $\mathbf{E}[-\bar{Z}]$ is finite for random walk satisfying (a).

The proof of the second

$I_r$ with endpoints 1 and $r$ (we still have to prove that $r > 1$, so that $I_r = [1,r]$). Now

$$f'(\rho) = \sum_{n=-\infty}^{\infty} n \rho^{n-1} P(0,n) \text{ for } \rho \in I_r,$$

and

$$f''(\rho) = \sum_{n=-\infty}^{\infty} n(n-1) \rho^{n-2} P(0,n) > 0$$

for all $\rho$ in the interior of $I_r$. The last sum is positive since $P(0,n) > 0$ for some $n < 0$ (for otherwise (a) could not hold). Hence $f(\rho)$ is convex in the interior of $I_r$ so that condition (c), which states that $f'(r) > 0$, implies $1 < r$. Finally $r$ is unique, for if there are two values $r_1$ and $r_2$ satisfying (b) and (c), with $1 < r_1 \leq r_2$, then $f(\rho)$ is strictly convex on $(1,r_2)$. But by (a) we have $f(1) = f(r_1) = f(r_2)$ which implies $r_1 = r_2$.

The rest of the proof depends on the elegant device of defining a new, auxiliary random walk. Let

$$P^{(r)}(x,y) = P(x,y)r^{y-z}, \quad x,y \in R.$$

Condition (b) implies that $P^{(r)}$ is a transition function of an aperiodic random walk, as it gives

$$\sum_{y \in R} P^{(r)}(x,y) = 1, \quad x \in R,$$

and obviously $P^{(r)}$ is a difference kernel, it is non-negative, and the aperiodicity of $P$ is also preserved. The random walk defined by $P^{(r)}$ has positive mean $\mu^{(r)}$ in view of (c). Now let $g^{(r)}(x,y)$ be the Green function of the half-line $B = [x \mid x \leq -1]$

devoid of any obvious probability interpretation. Using the obvious notation one writes

$$g(x,y) = \sum_{n=0}^{\infty} Q_n(x,y),$$

$$g^{(r)}(x,y) = \sum_{n=0}^{\infty} Q_n^{(r)}(x,y).$$

For $x,y$ in $R-B$ (otherwise there is nothing to prove),

$$Q_1^{(r)}(x,y) = P(x,y)r^{y-z},$$

and

$$Q_{n+1}^{(r)}(x,y) = \sum_{t \in R-B} Q_1^{(r)}(x,t)Q_n^{(r)}(t,y)$$

gives

$$Q_n^{(r)}(x,y) = Q_n(x,y)r^{y-z},$$

which implies (1).

Proceeding from (1),

(2) $$u^{(r)}(x)v^{(r)}(0) = g^{(r)}(x,0) = r^{-z}g(x,0) = r^{-z}u(x)v(0),$$

(3) $$u^{(r)}(0)v^{(r)}(y) = g^{(r)}(0,y) = g(0,y)r^y = u(0)v(y)r^y.$$

We shall use only (3). The random walk $P^{(r)}$ is aperiodic with positive mean. To its ladder random variable $Z$ we give the name $Z^{(r)}$. Since we know by P18.2 that $E[Z^{(r)}] < \infty$, P18.8 gives

$$\lim_{y \to +\infty} v^{(r)}(y) = \frac{1}{\sqrt{c^{(r)}E[Z^{(r)}]}} = k > 0,$$

where $c^{(r)}$ is $c(1) = c$ for the $P^{(r)}$ random walk. Finally equation (3) implies

$$\lim_{y \to +\infty} v(y)r^y = \frac{u^{(r)}(0)}{u(0)} k = k_2 > 0.$$

completing the proof of P6.

E4 Let us paraphrase P
