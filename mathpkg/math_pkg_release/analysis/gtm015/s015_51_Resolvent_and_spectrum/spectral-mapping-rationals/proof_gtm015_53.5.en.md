---
role: proof
locale: en
of_concept: spectral-mapping-rationals
source_book: gtm015
source_chapter: "53"
source_section: "53.5"
---

# Proof of Spectral mapping theorem for rational functions

Uniqueness: Such a $\Phi$ must extend the mapping $\varphi$ of (53.1) (by the uniqueness of $\varphi$). Suppose $f = p/q \in \mathbb{C}(t; \sigma(x))$ in reduced form. Since $q$ and $1/q$ are in $\mathbb{C}(t; \sigma(x))$, it results from $q(1/q) = (1/q)q = 1$ that $\Phi(q) = \varphi(q)$ is invertible, with inverse $\Phi(1/q)$. Then $f = p(1/q)$ yields

$$\Phi(f) = \Phi(p)\Phi(1/q) = \varphi(p)\varphi(q)^{-1},$$

which shows that $\Phi$ is just as unique as $\varphi$.

Existence: Let $f \in \mathbb{C}(t; \sigma(x))$; we are to define $\Phi(f)$. Write $f = p/q$, where $p$ and $q$ are polynomials and $q$ has no zeros in $\sigma(x)$. (Liberally, it is not assumed that $f$ is in reduced form; this simplifies some of the later algebra.) Note that $q(x) (= \varphi(q))$ is invertible in $A$. {This is obvious if $q$ is a constant. Otherwise, citing (53.3) we have $0 \notin q(\sigma(x)) = \sigma(q(x))$.} Note also that $p(x)$ commutes with $q(x)$ and with $q(x)^{-1}$. {The relation $p(x)q(x) = q(x)p(x)$ is obvious; left- and right-multiplying by $q(x)^{-1}$, we have also $q(x)^{-1}p(x) = p(x)q(x)^{-1}$.} We define

$$\Phi(f) = p(x)q(x)^{-1};$$

this is permissible because if $f = p_1/q_1$ is another such representation with $q_1$ nonvanishing on $\sigma(x)$, then $p(x)q(x)^{-1} = p_1(x)q_1(x)^{-1}$ results from $q_

singular) or $p - \mu q$ is not a constant (in which case (*) holds, showing that $(p - \mu q)(x)$ cannot be singular). We conclude that $(p - \mu q)(x)$ is singular iff $p - \mu q$ has a zero in $\sigma(x)$. Thus we have the following chain of equivalent statements: $\mu \in \sigma(f(x)); f(x) - \mu 1$ singular; $(p - \mu q)(x)$ singular; $p - \mu q$ has a zero in $\sigma(x); [p(\lambda) - \mu q(\lambda)]q(\lambda)^{-1} = 0$ for some $\lambda \in \sigma(x)$ (recall that $q$ has no zeros in $\sigma(x)); f(\lambda) - \mu = 0$ for some $\lambda \in \sigma(x); \mu \in f(\sigma(x))$.
