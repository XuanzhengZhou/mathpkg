---
role: proof
locale: en
of_concept: greens-function-conformal-invariance
source_book: gtm011
source_chapter: "X"
source_section: "5"
---

*Proof.* Let $f: G \to \Omega$ be a conformal equivalence. Near $z = a$, we can write

$$f(z) = \alpha + A_1(z-a) + A_2(z-a)^2 + \ldots$$

with $A_1 \neq 0$ (since $f$ is one-one and analytic, $f'(a) \neq 0$). Then

$$\log|f(z) - \alpha| = \log|z-a| + h(z)$$

where $h(z) = \log|A_1 + A_2(z-a) + \ldots|$ is harmonic near $z = a$ since $A_1 \neq 0$.

Suppose that $\gamma_\alpha(w) = \Delta(w) - \log|w - \alpha|$ where $\Delta$ is a harmonic function on $\Omega$ (this follows from properties (a) and (b) of the Green's Function). Define $\varphi(z) = \gamma_\alpha(f(z))$. Then

\begin{align*}
\varphi(z) &= \Delta(f(z)) - \log|f(z) - \alpha| \\
&= [\Delta(f(z)) - h(z)] - \log|z - a|.
\end{align*}

Since $\Delta \circ f$ is harmonic on $G$ (as the composition of a harmonic function with an analytic function) and $h$ is harmonic near $z = a$, the function $\Delta \circ f - h$ is harmonic near $z = a$. Hence $\varphi(z) + \log|z-a|$ is harmonic near $z = a$, verifying property (b).

Property (a) (harmonicity on $G - \{a\}$) follows since $\Delta \circ f$ is harmonic on $G$ and $\log|f(z)-\alpha|$ is harmonic on $G - \{a\}$.

For property (c), if $z \to w \in \partial_\infty G$, then $f(z) \to f(w) \in \partial_\infty \Omega$ (since $f$ is a homeomorphism of the closures), so

$$\lim_{z \to w} \varphi(z) = \lim_{\zeta \to f(w)} \gamma_\alpha(\zeta) = 0.$$

Thus $\varphi(z) = g_a(z)$ is the Green's Function on $G$ with singularity at $a$. $\square$
