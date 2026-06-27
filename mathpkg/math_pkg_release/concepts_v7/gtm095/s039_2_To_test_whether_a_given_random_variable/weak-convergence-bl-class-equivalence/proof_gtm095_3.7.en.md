---
role: proof
locale: en
of_concept: weak-convergence-bl-class-equivalence
source_book: gtm095
source_chapter: "3"
source_section: "§7. Metrizability of Weak Convergence"
---

# Proof of Weak Convergence Characterisation via Bounded Lipschitz Functions

**Lemma.** Weak convergence $P_n \xrightarrow{w} P$ occurs if and only if

$$\int_E f(x) \, P_n(dx) \to \int_E f(x) \, P(dx) \tag{12}$$

for every function $f = f(x)$ of class $BL$, where $BL$ denotes the set of bounded continuous functions on $E$ that satisfy a Lipschitz condition.

**Proof.** The implication ($\Leftarrow$) is obvious: if (12) holds for all bounded Lipschitz functions, then in particular it holds for all bounded continuous functions, so $P_n \xrightarrow{w} P$ by the definition of weak convergence.

For ($\Rightarrow$), we must show that it suffices to test weak convergence against the subclass $BL \subset C_b(E)$. Consider the functions

$$f_A^\varepsilon(x) = \left(1 - \frac{\rho(x, A)}{\varepsilon}\right)^+,$$

defined for each $A \in \mathcal{E}$ and $\varepsilon > 0$, where $\rho(x, A) = \inf_{y \in A} \rho(x, y)$ and $z^+ = \max(z, 0)$.

These functions satisfy:

$$I_A(x) \leq f_A^\varepsilon(x) \leq I_{A^\varepsilon}(x),$$

and

$$|f_A^\varepsilon(x) - f_A^\varepsilon(y)| \leq \varepsilon^{-1} \rho(x, y).$$

Hence for each $\varepsilon > 0$, the class $\mathcal{G}^\varepsilon = \{f_A^\varepsilon(x) : A \in \mathcal{E}\}$ is contained in $BL$ (each function is bounded by $1$ and Lipschitz with constant $\varepsilon^{-1}$).

Now recall the proof of the implication (I) $\Rightarrow$ (II) in Theorem 1 of Sect. 1 (the portmanteau theorem). An examination of that proof reveals that it does **not** require property (12) for all bounded continuous functions, but only for the functions of class $\mathcal{G}^\varepsilon$, $\varepsilon > 0$. Concretely, the proof uses test functions of the form $f_A^\varepsilon$ to translate between statements about measures of closed/open sets and integrals of continuous functions.

Since $\mathcal{G}^\varepsilon \subseteq BL$ for every $\varepsilon > 0$, the validity of (12) for all functions in $BL$ implies the validity of (12) for all functions in $\mathcal{G}^\varepsilon$, which in turn implies (by Theorem 1 of Sect. 1) that $P_n \xrightarrow{w} P$.

Thus, testing weak convergence against the class $BL$ of bounded Lipschitz functions is both necessary and sufficient. $\square$

**Remark.** The conclusion of Theorem 2 (equivalence of the BL$^*$ metric convergence and weak convergence) can be derived from Theorem 1 (metrizability by the Lévy–Prokhorov metric) and conversely, using the following inequalities valid for separable metric spaces $(E, \mathcal{E}, \rho)$:

$$\|P - \tilde{P}\|_{BL}^* \leq C \cdot L(P, \tilde{P}),$$

where $\|P - \tilde{P}\|_{BL}^* = \sup\{ |\int f \, dP - \int f \, d\tilde{P}| : \|f\|_{BL} \leq 1\}$ is the dual bounded Lipschitz metric.
