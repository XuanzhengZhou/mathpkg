---
role: proof
locale: en
of_concept: conformal-automorphisms-unit-disk
source_book: gtm011
source_chapter: "VI"
source_section: "2.5"
---

Since $f$ is one-to-one and onto, there is an analytic function $g: D \to D$ such that $g(f(z)) = z$ for $|z| < 1$. Applying inequality (2.3) to both $f$ and $g$ gives

$$|f'(a)| \leq \frac{1 - |f(a)|^2}{1 - |a|^2} = \frac{1}{1 - |a|^2}$$

(since $f(a) = 0$) and

$$|g'(0)| \leq \frac{1 - |g(0)|^2}{1 - |0|^2} = 1 - |a|^2$$

(since $g(0) = a$). But $g'(0) f'(a) = (g \circ f)'(a) = 1$ because $g(f(z)) = z$. Hence

$$1 = |g'(0) f'(a)| = |g'(0)| \, |f'(a)| \leq (1 - |a|^2) \cdot \frac{1}{1 - |a|^2} = 1.$$

Thus equality holds in both estimates. In particular, $|g'(0)| = 1 - |a|^2$, which means equality occurs in inequality (2.3) for $g$ at $z = 0$. By the case of equality in (2.3), which follows from Schwarz's Lemma, there exists a constant $c$ with $|c| = 1$ such that

$$g(z) = c \varphi_{-a}(z) = c \frac{z + a}{1 + \bar{a}z}.$$

Since $g$ is the inverse of $f$, we obtain $f(z) = g^{-1}(z) = \bar{c} \varphi_a(z)$. Writing $c' = \bar{c}$ (so $|c'| = 1$) gives $f(z) = c' \varphi_a(z)$, completing the proof.
