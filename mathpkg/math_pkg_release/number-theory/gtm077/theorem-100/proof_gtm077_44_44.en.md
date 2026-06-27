---
role: proof
locale: en
of_concept: theorem-100
source_book: gtm077
source_chapter: "VII"
source_section: "Summary and the System of Ideal Classes"
---
# Proof of Theorem 100

**Theorem 100 (Dirichlet's Unit Theorem for Real Quadratic Fields).** In a real quadratic field $k(\sqrt{d})$ with $d > 0$, the number of fundamental units is equal to 1.

*Proof.* In any real quadratic field $k = k(\sqrt{d})$ with $d > 0$, the field has exactly one fundamental unit $\varepsilon$. Since the only real roots of unity are $\pm 1$, the numbers

$$\pm \varepsilon^n \quad (n = 0, \pm 1, \pm 2, \ldots)$$

are all the units of $k$. An element $\eta = (x + y\sqrt{d})/2$ is a unit if and only if its norm satisfies

$$N(\eta) = \pm 1,$$

which is equivalent to the Pell equation

$$x^2 - dy^2 = \pm 4 \tag{104}$$

with rational integers $x$ and $y$.

In an imaginary quadratic field ($d < 0$), every unit $\eta$ is a root of unity. For $d < 0$, Equation (104) (where only the upper sign can hold) has only the trivial solutions $y = 0, x = \pm 2$ (i.e., $\eta = \pm 1$) for $d \leq -5$. For $d = -4$, there are two additional solutions $x = 0, y = \pm 1$; for $d = -3$, there are four additional solutions $x = \pm 1, y = \pm 1$. Thus the number $w$ of roots of unity in $k(\sqrt{-3})$ is 6, in $k(\sqrt{-1})$ it is 4, and in all other imaginary quadratic fields it is 2.

**Application (Pell Equation).** To find a fundamental unit $\eta = (x + y\sqrt{d})/2 > 1$, one uses the fact that among the numbers $\alpha = \omega\eta^n$ ($n = 0, \pm 1, \pm 2, \ldots$) associated to a given $\omega$, there exists one such that

$$1 \leq \left|\frac{\alpha}{\alpha'}\right| < \eta^2$$

(compare Equation (86)). Equivalently,

$$|\omega'| \leq |\omega| < |\omega'|\eta^2 \quad \text{or} \quad |\omega|\eta^{-2} < |\omega'| \leq |\omega|.$$

Since $|\omega\omega'| = n$, this becomes

$$\sqrt{n} \leq |\omega| < \eta\sqrt{n}, \quad \eta^{-1}\sqrt{n} < |\omega'| \leq \sqrt{n}. \tag{106}$$

Assuming $\omega > 0$ and the plus sign in (105), it follows that

$$(\eta^{-1} + 1)\sqrt{n} < x < (\eta + 1)\sqrt{n}; \tag{107}$$

with the minus sign,

$$(\eta^{-1} + 1)\sqrt{n} < y\sqrt{d} < (\eta + 1)\sqrt{n}. \tag{108}$$

Thus only a finite number of integer pairs $(x, y)$ need to be tested to determine whether a solution of the Pell equation yields a fundamental unit. The existence of at least one fundamental unit is guaranteed by Dirichlet's general unit theorem (Lemma (b) in §35), which provides an effective construction via logarithmic embeddings of the units into $\mathbb{R}$. $\square$
