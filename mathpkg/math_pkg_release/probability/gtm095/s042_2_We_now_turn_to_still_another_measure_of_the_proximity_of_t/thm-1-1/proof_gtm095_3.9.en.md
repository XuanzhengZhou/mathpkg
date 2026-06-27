---
role: proof
locale: en
of_concept: thm-1-1
source_book: gtm095
source_chapter: "3"
source_section: "9.2"
---

# Proof of Theorem 1 (Inequalities between variation and Hellinger distance)

**Theorem 1.** We have the following inequalities:

$$2[1 - H(P, \tilde{P})] \leq \|P - \tilde{P}\| \leq \sqrt{8[1 - H(P, \tilde{P})]}, \tag{21}$$

$$\|P - \tilde{P}\| \leq 2\sqrt{1 - H^2(P, \tilde{P})}. \tag{22}$$

In particular,

$$2\rho^2(P, \tilde{P}) \leq \|P - \tilde{P}\| \leq \sqrt{8}\,\rho(P, \tilde{P}).$$

**Proof.** Since $H(P, \tilde{P}) \leq 1$ and $1 - x^2 \leq 2(1 - x)$ for $0 \leq x \leq 1$, the right-hand inequality in (21) follows from (22), the proof of which uses the dominating measure $Q = \frac{1}{2}(P + \tilde{P})$. Then $dP/dQ = z$, $d\tilde{P}/dQ = 2 - z$, and

$$\frac{1}{2}\|P - \tilde{P}\| = E_Q|1 - z| \leq \sqrt{E_Q|1 - z|^2}$$

$$= \sqrt{1 - E_Q z(2 - z)} = \sqrt{1 - E_Q z \tilde{z}}$$

$$= \sqrt{1 - E_Q(\sqrt{z\tilde{z}})^2} \leq \sqrt{1 - (E_Q\sqrt{z\tilde{z}})^2}$$

$$= \sqrt{1 - H^2(P, \tilde{P})}.$$

Here the first inequality is Cauchy–Schwarz and the second follows from Jensen's inequality ($E(\sqrt{z\tilde{z}})^2 \geq (E\sqrt{z\tilde{z}})^2$).

The first inequality in (21) follows from

$$\frac{1}{2}[\sqrt{z} - \sqrt{2 - z}]^2 \leq |z - 1|, \quad z \in [0, 2],$$

which yields

$$1 - H(P, \tilde{P}) = \rho^2(P, \tilde{P}) = \frac{1}{2}E_Q[\sqrt{z} - \sqrt{2 - z}]^2 \leq E_Q|z - 1| = \frac{1}{2}\|P - \tilde{P}\|.$$

Thus $2\rho^2(P, \tilde{P}) \leq \|P - \tilde{P}\|$.

**Application.** For direct product measures $P^n = P \times \cdots \times P$ and $\tilde{P}^n = \tilde{P} \times \cdots \times \tilde{P}$, since $H(P^n, \tilde{P}^n) = [H(P, \tilde{P})]^n = e^{-\lambda n}$ with $\lambda = -\log H(P, \tilde{P}) \geq \rho^2(P, \tilde{P})$, we obtain

$$\frac{1}{2} e^{-2\lambda n} \leq \mathcal{E}r(P^n, \tilde{P}^n) \leq e^{-\lambda n} \leq e^{-n\rho^2(P, \tilde{P})}.$$

Hence, when $n \to \infty$, the error probability $\mathcal{E}r(P^n, \tilde{P}^n)$ decreases exponentially to zero whenever $\rho^2(P, \tilde{P}) > 0$ (i.e., $P \neq \tilde{P}$).
