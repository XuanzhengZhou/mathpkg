---
role: proof
locale: en
of_concept: polynomial-homomorphism
source_book: gtm015
source_chapter: "53"
source_section: "53.1"
---

# Proof of Polynomial homomorphism

(53.1) Lemma. Let $x \in A$. There exists a unique algebra homomorphism $\varphi: \mathbb{C}[t] \rightarrow A$ such that $\varphi(1) = 1$ and $\varphi(t) = x$.

Notation: If $p \in \mathbb{C}[t]$ we define $p(x) = \varphi(f)$; thus if $p = \sum_{k=0}^{n} a_k t^k$, then $p(x) = \sum_{k=0}^{n} a_k x^k$.

The range of $\varphi$ is the smallest subalgebra of $A$ containing $x$ and 1, i.e., it is the linear span of the set $\{1, x, x^2, x^3, \ldots\}$.

Proof. Since the set $\{1, t, t^2, t^3, \ldots\}$ is a basis for $\mathbb{C}[t]$ as a complex vector space, there exists a unique linear mapping $\varphi: \mathbb{C}[t] \rightarrow A$ such that $\varphi(t^n) = x^n$ for $n = 0, 1, 2, 3, \ldots$ (with the conventions that $t^0 = 1$ and $x^0 = 1$). The fact that $\varphi$ preserves products follows from the bilinearity of the mapping

$$(p, q) \mapsto \varphi(pq) \quad (p, q \in \mathbb{C}[t])$$

and the fact that

$$\varphi(t^m t^n) = \varphi(t^{m+n}) = x^{m+n} = x^m x^n = \varphi(t^m

If $p$ is a constant, say $p = a_0 \in \mathbb{C}$, then

$$\sigma(p(x)) = \sigma(a_01) = \{a_0\} = p(\sigma(x)).$$

{It is only in showing the last equality that the nonemptiness of $\sigma(x)$ is used.}

Assume $p$ nonconstant, say $\deg p = n \geq 1$. Let $\mu \in \mathbb{C}$. Factoring $p - \mu$ into linear factors, say

$$p - \mu = a_0(t - \lambda_1) \cdots (t - \lambda_n),$$

where $a_0 \neq 0$, we have

$$p(x) - \mu1 = a_0(x - \lambda_11) \cdots (x - \lambda_n1);$$

since the factors on the right side of (*) commute with each other, it is clear that $p(x) - \mu1$ is invertible iff $x - \lambda_k1$ is invertible for all $k$. In other words, $p(x) - \mu1$ is singular iff $x - \lambda_k1$ is singular for some $k$, thus the following statements are equivalent: $\mu \in \sigma(p(x)); \lambda_k \in \sigma(x)$ for some $k; \sigma(x)$ contains one of the zeros of $p - \mu$; the function $\lambda \mapsto p(\lambda) - \mu$ vanishes at some point of $\sigma(x); \mu \in p(\sigma(x))$.

The next order of business is to generalize from polynomial forms to rational forms. We write $\mathbb{C}(t)$ for the field of fractions of the integral domain $\mathbb{C}[t]$; thus $\mathbb{C}(t)$ is the set of all rational forms $f = p/q$, where $p, q \in \mathbb{C}[t]$ and $q \neq 0$. The rational form $f$ is in reduced form if (as can be arranged) $p$ and $q$ are relatively prime in $\mathbb{C}[t]$, i.e., when they possess no nonconstant common factor. When $f$ is itself a polynomial, the polyn

Proof. Uniqueness: Such a $\Phi$ must extend the mapping $\varphi$ of (53.1) (by the uniqueness of $\varphi$). Suppose $f = p/q \in \mathbb{C}(t; \sigma(x))$ in reduced form. Since $q$ and $1/q$ are in $\mathbb{C}(t; \sigma(x))$, it results from $q(1/q) = (1/q)q = 1$ that $\Phi(q) = \varphi(q)$ is invertible, with inverse $\Phi(1/q)$. Then $f = p(1/q)$ yields

$$\Phi(f) = \Phi(p)\Phi(1/q) = \varphi(p)\varphi(q)^{-1},$$

which shows that $\Phi$ is just as unique as $\varphi$.

Existence: Let $f \in \mathbb{C}(t; \sigma(x))$; we are to define $\Phi(f)$. Write $f = p/q$, where $p$ and $q$ are polynomials and $q$ has no zeros in $\sigma(x)$. (Liberally, it is not assumed that $f$ is in reduced form; this simplifies some of the later algebra.) Note that $q(x) (= \varphi(q))$ is invertible in $A$. {This is obvious if $q$ is a constant. Otherwise, citing
