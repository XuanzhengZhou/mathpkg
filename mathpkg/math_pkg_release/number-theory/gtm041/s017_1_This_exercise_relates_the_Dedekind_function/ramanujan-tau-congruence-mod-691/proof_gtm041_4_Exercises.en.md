---
role: proof
locale: en
of_concept: ramanujan-tau-congruence-mod-691
source_book: gtm041
source_chapter: "4"
source_section: "Exercises"
---

The congruence follows from Lehmer's formula, which is derived in Exercises 9 and 10.

**Step 1 (Exercise 9).** Using the identity
$$\left\{504 \sum_{n=0}^{\infty} \sigma_5(n)x^n\right\}^2 = \{j(\tau) - 12^3\} \sum_{n=1}^{\infty} \tau(n)x^n,$$
where $\sigma_5(0) = -1/504$ and $x = e^{2\pi i \tau}$, equate coefficients of $x^n$ to obtain
$$(504)^2 \sum_{k=0}^{n} \sigma_5(k)\sigma_5(n-k) = \tau(n+1) - 984\tau(n) + \sum_{k=1}^{n-1} c(k)\tau(n-k).$$

**Step 2 (Exercise 10).** Combine this with Exercise 10 of Chapter 6 (which relates $\sigma_5$ and $\sigma_{11}$) to obtain Lehmer's formula:
$$\frac{65520}{691} \left\{\sigma_{11}(n) - \tau(n)\right\} = \tau(n+1) + 24\tau(n) + \sum_{k=1}^{n-1} c(k)\tau(n-k).$$

Since the right-hand side is an integer (all $c(k)$ and $\tau(k)$ are integers), the left-hand side must also be an integer. Therefore $691$ divides $65520(\sigma_{11}(n) - \tau(n))$. Since $\gcd(65520, 691) = 1$ (indeed $691$ is prime and $65520 = 2^4 \cdot 3^2 \cdot 5 \cdot 7 \cdot 13$), it follows that $691 \mid (\sigma_{11}(n) - \tau(n))$, which is exactly
$$\tau(n) \equiv \sigma_{11}(n) \pmod{691}.$$

The factor $65520/691$ arises from the relationship between the Eisenstein series $E_{12}$ and the modular discriminant $\Delta$, specifically from the fact that the Fourier coefficients of $E_{12}$ involve $\sigma_{11}(n)$ and $B_{12} = -691/2730$.
