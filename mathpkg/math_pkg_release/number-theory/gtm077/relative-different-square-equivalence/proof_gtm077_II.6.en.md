---
role: proof
locale: en
of_concept: theorem-177
source_book: gtm077
source_chapter: "II"
source_section: "6"
---

# Proof of Theorem 177

**Theorem 177.** If the ideal $\mathfrak{D}_k$ in $k$ is the relative discriminant of a field with respect to $k$, then $\mathfrak{D}_k$ is equivalent to a square in $k$.

**Proof.** The proof applies the reciprocity law for Gauss sums to evaluate the quadratic residue symbol and show that the different $\mathfrak{d}$ belongs to the principal class complex.

**Step 1: Reduction via Gauss sums.** Let $\mathfrak{a}$ be an odd ideal and let $\omega = \mathfrak{a}\mathfrak{d}$ where $\mathfrak{d}$ is the different. Consider the Gauss sum $C(\frac{\varepsilon}{4\omega})$ with denominator $4\omega$. By formula (169), we decompose this sum by introducing an odd auxiliary ideal $\mathfrak{c}$ such that

$$\mathfrak{a}\mathfrak{c} = \alpha, \quad \gamma = \frac{\alpha}{\omega} = \frac{\mathfrak{c}}{\mathfrak{d}}.$$

Then

$$C\left(\frac{\varepsilon}{4\omega}\right) = C\left(\frac{\varepsilon\gamma}{4\alpha}\right) = C\left(\frac{4\varepsilon\gamma}{\alpha}\right) C\left(\frac{\alpha\varepsilon\gamma}{4}\right).$$

If $\varepsilon$ is primary, the right-hand side simplifies to

$$\left(\frac{\varepsilon}{\mathfrak{a}}\right) C\left(\frac{\gamma}{\alpha}\right) C\left(\frac{\alpha\gamma}{4}\right).$$

Taking $\varepsilon = 1$ gives

$$C\left(\frac{1}{4\omega}\right) = C\left(\frac{\gamma}{\alpha}\right) C\left(\frac{\alpha\gamma}{4}\right),$$

and consequently

$$\left(\frac{\varepsilon}{\mathfrak{a}}\right) = \frac{C(\frac{\varepsilon}{4\omega})}{C(\frac{1}{4\omega})}. \tag{215}$$

**Step 2: Application of the reciprocity formula.** Apply the reciprocity formula (199) to transform the sums on the right-hand side into sums with denominator $\varepsilon$. By Theorem 156, these sums can be evaluated directly. We obtain

$$\frac{C(\frac{\varepsilon}{4\omega})}{|\sqrt{N(4\mathfrak{a})}|} = \left|\sqrt{N\left(\frac{2}{\varepsilon}\right)}\right| e^{(\pi i/4)S(\operatorname{sgn} \omega\varepsilon - \operatorname{sgn} \omega)}$$

for each primary number $\varepsilon$ relatively prime to $\mathfrak{a}$.

**Step 3: Evaluation for singular $\varepsilon$.** Now assume that $\varepsilon$ is also a singular number. Then by Theorem 156, the sum $C(-\gamma^2\omega/\varepsilon)$ evaluates to $|\sqrt{N(\varepsilon)}|$. Consequently

$$\left(\frac{\varepsilon}{\mathfrak{a}}\right) = e^{(\pi i/4)S(\operatorname{sgn} \omega\varepsilon - \operatorname{sgn} \omega)}$$

whenever $\omega = \mathfrak{a}\mathfrak{d}$, $\mathfrak{a}$ is odd, and $\varepsilon$ is a singular primary number with $(\varepsilon, \mathfrak{a}) = 1$.

**Step 4: Totally positive case.** If, in addition, $\varepsilon$ is totally positive, the exponent vanishes and

$$\left(\frac{\varepsilon}{\mathfrak{a}}\right) = +1.$$

By Theorem 170, this implies that $\mathfrak{a}$ (as well as the different $\mathfrak{d}$) belongs to the principal class complex in the strict sense.

**Step 5: Extension to the relative discriminant.** Since the differents of relative fields compose according to Theorem 111, it follows that the relative different $\mathfrak{D}_k$ of a field $K$ with respect to a subfield $k$ is always equivalent to the square of an ideal in $k$. Moreover, the relative norm of $\mathfrak{D}_k$ equals the relative discriminant of $K$ with respect to $k$, and is therefore also equivalent to a square in $K$.

Thus $\mathfrak{D}_k$ is equivalent to a square in $k$. ∎
