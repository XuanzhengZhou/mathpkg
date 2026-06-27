---
role: proof
locale: en
of_concept: liouvilles-approximation-theorem
source_book: gtm041
source_chapter: "7"
source_section: "7.3"
---

Since $\theta$ is algebraic of degree $n$, $\theta$ is a zero of some polynomial $f(x)$ of degree $n$ with integer coefficients, say

$$f(x) = \sum_{r=0}^{n} a_r x^r,$$

where $f(x)$ is irreducible over the rational field. Since $f(x)$ is irreducible it has no rational roots so $f(h/k) \neq 0$ for every rational $h/k$.

Now we use the mean value theorem of differential calculus to write

$$f\left(\frac{h}{k}\right) = f\left(\frac{h}{k}\right) - f(\theta) = f'(\xi)\left(\frac{h}{k} - \theta\right),$$

where $\xi$ lies between $\theta$ and $h/k$. We will deduce the inequality from this by getting an upper bound for $|f'(\xi)|$ and a lower bound for $|f(h/k)|$. We have

$$f\left(\frac{h}{k}\right) = \sum_{r=0}^{n} a_r \left(\frac{h}{k}\right)^r = \frac{N}{k^n}$$

where $N$ is a nonzero integer. Therefore

$$\left| f\left(\frac{h}{k}\right) \right| \geq \frac{1}{k^n},$$

which is the required lower bound. To get an upper bound for $|f'(\xi)|$ we let

$$d = \left| \theta - \frac{h}{k} \right|.$$

If $d > 1$ then the inequality holds with $C(\theta) = 1$, so we can assume that $d < 1$.
