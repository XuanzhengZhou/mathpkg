---
role: proof
locale: en
of_concept: corollary-1-11
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. It is only necessary to prove this theorem for $2 \leq \alpha < \infty$. The proof is accomplished by looking at two cases.

Case 1. Suppose $\frac{1}{2} \leq |f(0)| \leq \alpha$. Recalling the functions $F, H,$ and $g$ in Lemma 2.1 (and rediscussed at the beginning of this section), (3.1) gives

$$|F(0)| = \frac{1}{2\pi} |\log|f(0)| + i \text{Im } \ell(0)|$$
$$\leq \frac{1}{2\pi} \log \alpha + 1;$$

Let $C_0(\alpha) = \frac{1}{2\pi} \log \alpha + 1$. Also

3.4 $|\sqrt{F(0)} \pm \sqrt{F(0)-1}| \leq |\sqrt{F(0)}| + |\sqrt{

Let $C_2(\alpha) = \log C_1(\alpha) + 2\pi$.

If $|a| < 1$ then Corollary 1.11 implies that $g(B(a; 1 - |a|))$ contains a disk of radius

3.5 $L(1 - |a|) |g'(a)|$.

On the other hand, Lemma 2.2 says that $g(B(0; 1))$ contains no disk of radius 1. Hence, the expression (3.5) must be less than 1; that is,

3.6 $|g'(a)| < [L(1 - |a|)]^{-1}$ for $|a| < 1$.

If $|a| < 1$, let $\gamma$ be the line segment $[0, a]$; then

$$|g(a)| \leq |g(0)| + |g(a) - g(0)|$$

$$\leq C_2(\alpha) + \left| \int_{\gamma} g'(z) \, dz \right|$$

$$\leq C_2(\alpha) + |a| \max \{ |g'(z)| : z \in [0, a] \}$$

Using (3.6) this gives

$$|g(a)| \leq C_2(\alpha) + \frac{|a|}{L(1 - |a|)}$$

If $C_3(\alpha, \beta) = C_2(\alpha) + \beta [L(1 - \beta)]^{-1}$ then this gives

$$|g(z)| \leq C_3(\alpha, \beta)$$

if $|z| \leq \beta$. Consequently if $|z| \leq \beta$,

$$|f(z)| = |\exp [\pi i \cosh 2g(z)]|$$

$$\leq \exp [\pi |\cosh 2g(z)|]$$

$$\leq \exp [\pi e^{2|g(z)|}]$$

$$\leq \exp [\pi e^{2C_3(\alpha, \beta)}]$$;

define $C_4(\alpha, \beta) = \exp \{ \pi \exp [2C_3(\alpha,
