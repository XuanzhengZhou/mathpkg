---
role: proof
locale: en
of_concept: local-maximum-modulus-implies-maximum-modulus
source_book: gtm035
source_chapter: "11"
source_section: "11.9"
---
# Proof that Local Maximum Modulus Implies Maximum Modulus Algebra

**Theorem 11.9.** Let $\mathfrak{A}$ be a uniform algebra on a compact space $\mathcal{M}$ and let $f \in \mathfrak{A}$. Let $\Omega$ be a bounded open set in $\mathbb{C}$ such that $f^{-1}(\Omega) \neq \emptyset$ and, for every $x \in f^{-1}(\Omega)$ and every closed disk $\Delta \subset \Omega$ centered at $f(x)$, we have

$$|g(x)| \leq \max_{y \in f^{-1}(\partial \Delta)} |g(y)|$$

for all $g \in \mathfrak{A}$. Then, letting $A = \mathfrak{A}|_{f^{-1}(\Omega)}$, the quadruple $(A, f^{-1}(\Omega), \Omega, f)$ is a maximum modulus algebra.

*Proof.* First we verify that $f$ maps $f^{-1}(\Omega)$ onto $\Omega$. Suppose not. Then there exists $\lambda_0 \in \Omega \setminus f(f^{-1}(\Omega))$. Let $Y = f^{-1}(\Omega)$ and choose $x^0 \in f^{-1}(\Omega)$ with $|f(x^0) - \lambda_0| = \operatorname{dist}(\lambda_0, f(Y))$. Then $g \equiv 1/(f - \lambda_0) \in \mathfrak{A}$ and

$$|g(x^0)| = \frac{1}{|f(x^0) - \lambda_0|} > \sup_{y \in Y} \frac{1}{|f(y) - \lambda_0|} = \|g\|_Y,$$

a contradiction to the local maximum modulus principle. Thus $f$ maps $f^{-1}(\Omega)$ onto $\Omega$.

Now fix a closed disk $\Delta \subseteq \Omega$ with center $\lambda_0$. Choose a point $x^0 \in f^{-1}(\lambda_0)$. Let $\mu_0$ be a representing measure for $x^0$ on $\partial(f^{-1}(\Omega))$ (which exists by the local maximum modulus assumption and the Riesz representation theorem). For each $\lambda \in \Delta$, define a functional $m_\lambda$ on $\mathfrak{A}$ by

$$m_\lambda(h) = \int_{\partial(f^{-1}(\Omega))} \frac{f - \lambda_0}{f - \lambda} \, h \, d\mu_0, \quad h \in \mathfrak{A}.$$

Then $m_{\lambda_0}(h) = h(x^0)$ for all $h \in \mathfrak{A}$.

Fix $\lambda \in \Delta$ and denote by $I_\lambda$ the closed ideal in $\mathfrak{A}$ which is the closure of

$$(f - \lambda)\mathfrak{A} = \{h \in \mathfrak{A} : \exists g \in \mathfrak{A} \text{ with } h = (f - \lambda)g\}.$$

Form the quotient algebra $\mathfrak{A}/I_\lambda$ and write $\|[h]\|_\lambda$ for the quotient norm of the coset $[h]$ in $\mathfrak{A}/I_\lambda$.

Now $\mathfrak{A}/I_\lambda$ is a commutative Banach algebra. Each point of $f^{-1}(\lambda)$ induces a homomorphism of $\mathfrak{A}/I_\lambda$ into $\mathbb{C}$. Conversely, each such homomorphism arises in this way. Hence the maximal ideal space of $\mathfrak{A}/I_\lambda$ may be identified with $f^{-1}(\lambda)$.

By the spectral radius formula,

$$\lim_{n \to \infty} \|[g^n]\|_\lambda^{1/n}$$

exists and equals $\max_{x \in f^{-1}(\lambda)} |g(x)|$.

Using the representation of $m_\lambda$ and standard estimates, one obtains

$$\log |g(x^0)| \leq \frac{1}{2\pi} \int_{\partial \Delta} \frac{1}{n} \log \big(C \|[g^n]\|_\lambda\big) \, d\theta.$$

Letting $n \to \infty$ and applying Fatou's Lemma,

$$\log |g(x^0)| \leq \frac{1}{2\pi} \int_{\partial \Delta} \log\left[\max_{x \in f^{-1}(\lambda)} |g(x)|\right] d\theta.$$

Since the right-hand side is bounded by $\log[\max_{f^{-1}(\partial \Delta)} |g|]$, we obtain

$$\log |g(x^0)| \leq \log\left[\max_{f^{-1}(\partial \Delta)} |g|\right],$$

and hence

$$|g(x^0)| \leq \max_{f^{-1}(\partial \Delta)} |g|.$$

This holds for every $g \in \mathfrak{A}$, every $x^0 \in f^{-1}(\lambda_0)$, and every closed disk $\Delta \subset \Omega$ centered at $\lambda_0$. Therefore $(A, f^{-1}(\Omega), \Omega, f)$ is a maximum modulus algebra. $\square$
