---
role: proof
locale: en
of_concept: reciprocity-gauss-sums-totally-real
source_book: gtm077
source_chapter: "VIII"
source_section: "56"
---

# Proof of Theorems 160-161: Reciprocity between Gauss Sums in Totally Real Fields

Let $k$ be a totally real algebraic number field of degree $n$. The proof proceeds by applying the theta function transformation formula (Theorem 159) together with Lemma (a) to deduce the reciprocity relation for Gauss sums.

**Step 1: Setting up the theta function with parameter $\omega$.**

From Theorem 159, we have the transformation formula

$$\theta(t, z; \mathfrak{a}) = \frac{1}{N(\mathfrak{a})|\sqrt{d}| \sqrt{t_1 \cdots t_n}} \sum_{\lambda \in 1/\mathfrak{a}\mathfrak{b}} \exp \left\{ -\pi \sum_{p=1}^{n} \frac{\lambda^{(p)^2}}{t_p} - 2\pi i \sum_{p=1}^{n} \lambda^{(p)} z_p \right\}. \tag{180}$$

For the application to Gauss sums, we set $z = 0$ and replace $t_p$ by a complex parameter incorporating the Gauss sum variable $\omega$. Specifically, we consider the theta function

$$\theta(x - 2i\omega; 1) = \theta(t, 0; 1) \quad \text{with} \quad t_p = x - 2i\omega^{(p)}$$

where $x > 0$ is a positive real parameter and $\omega \neq 0$ is a totally nonzero number in $k$ (so all $\omega^{(p)} \neq 0$).

**Step 2: Decomposition via residue classes.**

The sum over $\mu \in \mathfrak{a}$ in the theta function can be decomposed according to residue classes modulo an auxiliary ideal. Grouping the terms by residue class, we obtain

$$\theta(x - 2i\omega; 1) = \sum_{\rho \bmod \mathfrak{a}} e^{2\pi i S(\rho^2\omega)} \; \theta(x, \rho; \mathfrak{a})$$

where the inner sum is again a theta-series over the sublattice.

**Step 3: Applying Lemma (a) to determine the limit as $x \to 0$.**

By Lemma (a), we know the asymptotic behavior:

$$\lim_{x \to 0} x^{n/2} \; \theta(x - 2i\omega; 1) = \frac{C(\omega)}{N(\mathfrak{a})|\sqrt{d}|},$$

where $C(\omega)$ is the Gauss sum defined in §54:

$$C(\omega) = \sum_{\rho \bmod \mathfrak{a}} e^{2\pi i S(\rho^2\omega)}.$$

**Step 4: Analyzing the right side of (180) at $x = 0$.**

We apply the transformation formula (180) to the same theta function. Set

$$\frac{1}{t_p} = \frac{i}{2\omega^{(p)}} + \tau_p, \quad \text{where} \quad \tau_p = \frac{-ix}{2\omega^{(p)}(x - 2i\omega^{(p)})}.$$

The real part of $1/\tau_p$ is then

$$\Re\left(\frac{1}{\tau_p}\right) = \frac{4\omega^{(p)^2}}{x},$$

which grows beyond all bounds as $x \to 0$ (since $x \to 0^+$ while $\omega^{(p)} \neq 0$). Thus the hypothesis of Lemma (a) is satisfied for the dual sum.

Introduce an integral auxiliary ideal $\mathfrak{c}$ such that $\mathfrak{c}\mathfrak{d}$ is a principal ideal, $\mathfrak{c}\mathfrak{d} = \delta$, and $(\mathfrak{c}, 2\mathfrak{b}) = 1$. The numbers of $1/\mathfrak{d}$ are then of the form $\mu/\delta$ where $\mu$ runs through all numbers in $\mathfrak{c}$. After this substitution, the dual theta function reads

$$\theta\left(\frac{1}{t}; \frac{1}{\mathfrak{d}}\right) = \sum_{\mu \in \mathfrak{c}} \exp\left\{ -\pi \sum_{p=1}^{n} \left(\tau_p + \frac{i}{2\omega^{(p)}}\right) \frac{\mu^{(p)^2}}{\delta^{(p)^2}} \right\}.$$

**Step 5: Extracting the dominant Gauss sum.**

Let $\mathfrak{b}_1$ be the denominator of the rational function

$$\frac{d\mathfrak{c}^2}{4\omega\delta^2} = \frac{\mathfrak{a}}{4\mathfrak{b}}.$$

The sum over $\mu \in \mathfrak{c}$ can be reorganized modulo the denominator. The dominant contribution as $x \to 0$ comes from the terms where the numerator is divisible by the denominator, giving rise to a Gauss sum $A$ evaluated at the transformed argument.

Applying Lemma (a) to the dual theta function, we obtain

$$\lim_{x \to 0} x^{n/2} \; \theta\left( \frac{1}{t}; \frac{1}{\mathfrak{d}} \right) = \frac{|N(2\omega\delta)|}{|N(\mathfrak{b}_1\mathfrak{c})\sqrt{d}|} \cdot A, \tag{184}$$

where $A$ is the Gauss sum corresponding to the reciprocal argument $-1/(4\omega)$ modulo the appropriate denominator.

**Step 6: Equating the two limits and handling the square root.**

The denominator in the original theta function contains the factor

$$\sqrt{(x - 2i\omega^{(1)}) \cdots (x - 2i\omega^{(n)})}.$$

As $x \to 0$, this tends to

$$\lim_{x \to 0} \sqrt{(x - 2i\omega^{(1)}) \cdots (x - 2i\omega^{(n)})} = |\sqrt{N(2\omega)}| \; e^{-(\pi i/4)(\mathrm{sgn}\,\omega^{(1)} + \mathrm{sgn}\,\omega^{(2)} + \cdots + \mathrm{sgn}\,\omega^{(n)})},$$

where the square roots are chosen according to the standard convention (principal branch). The phase factor accounts for the signs of the conjugates $\omega^{(p)}$.

**Step 7: The reciprocity formula.**

Equating the limits from Steps 3 and 5-6, and using $|d| = N(\mathfrak{d})$, we obtain after simplification

$$\frac{C(\omega)}{N(\mathfrak{a})} = |\sqrt{d}| \cdot \frac{\sqrt{N(2\omega)}}{N(\mathfrak{b}_1)} \; A \; e^{(\pi i/4)S(\mathrm{sgn}\,\omega)},$$

where $S(\mathrm{sgn}\,\omega) = \sum_{p=1}^{n} \mathrm{sgn}\,\omega^{(p)}$.

Equivalently,

$$\frac{C(\omega)}{|\sqrt{N(\mathfrak{a})}|} = \left| \frac{\sqrt{N(2\mathfrak{b})}}{N(\mathfrak{b}_1)} \right| \; e^{(\pi i/4)S(\mathrm{sgn}\,\omega)} \; A.$$

This is the reciprocity law for Gauss sums in totally real fields (Theorems 160-161): it relates the Gauss sum $C(\omega)$ with denominator $\mathfrak{a}$ to the Gauss sum $A$ with transformed argument $-1/(4\omega)$ and denominator $\mathfrak{b}_1$, multiplied by explicit algebraic factors involving norms, discriminants, and a root of unity determined by the signs of the conjugates of $\omega$.

The significance is that, by iterating this reciprocity (applying it to $A$ with a new choice of $\omega$), one can reduce the evaluation of general Gauss sums to elementary cases, ultimately leading to explicit determination of their values.
