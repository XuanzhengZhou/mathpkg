---
role: proof
locale: en
of_concept: formal-logarithm-derivative-lemma
source_book: gtm059
source_chapter: "Lubin-Tate Theory"
source_section: "1.5"
---

*Proof.* (i) Differentiating the additivity relation

$$\lambda_d(X +_A Y) = \lambda_d(X) + \lambda_d(Y)$$

with respect to $X$ and then setting $Y = 0$, we obtain

$$\lambda_d'(X +_A Y) \cdot F_1(X, Y) = \lambda_d'(X),$$

where $F_1(X, Y)$ denotes the partial derivative of $X +_A Y$ with respect to $X$. Setting $Y = 0$ yields

$$\lambda_d'(X) \cdot F_1(X, 0) = \lambda_d'(X),$$

so $F_1(X, 0) = 1$ and $\lambda_d'(0) = 1$. A power series argument then shows $\lambda_d'(X)$ is a power series with constant term $1$ and coefficients in $\mathfrak{o}_d$, giving the first assertion.

(ii) It suffices to prove the result for the basic Lubin-Tate group whose Frobenius power series is given by

$$[\pi](X) = \pi X + X^q.$$

The power series $[\pi^n](X)$ lies in the module

$$\mathfrak{o}[X] \pi^n X^{p^j}$$

with $j \geq 0$, $k \geq 1$, and $j + \log_q k \geq n$.

We prove this by induction on $n$. It is obvious for $n = 1$. Assume it for $n$. Let

$$[\pi^n](X) = f_n(X) = \sum_{k=0}^{\infty} \pi^{n_k} X^k.$$

Then

$$[\pi^{n+1}](X) = [\pi](f_n(X)) = \pi f_n(X) + f_n(X)^q.$$

It is immediate that $\pi f_n(X)$ satisfies the induction hypothesis with respect to $n+1$. For the term $f_n(X)^q$, the cross terms have binomial-type coefficients divisible by $\pi$ (since $q$ is a power of $p$), satisfying the integrality condition on the coefficients. The degree of the expression is increased by a factor of $q$, and the desired inequality on the exponent of $\pi$ is also satisfied. This proves (ii).

(iii) This follows directly from (ii) by observing the expansion explicitly.

**Remark.** In the simplest case of the ordinary logarithm, $\log(1+X) = X - X^2/2 + X^3/3 - \cdots$. If $p=2$, the term $-X^2/2$ causes trouble. If $p=3$, the term $X^3/3$ is the first that might cause trouble, but the assumption $\operatorname{ord}_\pi x \geq 1$ ensures that (iii) holds. For larger $p$, convergence only improves.
