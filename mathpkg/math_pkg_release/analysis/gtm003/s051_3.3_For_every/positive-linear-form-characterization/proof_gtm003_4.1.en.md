---
role: proof
locale: en
of_concept: positive-linear-form-characterization
source_book: gtm003
source_chapter: "4"
source_section: "4.1"
---

Let $\phi$ be positive and denote by $(u_{\lambda})$ any approximate unit of $A$. Because $(x, y) \mapsto \phi(y^*x)$ is a positive sesquilinear (or Hermitian) form on $A \times A$, Schwarz' inequality shows that $|\phi(y^*x)|^2 \leq \phi(y^*y)\phi(x^*x)$. Now suppose $\|\phi\| = 1$ and let $0 < \varepsilon \in \mathbb{R}$ be preassigned; there exists $x \in A$, $\|x\| = 1$ such that $|\phi(x)|^2 \geq 1 - \varepsilon$. Since $\lim_{\lambda} u_{\lambda}x = x$, the preceding inequality shows that

$$1 - \varepsilon \leq |\phi(x)|^2 = \lim_{\lambda} |\phi(u_{\lambda}x)|^2 \leq \phi(x^*x) \cdot \lim_{\lambda} \phi(u_{\lambda}^2) \leq \lim_{\lambda} \phi(u_{\lambda})$$

because $0 \leq u_{\lambda}^2 \leq u_{\lambda}$. Since $(u_{\lambda})$ is directed $(\leq)$, we have $\lim_{\lambda} \phi(u_{\lambda}) = 1 = \|\phi\|$.

For the converse assertion, let $\phi \in A'$ satisfy $\|\phi\| = \lim_{\lambda} \phi(u_{\lambda})$ for some approximate unit; we may assume $\|\phi\| = 1$. Given $x \in A_{sa}$, $\|x\| = 1$, let $\phi(x) = \alpha + i\beta$ where we may suppose that $\beta \leq 0$. Then

$$\|x - inu_{\lambda}\|^2 = \|(x + inu_{\lambda})(x - inu_{\lambda})\| = \|x^2 + n^2 u_{\lambda}^2\| \leq 1 + n^2,$$

and since $\|\phi\| = 1$, $|\phi(x - inu_{\lambda})| \leq \sqrt{1 + n^2}$. But

$$\phi(x - inu_{\lambda}) = \alpha + i\beta - in\phi(u_{\lambda}),$$

so that $|\beta - n\phi(u_{\lambda})| \leq \sqrt{1 + n^2}$. Since $\phi(u_{\lambda}) \to 1$, this forces $\beta = 0$ as $n \to \infty$, whence $\phi(x) \in \mathbb{R}$. For $x \geq 0$, we have $\| \|x\|e - x \| \leq \|x\|$, and since $\phi(u_{\lambda}) \to \|\phi\|$, it follows that $\phi(x) \geq 0$. Thus $\phi$ is positive.
