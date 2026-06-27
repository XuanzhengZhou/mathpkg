---
role: proof
locale: en
of_concept: theorem-9-12
source_book: gtm055
source_chapter: "8-9"
source_section: "Section 10_Section_10"
---

Proof. If $(\dot{\mathbf{S}}_{\mathcal{F}}, \rho)$ is the metric space associated with $(X, \mathbf{S}, \mu)$, then by hypothesis there exists a dense sequence $\{[E_n]\}$ in $\dot{\mathbf{S}}_{\mathcal{F}}$. Set $X_0 = \bigcup_n E_n$. If $E$ is a measurable subset of $X \setminus X_0$, then $\mu(E)$ must be either 0 or $+\infty$. Since $\mu$ is atom-free, this implies that $\mu(X \setminus X_0) = 0$, and hence that $\mu$ is $\sigma$-finite. Thus it suffices to treat the case $0 < \mu(X) < +\infty$ (cf. Example 8H, Example K, and Problem 8R). Accordingly we assume henceforth that $\{[E_n]\}_{n=1}^{\infty}$ is a fixed dense sequence in the metric space associated with the finite measure space $(X, \mathbf{S}, \mu)$ (with $\mu(X) > 0$), and we write $(Y, \mathbf{B}, \nu)$ for the measure space consisting of the interval $[0, \mu(X)]$ equipped with Lebesgue–Borel measure. For each positive integer $n$ let $\mathcal{P}_n$ be the partition of $X$ determined by the sets $E_1, E_2, \ldots, E_n$, that is, the partition consisting of all the nonempty subsets of $X$ of the form $A_1 \cap \cdots \cap A_n$, where, for each $

by continuity, we obtain an isometry $\Phi$ of $\dot{S}$ onto $\dot{B}$. Since $\Phi$ is isometric, we have $\dot{v}(\Phi([E])) = \dot{\mu}([E])$ for every $E$ in $S$. Likewise, $\Phi| \dot{R} = \Phi_0$ preserves $\vee$ and $\backslash$, and since $\dot{R}$ is dense in $\dot{S}$, and since the operations $\vee$ and $\backslash$ are continuous on $\dot{S}$ and on $\dot{B}$ (Prop. 9.9), we see that $\Phi$ also preserves $\vee$ and $\backslash$. Finally, this shows that $\Phi$ is order preserving, from which it follows at once that

$$\Phi \left( \bigvee_{n=1}^{\infty} [F_n] \right) = \bigvee_{n=1}^{\infty} \Phi([F_n])$$

for every sequence $\{[F_n]\}$ in $\dot{S}$. Thus $\Phi$ is a measure ring isomorphism of $(\dot{S}, \dot{\mu})$ onto $(\dot{B}, \dot{v})$.
