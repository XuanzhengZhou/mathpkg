---
role: proof
locale: en
of_concept: stirling-formula
source_book: gtm095
source_chapter: "1"
source_section: "5"
---

# Proof of Stirling's Formula

**Statement (Formula (6)).** For all $n \geq 1$,
$$n! = \sqrt{2\pi n}\left(\frac{n}{e}\right)^n \exp\left(\frac{\theta_n}{12n}\right), \quad 0 < \theta_n < 1.$$

In asymptotic notation, as $n \to \infty$:
$$n! \sim \sqrt{2\pi n}\, e^{-n} n^n,$$
meaning $n! \big/ \left(\sqrt{2\pi n}\, e^{-n} n^n\right) \to 1$ as $n \to \infty$.

**Proof.** The proof is not given in the text. Shiryaev remarks: *"whose proof can be found in most textbooks on mathematical analysis"* (GTM 095, p. 18).

The standard proof proceeds via Wallis's product or by approximating $\log n! = \sum_{k=1}^n \log k$ using the Euler–Maclaurin summation formula. The sharper form with the exponential factor $\exp(\theta_n / 12n)$, $0 < \theta_n < 1$, is due to Robbins (1955) and is known as the Robbins bounds:
$$\sqrt{2\pi n}\left(\frac{n}{e}\right)^n e^{\frac{1}{12n+1}} < n! < \sqrt{2\pi n}\left(\frac{n}{e}\right)^n e^{\frac{1}{12n}}.$$

**Application in the text.** Stirling's formula is used to study the asymptotic behavior of binomial probabilities in the symmetric random walk. Specifically, for $2n$ steps:
$$C_{2n}^n = \frac{(2n)!}{(n!)^2} \sim 2^{2n} \cdot \frac{1}{\sqrt{\pi n}},$$
and therefore the probability of being at the origin after $2n$ steps is
$$\mathrm{P}(A_0) = C_{2n}^n \cdot 2^{-2n} \sim \frac{1}{\sqrt{\pi n}}.$$
