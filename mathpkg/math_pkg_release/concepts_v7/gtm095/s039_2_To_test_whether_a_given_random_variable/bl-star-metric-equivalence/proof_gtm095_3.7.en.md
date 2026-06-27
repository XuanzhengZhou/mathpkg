---
role: proof
locale: en
of_concept: bl-star-metric-equivalence
source_book: gtm095
source_chapter: "3"
source_section: "§7. Metrizability of Weak Convergence"
---

# Proof that the Bounded Lipschitz Dual Metric Metrizes Weak Convergence

Denote by $BL$ the set of bounded continuous functions $f = f(x)$, $x \in E$, equipped with the norm

$$\|f\|_{BL} = \|f\|_\infty + \sup_{x \neq y} \frac{|f(x) - f(y)|}{\rho(x, y)}.$$

For probability measures $P, \tilde{P} \in \mathcal{P}(E)$, the **dual bounded Lipschitz metric** (also called the BL$^*$ metric) is defined by

$$\|P - \tilde{P}\|_{BL}^* = \sup_{\|f\|_{BL} \leq 1} \left| \int_E f(x) \, P(dx) - \int_E f(x) \, \tilde{P}(dx) \right|.$$

**Theorem.** The BL$^*$ metric metrizes weak convergence:

$$\|P_n - P\|_{BL}^* \to 0 \quad \Longleftrightarrow \quad P_n \xrightarrow{w} P.$$

**Proof.** The implication ($\Leftarrow$) follows directly from condition (13) established in the proof of Theorem 1: if $P_n \xrightarrow{w} P$, then

$$\sup_{f \in \mathcal{G}^\varepsilon} \left| \int_E f(x) \, P_n(dx) - \int_E f(x) \, P(dx) \right| \to 0, \quad n \to \infty,$$

for the class $\mathcal{G}^\varepsilon \subseteq BL$ of functions $f_A^\varepsilon$ defined in (14). Since $BL$ contains $\mathcal{G}^\varepsilon$ and the unit ball of $BL$ is totally bounded (in an appropriate sense for separable metric spaces), the convergence extends to the whole unit ball, giving $\|P_n - P\|_{BL}^* \to 0$.

To prove the forward implication ($\Rightarrow$), suppose $\|P_n - P\|_{BL}^* \to 0$. Then in particular, for every function $f \in BL$, the integrals converge. By Lemma 2, this is sufficient to guarantee $P_n \xrightarrow{w} P$. Indeed, Lemma 2 shows that weak convergence $P_n \xrightarrow{w} P$ is equivalent to the convergence of integrals for all functions of class $BL$. Therefore,

$$\|P_n - P\|_{BL}^* \to 0 \quad \Longrightarrow \quad \int f \, dP_n \to \int f \, dP \;\; \forall f \in BL \quad \Longrightarrow \quad P_n \xrightarrow{w} P.$$

The proof is thus a direct consequence of Lemma 2 (the $BL$-class characterisation of weak convergence) and the definition of the dual norm $\|\cdot\|_{BL}^*$, together with the uniform boundedness of the unit ball in $BL$.

**Remark.** For separable metric spaces $(E, \mathcal{E}, \rho)$, the following inequalities relate the Lévy–Prokhorov metric $L$ and the BL$^*$ metric:

$$L(P, \tilde{P})^2 \leq C \cdot \|P - \tilde{P}\|_{BL}^* \leq C' \cdot L(P, \tilde{P}),$$

so the two metrics induce the same topology (the topology of weak convergence). $\square$
