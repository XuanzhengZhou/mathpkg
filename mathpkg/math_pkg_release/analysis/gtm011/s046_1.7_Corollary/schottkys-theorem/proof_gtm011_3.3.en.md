---
role: proof
locale: en
of_concept: schottkys-theorem
source_book: gtm011
source_chapter: "3"
source_section: "3.3"
---

It suffices to prove the theorem for $2 \leq \alpha < \infty$. The proof proceeds by considering two cases.

**Case 1.** Suppose $\frac{1}{2} \leq |f(0)| \leq \alpha$. Recalling the functions $F$, $H$, and $g$ from Lemma 2.1, the branch condition (3.1) $0 \leq \operatorname{Im} \ell(0) < 2\pi$ gives

$$|F(0)| = \frac{1}{2\pi} \bigl| \log|f(0)| + i\operatorname{Im} \ell(0) \bigr| \leq \frac{1}{2\pi} \log \alpha + 1.$$

Define $C_0(\alpha) = \frac{1}{2\pi} \log \alpha + 1$. Also,

$$|\sqrt{F(0)} \pm \sqrt{F(0)-1}| \leq |\sqrt{F(0)}| + |\sqrt{F(0)-1}| \leq \sqrt{C_0(\alpha)} + \sqrt{C_0(\alpha)+1}.$$

Let $C_1(\alpha) = \sqrt{C_0(\alpha)} + \sqrt{C_0(\alpha)+1}$, so that $|H(0)| \leq C_1(\alpha)$. From the branch condition (3.2) $0 \leq \operatorname{Im} g(0) < 2\pi$, we obtain

$$|g(0)| \leq \log C_1(\alpha) + 2\pi.$$

Set $C_2(\alpha) = \log C_1(\alpha) + 2\pi$.

If $|a| < 1$, then Corollary 1.11 implies that $g(B(a; 1 - |a|))$ contains a disk of radius

$$L(1 - |a|) |g'(a)|.$$

On the other hand, by Lemma 2.2, $g(B(0; 1))$ contains no disk of radius $1$. Hence

$$L(1 - |a|) |g'(a)| < 1,$$

that is,

$$|g'(a)| < [L(1 - |a|)]^{-1} \quad \text{for } |a| < 1.$$

Now for $|a| < 1$, let $\gamma$ be the line segment $[0, a]$. Then

$$|g(a)| \leq |g(0)| + |g(a) - g(0)| \leq C_2(\alpha) + \left| \int_{\gamma} g'(z) \, dz \right| \leq C_2(\alpha) + |a| \max\{|g'(z)| : z \in [0, a]\}.$$

Using the derivative bound (3.6),

$$|g(a)| \leq C_2(\alpha) + \frac{|a|}{L(1 - |a|)}.$$

Define $C_3(\alpha, \beta) = C_2(\alpha) + \frac{\beta}{L(1 - \beta)}$. Then $|g(z)| \leq C_3(\alpha, \beta)$ for $|z| \leq \beta$.

Consequently, for $|z| \leq \beta$,

$$|f(z)| = |\exp[\pi i \cosh(2g(z))]| \leq \exp[\pi |\cosh(2g(z))|] \leq \exp[\pi e^{2|g(z)|}] \leq \exp[\pi e^{2C_3(\alpha, \beta)}].$$

Define $C(\alpha, \beta) = \exp[\pi e^{2C_3(\alpha, \beta)}]$ for Case 1.

**Case 2.** If $|f(0)| < \frac{1}{2}$, apply Case 1 to the function $1 - f$, which also omits $0$ and $1$ and satisfies $|1 - f(0)| \geq \frac{1}{2}$. This yields a bound on $|1 - f(z)|$ and hence on $|f(z)|$. Taking the larger of the two constants completes the proof.
