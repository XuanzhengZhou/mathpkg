---
role: proof
locale: en
of_concept: distance-in-variation-radon-nikodym
source_book: gtm095
source_chapter: "3"
source_section: "5"
---

# Proof of Lemma 2 (Distance in Variation via Radon–Nikodym Derivatives)

Let $Q$ be a $\sigma$-finite measure such that $P \ll Q$ and $\tilde{P} \ll Q$. Let $z = dP/dQ$ and $\tilde{z} = d\tilde{P}/dQ$ be the Radon–Nikodym derivatives of $P$ and $\tilde{P}$ with respect to $Q$. Then

$$\|P - \tilde{P}\| = E_Q|z - \tilde{z}|.$$

Moreover, if $Q = (P + \tilde{P})/2$, then

$$\|P - \tilde{P}\| = E_Q|z - \tilde{z}| = 2E_Q|1 - z| = 2E_Q|1 - \tilde{z}|.$$

*Proof.* For all $\mathcal{F}$-measurable functions $\psi = \psi(\omega)$ with $|\psi(\omega)| \leq 1$, we see from the definitions of $z$ and $\tilde{z}$ that

$$|E\psi - \tilde{E}\psi| = |E_Q \psi(z - \tilde{z})| \leq E_Q |\psi| |z - \tilde{z}| \leq E_Q |z - \tilde{z}|.$$

Therefore,

$$\|P - \tilde{P}\| \leq E_Q |z - \tilde{z}|.$$

However, for the particular function

$$\psi = \operatorname{sign}(\tilde{z} - z) = \begin{cases} 1, & \tilde{z} \geq z, \\ -1, & \tilde{z} < z, \end{cases}$$

we have

$$|E\psi - \tilde{E}\psi| = |E_Q \psi(z - \tilde{z})| = E_Q |z - \tilde{z}|.$$

Since the distance in variation is the supremum of $|E\psi - \tilde{E}\psi|$ over all such $\psi$, we obtain

$$E_Q |z - \tilde{z}| = |E\psi - \tilde{E}\psi| \leq \|P - \tilde{P}\|.$$

Combining the two inequalities yields the required identity $\|P - \tilde{P}\| = E_Q|z - \tilde{z}|$.

For the second part, when $Q = (P + \tilde{P})/2$, we observe that $z + \tilde{z} = 2$ (because $dP/dQ + d\tilde{P}/dQ = d(P + \tilde{P})/dQ = 2$). Hence

$$E_Q |z - \tilde{z}| = E_Q |z - (2 - z)| = E_Q |2z - 2| = 2E_Q |1 - z| = 2E_Q |1 - \tilde{z}|,$$

which gives the pair of alternative formulas.

$\square$

**Remark.** This lemma is fundamental in the theory of hypothesis testing. For the problem of discriminating between two simple hypotheses $H: P$ and $\tilde{H}: \tilde{P}$ based on an observation $\omega$, the optimal Bayes risk (with equal prior probabilities) equals

$$\frac{1}{2}\left(1 - \frac{1}{2}\|P - \tilde{P}\|\right).$$

Thus the distance in variation directly controls the achievable performance of any statistical test. The formula via Radon–Nikodym derivatives also connects variation distance to likelihood ratios and the Neyman–Pearson lemma.
