---
role: proof
locale: en
of_concept: backward-equation-jump
source_book: gtm017
source_chapter: "VI"
source_section: "b"
---
Using the Chapman-Kolmogorov equation:
$$P(\tau-\Delta\tau, x; t, A) = \int P(\tau-\Delta\tau, x; \tau, dy) P(\tau, y; t, A).$$

Splitting the integral into $\{x\}$ and $\Omega_X - \{x\}$:
$$P(\tau-\Delta\tau, x; t, A) = P(\tau-\Delta\tau, x; \tau, \{x\}) P(\tau, x; t, A) + \int_{\Omega_X - \{x\}} P(\tau-\Delta\tau, x; \tau, dy) P(\tau, y; t, A).$$

By the jump process infinitesimal condition:
$$P(\tau-\Delta\tau, x; \tau, \{x\}) = 1 - p(\tau, x)\Delta\tau + o(\Delta\tau),$$
$$\frac{P(\tau-\Delta\tau, x; \tau, A)}{\Delta\tau} \to p(\tau, x)\Pi(\tau, x, A) \text{ for } x \notin A.$$

Substituting and taking $\Delta\tau \to 0$ gives the backward equation:
$$\frac{\partial P}{\partial \tau} = p(\tau, x)\{P(\tau, x; t, A) - \int P(\tau, y; t, A)\Pi(\tau, x, dy)\}.$$
