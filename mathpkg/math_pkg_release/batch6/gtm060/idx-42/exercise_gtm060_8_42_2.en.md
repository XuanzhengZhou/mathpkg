---
role: exercise
locale: en
chapter: "8"
section: "42"
exercise_number: 2
---

**Problem.** Let $x$ and $y$ be two points in $\mathbb{R}^{2n}$, $\gamma$ a curve connecting them with $\partial\gamma = y - x$. Consider the images of the curve $\gamma$ under the transformations $g_\tau$, $0 \leq \tau \leq \varepsilon$, forming a band $\sigma(\varepsilon)$. Show that

$$\lim_{\varepsilon \to 0} \frac{1}{\varepsilon} \iint_{\sigma(\varepsilon)} \omega^2 = H(x) - H(y)$$

exists and does not depend on the representative of the class $g_\varepsilon$, where $\omega^2 = \sum dp_i \wedge dq_i$ is the canonical symplectic form and $H$ is the hamiltonian function generating the infinitesimal canonical transformation.

*(Hint: Use the fact that $\partial\sigma = g_\varepsilon\gamma - \gamma + g_\tau x - g_\tau y$ and apply Stokes' theorem.)*
