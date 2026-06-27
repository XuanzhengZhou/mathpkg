---
role: proof
locale: en
of_concept: hellinger-variation-inequalities
source_book: gtm095
source_chapter: "3"
source_section: "9.2"
---

# Proof of Theorem 1 (Inequalities relating the Hellinger integral and total variation distance)

**Theorem 1.** We have the following inequalities:

$$2[1 - H(P, \tilde{P})] \leq \|P - \tilde{P}\| \leq \sqrt{8[1 - H(P, \tilde{P})]},$$

$$\|P - \tilde{P}\| \leq 2\sqrt{1 - H^2(P, \tilde{P})}.$$

In particular,

$$2\rho^2(P, \tilde{P}) \leq \|P - \tilde{P}\| \leq \sqrt{8}\,\rho(P, \tilde{P}).$$

**Proof.** Since $H(P, \tilde{P}) \leq 1$ and $1 - x^2 \leq 2(1 - x)$ for $0 \leq x \leq 1$, the right-hand inequality in (21) follows from (22). The proof of (22) is provided by the following chain of inequalities, where we take $Q = \frac{1}{2}(P + \tilde{P})$ so that $z = dP/dQ$ satisfies $z \in [0, 2]$ and $\tilde{z} = 2 - z$:

$$\frac{1}{2}\|P - \tilde{P}\| = E_Q|1 - z| \leq \sqrt{E_Q|1 - z|^2} = \sqrt{1 - E_Q z(2 - z)}$$

$$= \sqrt{1 - E_Q z \tilde{z}} = \sqrt{1 - E_Q(\sqrt{z\tilde{z}})^2} \leq \sqrt{1 - (E_Q\sqrt{z\tilde{z}})^2}$$

$$= \sqrt{1 - H^2(P, \tilde{P})}.$$

The first inequality is the Cauchy–Schwarz inequality ($E|X| \leq \sqrt{E X^2}$), and the second uses the fact that $E_Q z \tilde{z} = E_Q(\sqrt{z\tilde{z}})^2 \geq (E_Q\sqrt{z\tilde{z}})^2$ by Jensen's inequality.

Finally, the first inequality in (21) follows from the elementary inequality

$$\frac{1}{2}[\sqrt{z} - \sqrt{2 - z}]^2 \leq |z - 1|, \quad z \in [0, 2],$$

which gives (again taking $Q = \frac{1}{2}(P + \tilde{P})$)

$$1 - H(P, \tilde{P}) = \rho^2(P, \tilde{P}) = \frac{1}{2}E_Q[\sqrt{z} - \sqrt{2 - z}]^2 \leq E_Q|z - 1| = \frac{1}{2}\|P - \tilde{P}\|.$$

Multiplying by $2$ yields $2\rho^2(P, \tilde{P}) = 2[1 - H(P, \tilde{P})] \leq \|P - \tilde{P}\|$.
