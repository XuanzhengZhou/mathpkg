---
role: proof
locale: en
of_concept: jp-expressed-as-polynomial-in-phi
source_book: gtm041
source_chapter: "4"
source_section: "4.10"
---

We have the Fourier expansions
$$j(\tau) = x^{-1} + c(0) + c(1)x + c(2)x^2 + \cdots,$$
$$j_p(\tau) = c(0) + c(p)x + c(2p)x^2 + \cdots,$$
$$p\,j_p(p\tau) = p\,c(0) + p\,c(p)x^p + p\,c(2p)x^{2p} + \cdots,$$
and
$$j(p^2\tau) = x^{-p^2} + c(0) + c(1)x^{p^2} + c(2)x^{2p^2} + \cdots.$$

Substituting these into the identity
$$j_p\left(-\frac{1}{p\tau}\right) = j_p(p\tau) + \frac{1}{p}j(p^2\tau) - \frac{1}{p}j(\tau)$$
from Theorem 4.6 (with $\tau$ replaced by $p\tau$), we obtain
$$p\,j_p\left(-\frac{1}{p\tau}\right) = p\,j_p(p\tau) + j(p^2\tau) - j(\tau)$$
$$= x^{-p^2} - x^{-1} + I(x),$$
where $I(x)$ is a power series in $x$ with integer coefficients.

Now from Theorem 4.9, since $12\alpha = r/2$, Theorem 4.8 gives us
$$p^{r/2}\Phi\left(-\frac{1}{p\tau}\right) = \frac{1}{\Phi(\tau)} = x^{-1} + I(x).$$

Let $\psi(\tau) = p^{r/2}\Phi(-1/(p\tau))$. Then the difference
$$p\,j_p\left(-\frac{1}{p\tau}\right) - \{\psi(\tau)\}^{p^2}$$
has a pole of order $\leq p^2 - 1$ at $x = 0$, and the Laurent expansion near $x = 0$ has integer coefficients. Hence there is an integer $b_1$ such that
$$p\,j_p\left(-\frac{1}{p\tau}\right) - \{\psi(\tau)\}^{p^2} - b_1\{\psi(\tau)\}^{p^2-1}$$
has a pole of order $\leq p^2 - 2$ at $x = 0$, and the Laurent expansion near $x = 0$ has integer coefficients. In $p^2$ steps we arrive at a function
$$f\left(-\frac{1}{p\tau}\right) = p\,j_p\left(-\frac{1}{p\tau}\right) - \{\psi(\tau)\}^{p^2} - b_1\{\psi(\tau)\}^{p^2-1} - \cdots - b_{p^2-1}\psi(\tau)$$
which is analytic at $x = 0$ and has a power series expansion with integer coefficients. Moreover, all the numbers $b_1, \ldots, b_{p^2-1}$ are integers. Replacing $\tau$ by $-1/(p\tau)$ we obtain
$$f(\tau) = p\,j_p(\tau) - \{p^{r/2}\Phi(\tau)\}^{p^2} - b_1\{p^{r/2}\Phi(\tau)\}^{p^2-1} - \cdots - b_{p^2-1}\{p^{r/2}\Phi(\tau)\}.$$

Now $f(\tau)$ is automorphic under $\Gamma_0(p)$ and is analytic in $H$ and at $\infty$, hence $f$ is a modular function of weight $0$ for $\Gamma_0(p)$ with no poles. By the valence formula, $f$ must be constant. Evaluating at $\infty$ shows $f(\tau) = 0$. Therefore $p\,j_p(\tau)$ is a monic polynomial in $p^{r/2}\Phi(\tau)$ of degree $p^2$ with integer coefficients.
