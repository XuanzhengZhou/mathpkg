---
role: proof
locale: en
of_concept: main-lemma-highly-divisible-x
source_book: gtm059
source_chapter: ""
source_section: "9. Explicit Reciprocity Laws"
---

The proof proceeds in three steps.

**Step 1.** Using the expression involving the mapping $\psi_n$ from Chapter 8, formula (15.7):
$$(x_n) = \bigl[T_{1/\sqrt{2}} I(x_n) I(x_n)\bigr] n_n.$$
Since $I(x_n) \equiv 1 \bmod x^{n+1}$ and $T_{1/\sqrt{2}} I(x_n)$ is a unit, it suffices to replace $I(x)$ by $x$ on the right-hand side, for which we require
$$T_{1/\sqrt{2}}\Bigl(\frac{x^2}{\sqrt{2} I(x_n)}\Bigr) \equiv 0 \bmod x^{n+1}.$$
Since $I(x_n)$ is a unit, this is equivalent to requiring
$$2\alpha(n) - n - 3 = \frac{9}{2} - \frac{1}{2} \bmod 1 \geq 0.$$
Certainly $n \geq n+2$ and $2$ suffices. Using Taylor's formula and the fact that $V(\lambda)$ has integral coefficients with $d(\alpha)=0$:
$$\Delta(\alpha) + \alpha n \equiv V(\alpha)x \bmod \frac{2^{\alpha(n)}}{2},$$
provided $v(\alpha) \geq \varepsilon$. It suffices to take
$$v(\alpha) \geq \frac{9}{2} + 1 + 2\alpha.$$
Since $T_n[\Delta(\alpha)]_{n+1} V(\alpha)x \equiv 0 \bmod n^{s+1}$, we may replace $V(\alpha)x$ by $d(\alpha) + x$ to conclude Step 1.

**Step 2.** Formally this is the alternating property LS 4 of the symbol $(x, \alpha) = 0$, but the proof must be adjusted because the groups on the right and left are not symmetric. We have:
$$0 = (x, n+x, n+x) = \bigl\langle x+n, 1+\tfrac{x}{n}\bigr\rangle \bigl\langle x+n, x+n\bigr\rangle$$
$$= \bigl\langle x+n, 1-\tfrac{x}{n}\bigr\rangle \bigl\langle x+n, x+n\bigr\rangle$$
$$= \bigl\langle x+n, \tfrac{x}{n}\bigr\rangle \bigl\langle x+n, x+n\bigr\rangle.$$

Let $F(X,Y)$ be the group law on a slice with $F(0,Y)=Y$ and $F(X,0)=X$. Then $F(X,Y) = X+Y \bmod XY$. It follows that $(x+s_n) - |x_n| \equiv 0 \bmod n^n$. Taking $r = r(n)-1$ and solving $1+y = w$ with a unit $u$ for $y = x/u$, we use the fact that the algorithm proves the order in the other lemma for order $n>1$ is $1$. Any integer $d$ satisfying
$$0 \leq d \leq d \bmod y - \frac{1}{p-1}$$
suffices, or in terms of $x$:
$$0 \leq d \leq \frac{2(s_n)}{p} - \frac{1}{p-1}.$$
In particular $0 \leq d \leq \frac{1}{p}(n-1)$ suffices. Picking $v(n) = [a2] + 1 + 2w$ completes Step 2.

**Step 3.** Let $y = x/u$ and $n = 1+y$. Then:
$$(s_n + s_n + y) = (s_n + 1 + y) = \frac{1}{2}\Bigl[\frac{1}{n}\bigl(N(1+y)\bigr)^2 - 1\Bigr](s_n).$$
We contend that
$$N(1+y) \equiv -1 \bmod n^{n+1},$$
from which it follows that
$$(s_n + s_n + x) = \Bigl[\frac{1}{2}\frac{1}{n} T(1,y)\Bigr](s_n),$$
concluding the proof of the main lemma.
