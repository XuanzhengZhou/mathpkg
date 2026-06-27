---
role: proof
locale: en
of_concept: "let-be-a-monotone-continuous--function-with-domain"
source_book: gtm025
source_chapter: "Integration Theory Continued"
source_section: "20.5"
---

Theorem (18.25) shows that $\varphi$ is absolutely continuous, since as a monotone function $\varphi$ has finite variation. With no loss of generality, we suppose that $\varphi$ is nondecreasing. Applying (20.4.i) to the function 1 on $[\alpha, \beta]$, we obtain

$$\varphi(b) - \varphi(a) = \int_{\alpha}^{\beta} dy = \int_{a}^{b} w(t) dt.$$

(1)

For every $x \in [a, b]$, the inclusion $\varphi^{-1}(\varphi([a, x])) \supset [a, x]$ holds, and hence by (20.4.i) applied to $\xi_{\varphi([a, x])}$ we have

$$\varphi(x) - \varphi(a) = \int_{\alpha}^{\beta} \xi_{\varphi([a, x])}(y) dy$$

$$= \int_{a}^{b} \xi_{\varphi([a, x])} \circ \varphi(t) w(t) dt$$

$$= \int_{a}^{b}

N-function (18.25). Consider $\varphi$ as a mapping of $[0, 1]$ onto $[0, \frac{1}{2}]$, to which (20.4) may be applied.

(a) Let $v$ be a function in $\mathfrak{L}_1([0, 1], \mathcal{M}_\lambda, \lambda)$ with the property that

(i) $$\int_{c}^{d} v d\lambda + \int_{1-d}^{1-c} v d\lambda = d - c$$

for all $[c, d] \subset [0, \frac{1}{2}]$. Prove that

(ii) $$\int_{0}^{\frac{1}{2}} f(y) dy = \int_{0}^{1} (f \circ \varphi(x)) v(x) dx$$

for all $f \in \mathfrak{L}_1([0, \frac{1}{2}], \mathcal{M}_\lambda, \lambda)$.

(b) If $v$ is any function in $\mathfrak{L}_1([0, 1], \mathcal{M}_\lambda, \lambda)$ for which (ii) holds, prove that (i) holds for $v$.

(c) Infer that the function $w$ in Theorem (20.4) is never unique if $\varphi$ fails to be monotone.

(d) Is the function $|\varphi'|$ of (20.5) the only function [a.e. of course] for which (20.5.i) holds?

Extra complications appear with more complicated mapping functions $\varphi$, as the following exercise shows.

(20.7) Exercise. Let $\psi$ be the function of period 1 on $R$ such that $\psi(t) = t$ for $0 \leq t \leq \frac{1}{2}$ and $\psi(t) = 1 - t$ for $\frac{1}{2} \leq t \leq 1$. Define the function $\varphi$ on $[0, 1]$ by the following rules:

for $2^{-1} \leq t \leq 1$, $\varphi(t) = 2^{-1}\psi(2t)$;

for $2^{-2} \leq t \leq 2^{-1}$, $\varphi(t) =

Thus Theorem (20.4) can be applied, with $g = \varphi$. Since $g'$ does not exist on $F$, no function $w$ for which (20.4.i) holds can possibly be the derivative of $g$. Find all $\mathcal{M}_1$-measurable functions on $[0, 1]$ for which (20.4.i) holds for $\varphi = g$.

(20.9) Note. There are obvious questions concerning classical transformations of integrals other than those treated in (20.4) and (20.5). For example, for a continuous mapping $\varphi$ of $R^n$ into $R^n$, the function $w$ of (20.3) is in certain cases the absolute value of the Jacobian of the transformation $\varphi$. Lack of space and time compels us to omit this interesting subject, although its main outlines are clear enough from (20.3) and the $n$-dimensional Lebesgue integral to be defined in §21.

In §15 we computed the conjugate space for each of the Banach spaces $\mathfrak{L}_p(X, \mathcal{A}, \mu)$ for $1 < p < \infty$ and arbitrary measure spaces $(X, \mathcal{A}, \mu)$, but omitted all mention of this problem for spaces $\mathfrak{L}_1(X, \mathcal{A}, \mu)$. We now address ourselves to this computation. The results and the techniques employed here are quite different from those of §15: our main tool is the Lebesgue-Radon-Nikodym theorem.

(20.10) Remarks. Let $(X, \mathcal{A}, \mu)$ be any measure space. Let $g$ be a bounded $\mathcal{A}$-measurable function on $X$ and let $L_g$ be defined on $\mathfrak{L}_1(X, \mathcal{A}, \mu)$ by the rule

(i) $L_g(f) = \int_X f \bar{g} d\mu$.

Obviously $L_g$ is linear on $\mathfrak{L}_1$ and

$$|L_g(f)| \leq \|g\|_u \|f\|_1$$

for all

(ii) $fg \in \mathfrak{L}_1$;
and
(iii) $|\int_X fg \, d\mu| \leq \|g\|_\infty \|f\|_1$.

Proof. Let $E = \{x \in X : |f(x)| > 0\}$ and $E_n = \{x \in X : |f(x)| \geq \frac{1}{n}\}$ for $n = 1, 2, \ldots$. Obviously $E = \bigcup_{n=1}^{\infty} E_n$ and $\mu(E_n) < \infty$ for all $n$. Thus (i) holds. Let $a$ be any nonnegative real number such that the set

$$A = \{x \in X : |g(x)| > a\}$$

is locally $\mu$-null. By (12.22), we have

$$\int_X |fg| \, d\mu = \int_{E'} |fg| \, d\mu + \lim_{n \to \infty} \int_{E_n \cap A} |fg| \, d\mu + \int_{E \cap A'} |fg| \, d\mu$$

$$\leq 0 + 0 + a \int_{E \cap A'} |f| \, d\mu$$

$$\leq a \int_X |f| \, d\mu = a \|f\|_1.$$

Taking the infimum over all such $a$, we obtain (ii) and (iii). $\square$
