---
role: proof
locale: en
of_concept: measurable-function-2
source_book: gtm095
source_chapter: "II"
source_section: "4"
---

# Proof of Lemma (Chain Rule for Radon--Nikodym Derivatives)

**Lemma.** Let $(\Omega, \mathcal{F})$ be a measurable space.

(a) Let $\mu$ and $\lambda$ be $\sigma$-finite measures, $\mu \ll \lambda$, and $f = f(\omega)$ an $\mathcal{F}$-measurable function. Then

$$\int_{\Omega} f \, d\mu = \int_{\Omega} f \, \frac{d\mu}{d\lambda} \, d\lambda$$

(in the sense that if either integral exists, the other exists and they are equal).

(b) If $\nu$ is a signed measure and $\mu, \lambda$ are $\sigma$-finite measures, $\nu \ll \mu$, $\mu \ll \lambda$, then

$$\frac{d\nu}{d\lambda} = \frac{d\nu}{d\mu} \cdot \frac{d\mu}{d\lambda} \quad (\lambda\text{-a.s.})$$

and

$$\frac{d\nu}{d\mu} = \frac{d\nu}{d\lambda} \Bigg/ \frac{d\mu}{d\lambda} \quad (\mu\text{-a.s.}).$$

*Proof.* (a) Since

$$\mu(A) = \int_A \left( \frac{d\mu}{d\lambda} \right) d\lambda, \quad A \in \mathcal{F},$$

the equality $\int_{\Omega} f \, d\mu = \int_{\Omega} f \, \frac{d\mu}{d\lambda} \, d\lambda$ is evidently satisfied for simple functions $f = \sum f_i I_{A_i}$. The general case follows from the representation $f = f^+ - f^-$ and the monotone convergence theorem (cf. the proof of (39) in Sect. 6).

(b) From (a) with $f = d\nu/d\mu$ we obtain

$$\nu(A) = \int_A \left( \frac{d\nu}{d\mu} \right) d\mu = \int_A \left( \frac{d\nu}{d\mu} \right) \left( \frac{d\mu}{d\lambda} \right) d\lambda.$$

Then $\nu \ll \lambda$ and therefore

$$\nu(A) = \int_A \frac{d\nu}{d\lambda} \, d\lambda.$$

Since $A$ is arbitrary, the integrands must coincide $\lambda$-a.s., whence

$$\frac{d\nu}{d\lambda} = \frac{d\nu}{d\mu} \cdot \frac{d\mu}{d\lambda} \quad (\lambda\text{-a.s.}).$$

The second identity follows by division, since $d\mu/d\lambda \neq 0$ $\mu$-a.s.
