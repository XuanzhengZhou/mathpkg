---
role: proof
locale: en
of_concept: tau-e-surjective-homomorphism
source_book: gtm013
source_chapter: "1"
source_section: "1.16"
---

Since $e$ is central, $exe = xe$ for all $x$. Check that $\tau_e$ is a ring homomorphism:

- $\tau_e(x + y) = e(x + y)e = exe + eye = \tau_e(x) + \tau_e(y)$.
- $\tau_e(xy) = exye = exeye = (exe)(eye) = \tau_e(x)\tau_e(y)$ (using centrality of $e$).
- $\tau_e(1) = e1e = e$, which is the identity of $eRe$.

Surjectivity is by definition of $eRe$. For the kernel: $\tau_e(x) = 0$ means $exe = 0$. Multiplying on the left by $(1-e)$ gives $0 = (1-e)exe = 0$, but instead note $x = exe + (1-e)x$ since $x = ex + (1-e)x$ and $exe = 0$. Actually, $x \in \ker \tau_e \iff exe = 0$. Then $x = (1-e)x$ (since $ex = exe$ by centrality, so $ex = e^2xe = exe = 0$). Conversely, if $x \in (1-e)R$, say $x = (1-e)r$, then $exe = e(1-e)re = 0$. Hence $\ker \tau_e = (1-e)R$.
