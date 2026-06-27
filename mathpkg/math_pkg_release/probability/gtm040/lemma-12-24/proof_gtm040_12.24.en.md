---
role: proof
locale: en
of_concept: lemma-12-24
source_book: gtm040
source_chapter: "12"
source_section: "24"
---

**Proof:** The left hand expression may be rewritten as

$$\frac{\mu([\kappa^m, \ldots, \kappa^n])}{\nu([\kappa^m, \ldots, \kappa^n])} \frac{\mu_{A(m-1)}^{A(n)}(\iota)}{\nu_{A

PROOF: Given $\mu \in \mathcal{G}_V$, define $h$ according to the first equation in the theorem. By Lemma 12-24,

$$\sum_{\kappa^{n+1}} P_{(n,\kappa^n)(n+1,\kappa^{n+1})} h_{(n+1,\kappa^{n+1})} = \sum_{\kappa^{n+1}} \frac{\nu([\kappa^n, \kappa^{n+1}])}{\nu([\kappa^n])} \frac{\mu([\kappa^n, \kappa^{n+1}])}{\nu([\kappa^n, \kappa^{n+1}])}$$

$$= \sum_{\kappa^{n+1}} \frac{\mu([\kappa^n, \kappa^{n+1}])}{\nu([\kappa^n])}$$

$$= \frac{\mu([\kappa^n])}{\nu([\kappa^n])} = h_{(n,\kappa^n)},$$

so $h$ is $P$-regular. Clearly, $h$ is also non-negative and normalized. Conversely, let $h$ be any non-negative normalized $P$-regular function. We claim that the second equation of the theorem prescribes cylinder probabilities for a unique measure $\mu \in \mathcal{G}_V$ determined by $h$. Note first that $h$ must be strictly positive. To see this, write

$$\sum_{\kappa^{n+1}} \nu([\kappa^{n+1}]) h_{(n+1,\kappa^{n+1})} = \pi P^{n+1} h = 1,$$

and

$$h_{(n,\kappa^n)} = (Ph)_{(n,\kappa^n)} = \sum_{\kappa^{n+1}} \frac{\nu([\kappa^n, \kappa^{n+1}])}{\nu([\kappa^n])} h_{(n+1,\kappa^{n+1})}.$$

The first equation above implies that $h_{(n+1,\kappa^n)} > 0$ for some $\

enough that $\Lambda \subset \Lambda(n)$. Let $\iota = \{i_t; t \in T\} = (\kappa^0, \kappa^1, \ldots) \in \Omega$. Introduce the sets

$$[\iota_A] = \{\omega \mid \omega_t = i_t \text{ for all } t \in \Lambda\},$$
$$[\iota_{\Lambda-A}] = \{\omega \mid \omega_t = i_t \text{ for all } t \in \Lambda - A\},$$
$$[\psi] = \{\omega \mid \omega_t = \psi_t \text{ for all } t \in \Lambda(n-1) - \Lambda\} \text{ where } \psi \in S^{\Lambda(n-1)-\Lambda}.$$

Then by construction,

$$\mu([\iota_A]) = \sum_\psi \sum_{\kappa^n} \nu([\iota_A] \cap [\psi] \cap [\kappa^n]) h_{(n,\kappa^n)}$$

and

$$\mu([\iota_{\Lambda-A}]) = \sum_\psi \sum_{\kappa^n} \nu([\iota_{\Lambda-A}] \cap [\psi] \cap [\kappa^n]) h_{(n,\kappa^n)},$$

where $\psi$ is summed over $S^{\Lambda(n-1)-\Lambda}$, $\kappa^n$ over $S^{K(n)}$. If $\iota^{\psi,\kappa^n}$ denotes the modification of $\iota$ obtained by replacing its values on $\Lambda(n-1)-\Lambda$ with $\psi$, and its values on $K(n)$ with $\kappa^n$, then $\nu_A^{\Lambda(n)}(\iota^{\psi,\kappa^n}) = \nu_A^{\bar{A}}(\iota)$ for all $\psi$ and $\kappa^n$, since $\nu \in \mathcal{G}_V$. Thus

$$\mu([\iota_A]) = \sum_\psi \sum_{\kappa^n} \nu_A^{\Lambda(n)}(\iota^{\psi,\kappa^n}) \nu([\iota_{\Lambda-A}] \cap

for all $m \geq 0$ and all configurations $(\kappa^0, \ldots, \kappa^m)$ on $S^{\Lambda(m)}$.

Theorem 12-27:

$$\nu \left( \left\{ \omega \mid t - \lim_{n \to \infty} \nu^{\kappa^n(\omega)} \in \mathcal{E}_V \right\} \right) = 1,$$

where $\kappa^n(\omega)$ is the configuration of $\omega$ restricted to $K(n)$. In particular, $\mathcal{E}_V \neq \emptyset$ whenever $\mathcal{G}_V \neq \emptyset$.

Proof: Let $B_e$ comprise the extreme points of the Martin boundary for $P$ started with $\pi$, and let $\lambda$ denote harmonic measure. Theorem 10-41 applied to the constant regular function $h = 1$ shows that $\Pr_n[y_v \in B_e] = \lambda(B_e) = 1$. Since $\{y_n\}$ visits each state $(m, \kappa^m)$ at most once, the Martin kernel is given by

$$K((m, \kappa^m), (n, \kappa^n)) = P^{(n-m)}_{(m, \kappa^m)(n, \kappa^n)} / \sum_{\kappa^0} \pi(\kappa^0) P_{(0, \kappa^0)(n, \kappa^n)}, \quad n \geq m,$$

(= 0 otherwise). Thus $y_v(\omega) \in B_e$ means that

$$K((m, \kappa^m), x) = \lim_{n \to \infty} \frac{\nu([\kappa^m, \kappa^n(\omega)])}{\nu([\kappa^m])\nu([\kappa^n(\omega)])}$$

exists for every $(m, \kappa^m)$, and is a minimal regular function of $(m, \kappa^m)$. By the last theorem, $K(\cdot, x)$ is minimal regular if and only if $\nu([\kappa^0, \ldots, \k

and

$$\lambda^\mu(E) = \mu \left( \left\{ \omega \mid t - \lim_{n \to \infty} \mu^{\kappa^n(\omega)} = \mu^x \text{ for some } x \in E \right\} \right),$$

$E$ Borel in $B_e$.

Proof: We know from Chapter 10 that $B_e$ is in one-to-one correspondence with the class $\mathcal{H}_e$ of minimal normalized regular functions, while Theorem 12-25 gives a bijection between $\mathcal{H}_e$ and $\mathcal{E}_V$. Hence there is a one-to-one correspondence $x \leftrightarrow \mu^x$ between $B_e$ and $\mathcal{E}_V$. For $\mu \in \mathcal{G}_V$, apply Theorem 10-41 to $\rho(\mu) \in \mathcal{H}$, and use Lemma 12-24, to get

$$\frac{\mu([\kappa^0, \ldots, \kappa^m])}{\nu([\kappa^0, \ldots, \kappa^m])} = \int_{x \in B_e} \frac{\mu^x([\kappa^0, \ldots, \kappa^m])}{\nu([\kappa^0, \ldots, \kappa^m])} d\lambda^{\rho(\mu)}(x),$$

where $\lambda^h$ is harmonic measure for the $h$-process. A routine computation using the explicit form of the Martin kernel, derived in the proof of the previous theorem, shows that

$$\lambda^{\rho(\mu)}(E) = \mu \left( \left\{ \omega \mid t - \lim_{n \to \infty} \nu^{\kappa^n(\omega)} = \mu^x \text{ for some } x \in E \right\} \right)$$

$$= \mu \left( \left\{ \omega \mid t - \lim_{n \to \infty} \mu^{\kappa^n(\omega)} = \mu^x \text{ for some } x \in E \right\} \right),$$

(The

Theorem 12-30: If $S$ is finite, then $\mathcal{G}_V \neq \varnothing$. Moreover, the limits

$$\mu^+([\kappa^0, \ldots, \kappa^m]) = \lim_{n \to \infty} \max_{\kappa^n \in S^{K(n)}} \mu^{\kappa^n}([\kappa^0, \ldots, \kappa^m])$$

and

$$\mu^-([\kappa^0, \ldots, \kappa^m]) = \lim_{n \to \infty} \min_{\kappa^n \in S^{K(n)}} \mu^{\kappa^n}([\kappa^0, \ldots, \kappa^m])$$

exist for all $m \geq 0$, $(\kappa^0, \ldots, \kappa^m) \in S^{\Lambda(m)}$, and there is phase multiplicity for $V$ if and only if

$$\mu^+([\kappa^0, \ldots, \kappa^m]) \neq \mu^-([\kappa^0, \ldots, \kappa^m])$$ for some $m$ and $(\kappa^0, \ldots, \kappa^m)$.

(Recall that $\mu^{\kappa^n}([\kappa^0, \ldots, \kappa^m])$ is a certain characteristic which is completely and uniquely determined by $V$.)

To prove the theorem, we first need the following lemma.

Lemma 12-31: For given $\mu \in \mathcal{G}_V, m > 0$ and fixed $(\kappa^0, \ldots, \kappa^m) \in S^{\Lambda(m)}$, abbreviate

$$\mu^+_n = \max_{\kappa^n \in S^{K(n)}} \mu^{\kappa^n}([\kappa^0, \ldots, \kappa^m]),$$

$$\mu^-_n = \min_{\kappa^n \in S^{K(n)}} \mu^{\kappa^n}([\

This shows that $\mu_n^-$ is increasing with $n$; a similar estimate proves that $\mu_n^+$ is decreasing.

**Proof of Theorem 12-30:** The limits $\mu^+$ and $\mu^-$ are well-defined by the monotonicity established in the lemma. We now show that for any given configuration $(\kappa^0, \ldots, \kappa^m)$ on $\Lambda(m)$, there is a random field $\mu \in \mathcal{G}_V$ such that $\mu([\kappa^0, \ldots, \kappa^m]) = \mu^-([\kappa^0, \ldots, \kappa^m])$. Let $\kappa^n$ denote the configuration on $K(n)$ for which the minimum value $\mu_n^-$ is attained, and define measures $\mu_n$, $n \geq 1$, on $\Omega$ by

$$\mu_n: \begin{cases} \mu_n([\iota]) = \mu^{\kappa^n}([\iota_\Lambda]) & \text{whenever } \Lambda \subset \Lambda(n - 1) \\ \mu_n([\kappa^n]) = 1 \\ \mu_n(\{\omega : x_t = 0\}) = 1 & \text{whenever } t \notin \Lambda(n) \end{cases}$$

(The notation $[\iota_\Lambda]$ was introduced in the proof of Theorem 12-25.) These specifications are clearly consistent, so each $\mu_n$ is well-defined. Now by the finiteness of $S$, we can use a diagonal argument (like the one in Proposition 1-63) to choose a subsequence $\{\mu_{n'}\}$ such that $\mu_{n'}([\iota_\Lambda]) \rightarrow \mu([\iota_\Lambda])$ for all possible configurations on every finite $A \subset T$. By the extension theorem, these cylinder limits give rise to a unique $\mu$ on $\Omega$. Now observe that
