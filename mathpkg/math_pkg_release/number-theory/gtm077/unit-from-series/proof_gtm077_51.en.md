---
role: proof
locale: en
of_concept: unit-from-series
source_book: gtm077
source_chapter: ""
source_section: "51"
---
# Proof of Theorem 149

**Theorem 149.** The expression

$$\varepsilon^{2h} = e^{\sqrt{d} \sum_{n=1}^{\infty} \left(\frac{d}{n}\right)/n}$$

represents a unit of infinite degree in $k(\sqrt{d})$ with $d > 0$. And

$$\varepsilon^{2h} + \varepsilon'^{2h} = \varepsilon^{2h} + \varepsilon^{-2h} = e^{\sqrt{d}L(1)} + e^{-\sqrt{d}L(1)} = A$$

is a rational integer such that this unit is the larger of the two roots of the equation

$$x^2 - Ax + 1 = 0.$$

*Proof.* From §49 we have the factorization of the Dedekind zeta-function of the quadratic field $k = k(\sqrt{d})$:

$$\zeta_k(s) = \zeta(s) \cdot L(s),$$

where

$$L(s) = \prod_{p} \frac{1}{1 - \chi(p)p^{-s}} \tag{137}$$

and $\chi$ is the quadratic residue character modulo $|d|$ (the Kronecker symbol $\left(\frac{d}{\cdot}\right)$). From the analytic class number formula derived there, we obtain the relation

$$h \cdot \kappa = \lim_{s \to 1} L(s), \tag{138}$$

where $h$ is the class number and $\kappa$ is the regulator factor.

Now, $\chi(n) = \left(\frac{d}{n}\right)$ is a residue character modulo $|d|$ for positive integers $n$. Consequently, the Euler product (137) expands to the Dirichlet series

$$L(s) = \sum_{n=1}^{\infty} \frac{\chi(n)}{n^s}.$$

By Theorem 128, this Dirichlet series with the residue character $\chi(n)$ converges at $s = 1$. Combining this with the limit relation (138), we obtain

$$h \cdot \kappa = L(1) = \sum_{n=1}^{\infty} \frac{\chi(n)}{n}. \tag{145}$$

This is precisely the same formula that was derived in §50 without using the zeta-function, confirming consistency of the approach.

For the quadratic field $k(\sqrt{d})$, the regulator factor $\kappa$ (derived from the structure of the unit group) takes the following explicit forms depending on the sign of the discriminant $d$:

$$\kappa = \begin{cases} \dfrac{2 \log \varepsilon}{|\sqrt{d}|} & \text{if } d > 0,\\[10pt] \dfrac{2\pi}{w|\sqrt{d}|} & \text{if } d < 0, \end{cases}$$

where for $d > 0$, $\varepsilon > 1$ denotes the fundamental unit of the real quadratic field; for $d < 0$, $w$ denotes the number of roots of unity in the imaginary quadratic field ($w = 2$ for $d < -4$).

We now restrict to the case $d > 0$ (real quadratic fields). Substituting $\kappa = \frac{2\log \varepsilon}{\sqrt{d}}$ into (145) yields

$$h \cdot \frac{2 \log \varepsilon}{\sqrt{d}} = L(1) = \sum_{n=1}^{\infty} \frac{\chi(n)}{n}.$$

Solving for $\log \varepsilon$:

$$2h \log \varepsilon = \sqrt{d} \, L(1),$$

and exponentiating both sides gives

$$\varepsilon^{2h} = e^{\sqrt{d} \, L(1)} = e^{\sqrt{d} \sum_{n=1}^{\infty} \left(\frac{d}{n}\right)/n}.$$

This exhibits $\varepsilon^{2h}$ as a transcendental expression in terms of the convergent series $L(1)$, proving the first assertion of the theorem.

For the second assertion, let $\varepsilon'$ denote the conjugate of $\varepsilon$ in $k(\sqrt{d})$. Since $\varepsilon$ is a unit of the real quadratic field, its conjugate is $\varepsilon' = \pm \varepsilon^{-1}$; because $\varepsilon > 1$ and the norm is $N(\varepsilon) = \varepsilon\varepsilon' = \pm 1$ (and in a real quadratic field with $d > 0$, the fundamental unit has norm $+1$ when $d$ is not of the form $d = a^2 + 4$, otherwise possibly $-1$), we have $\varepsilon' = \varepsilon^{-1}$ (or for the square $\varepsilon^2$, certainly $\varepsilon^{2}\varepsilon'^{2} = 1$). Thus

$$\varepsilon^{2h} + \varepsilon'^{2h} = \varepsilon^{2h} + \varepsilon^{-2h} = e^{\sqrt{d}L(1)} + e^{-\sqrt{d}L(1)} = A.$$

The sum $A = \varepsilon^{2h} + \varepsilon^{-2h}$ is invariant under the nontrivial Galois automorphism of $k(\sqrt{d})/\mathbb{Q}$, hence lies in $\mathbb{Q}$. Moreover, $\varepsilon$ is an algebraic integer, so $\varepsilon^{2h}$ is also an algebraic integer. The sum of an algebraic integer and its conjugate is an integer symmetric in the Galois group, hence $A \in \mathbb{Z}$.

The quadratic equation with roots $\varepsilon^{2h}$ and $\varepsilon^{-2h}$ is

$$(x - \varepsilon^{2h})(x - \varepsilon^{-2h}) = x^2 - (\varepsilon^{2h} + \varepsilon^{-2h})x + 1 = x^2 - Ax + 1 = 0.$$

Since $\varepsilon^{2h} > 1$ (as $\varepsilon > 1$ and $h \ge 1$), the unit $\varepsilon^{2h}$ is the larger of the two roots. This completes the proof.

**Remark.** The rational integer $A$ can be calculated numerically by estimating the remainder of the convergent series $L(1)$. This provides a transcendental method for finding a unit in real quadratic fields. ∎
