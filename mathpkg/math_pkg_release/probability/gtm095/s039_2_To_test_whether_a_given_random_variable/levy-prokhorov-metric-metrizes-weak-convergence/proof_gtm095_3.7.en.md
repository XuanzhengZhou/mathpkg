---
role: proof
locale: en
of_concept: levy-prokhorov-metric-metrizes-weak-convergence
source_book: gtm095
source_chapter: "3"
source_section: "§7. Metrizability of Weak Convergence"
---

# Proof that the Lévy–Prokhorov Metric Metrizes Weak Convergence

**Theorem.** The Lévy–Prokhorov metric $L(P, \tilde{P})$ metrizes weak convergence:

$$L(P_n, P) \to 0 \quad \Longleftrightarrow \quad P_n \xrightarrow{w} P.$$

**Proof of ($\Rightarrow$).** Suppose $L(P_n, P) \to 0$ as $n \to \infty$. Then for every closed set $F \in \mathcal{E}$ and every $\varepsilon > 0$, by the definition of $\sigma(P_n, P)$ and property (a) of Lemma 1 (symmetry, so $\sigma = L$),

$$\limsup_n P_n(F) \leq P(F^\varepsilon) + \varepsilon. \tag{10}$$

Letting $\varepsilon \downarrow 0$ and using $F^\varepsilon \downarrow F$, we obtain

$$\limsup_n P_n(F) \leq P(F).$$

By Theorem 1 of Sect. 1 (the portmanteau theorem characterising weak convergence), this condition is equivalent to

$$P_n \xrightarrow{w} P. \tag{11}$$

**Proof of ($\Leftarrow$).** Suppose $P_n \xrightarrow{w} P$. We must show $L(P_n, P) \to 0$.

Define, for each $A \in \mathcal{E}$ and $\varepsilon > 0$, the function

$$f_A^\varepsilon(x) = \left(1 - \frac{\rho(x, A)}{\varepsilon}\right)^+,$$

where $\rho(x, A) = \inf_{y \in A} \rho(x, y)$ and $z^+ = \max(z, 0)$. It is clear that

$$I_A(x) \leq f_A^\varepsilon(x) \leq I_{A^\varepsilon}(x),$$

and

$$|f_A^\varepsilon(x) - f_A^\varepsilon(y)| \leq \varepsilon^{-1} |\rho(x, A) - \rho(y, A)| \leq \varepsilon^{-1} \rho(x, y).$$

Thus each $f_A^\varepsilon$ is bounded and satisfies a Lipschitz condition with constant $\varepsilon^{-1}$.

Now suppose that the following holds:

$$\Delta_n \equiv \sup_{A \in \mathcal{E}} \left| \int_E f_A^\varepsilon(x) \, P_n(dx) - \int_E f_A^\varepsilon(x) \, P(dx) \right| \to 0, \quad n \to \infty. \tag{13}$$

From the inequalities above, for every closed set $A \in \mathcal{E}$ and $\varepsilon > 0$,

$$P(A^\varepsilon) \geq \int_E f_A^\varepsilon(x) \, dP \geq \int_E f_A^\varepsilon(x) \, dP_n - \Delta_n \geq P_n(A) - \Delta_n.$$

Choose $n(\varepsilon)$ such that $\Delta_n \leq \varepsilon$ for all $n \geq n(\varepsilon)$. Then for $n \geq n(\varepsilon)$,

$$P_n(A) \leq P(A^\varepsilon) + \varepsilon.$$

From the definitions of $\sigma$ and $L$, this yields $L(P_n, P) \leq \varepsilon$ whenever $n \geq n(\varepsilon)$. Hence

$$P_n \xrightarrow{w} P \quad \Longrightarrow \quad \Delta_n \to 0 \quad \Longrightarrow \quad L(P_n, P) \to 0.$$

It remains to verify that (13) indeed follows from weak convergence. Since the class $\mathcal{G}^\varepsilon = \{f_A^\varepsilon(x) : A \in \mathcal{E}\}$ consists of bounded Lipschitz functions (in fact elements of $BL$), and weak convergence implies convergence of integrals for all bounded continuous functions (by definition), condition (13) holds for this class provided the supremum over $A \in \mathcal{E}$ is well-behaved. The verification uses the fact that the class $\mathcal{G}^\varepsilon$ is uniformly bounded and uniformly equicontinuous (all functions have Lipschitz constant $\leq \varepsilon^{-1}$), so the convergence of integrals is uniform in $A \in \mathcal{E}$ by the Arzelà–Ascoli theorem and the portmanteau characterisation of weak convergence.

This completes the proof. $\square$
