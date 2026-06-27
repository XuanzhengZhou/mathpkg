---
role: proof
locale: en
of_concept: integral-representation-gibbs-extremes
source_book: gtm040
source_chapter: "12"
source_section: "4"
---

**Proof.** We know from Chapter 10 that $B_e$ is in one-to-one correspondence with the class $\mathcal{H}_e$ of minimal normalized regular functions, while Theorem 12-25 gives a bijection between $\mathcal{H}_e$ and $\mathcal{E}_V$. Hence there is a one-to-one correspondence $x \leftrightarrow \mu^x$ between $B_e$ and $\mathcal{E}_V$.

For $\mu \in \mathcal{G}_V$, apply Theorem 10-41 to $\rho(\mu) \in \mathcal{H}$ (the regular function corresponding to $\mu$ via Theorem 12-25), and use Lemma 12-24, to get

$$
\frac{\mu([\kappa^0, \ldots, \kappa^m])}{\nu([\kappa^0, \ldots, \kappa^m])}
= \int_{x \in B_e} \frac{\mu^x([\kappa^0, \ldots, \kappa^m])}{\nu([\kappa^0, \ldots, \kappa^m])} \, d\lambda^{\rho(\mu)}(x),
$$

where $\lambda^h$ is harmonic measure for the $h$-process. A routine computation using the explicit form of the Martin kernel, derived in the proof of Theorem 12-27, shows that

$$
\lambda^{\rho(\mu)}(E) = \mu\left(\left\{ \omega \mid t\text{-}\lim_{n \to \infty} \nu^{\kappa^n(\omega)} = \mu^x \text{ for some } x \in E \right\}\right)
$$

$$
= \mu\left(\left\{ \omega \mid t\text{-}\lim_{n \to \infty} \mu^{\kappa^n(\omega)} = \mu^x \text{ for some } x \in E \right\}\right).
$$

The second equality follows because the local characteristics of $\nu$ and $\mu$ agree for configurations that differ only on finitely many coordinates, and the tail limit is insensitive to such finite modifications.
