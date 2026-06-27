---
role: proof
locale: en
of_concept: stone-cech-ordinals
source_book: gtm027
source_chapter: "5"
source_section: "Q: Example on Compactification"
---

# Proof of Stone-Čech Compactification of the Ordinal Space $\Omega_0$

Let $\Omega'$ be the set of all ordinal numbers less than or equal to the first uncountable ordinal $\Omega$, and let $\Omega_0 = \Omega' \setminus \{\Omega\}$, each endowed with the order topology.

**Claim.** The Stone-Čech compactification $\beta(\Omega_0)$ is homeomorphic to $\Omega'$.

**Proof.** By Problem 5.P (characterization of the Stone-Čech compactification via bounded continuous functions), it suffices to show that every bounded real-valued continuous function $f$ on $\Omega_0$ is *eventually constant*: that is, there exists an ordinal $x \in \Omega_0$ such that for all $y > x$ (with $y \in \Omega_0$), $f(y) = f(x)$. If this holds, then each bounded continuous $f$ extends continuously to $\Omega'$ by defining $f(\Omega) = \lim_{y \to \Omega} f(y)$ (the eventual constant value), and consequently $\beta(\Omega_0) \cong \Omega'$.

To prove that every bounded continuous real-valued $f$ on $\Omega_0$ is eventually constant, we use the *interlacing lemma* (Lemma 4.E). Let $r, s \in \mathbb{R}$ with $r > s$. The interlacing lemma implies that for the continuous function $f$, one of the two sets

$$A = \{x \in \Omega_0 : f(x) \geq r\}, \qquad B = \{x \in \Omega_0 : f(x) \leq s\}$$

is countable. (The interlacing lemma states that if a net in a connected ordered space converges, then any two interlacing sequences force a countability restriction on the level sets.)

Now, since $f$ is bounded, let $m = \inf f(\Omega_0)$ and $M = \sup f(\Omega_0)$. For each $n \in \mathbb{N}$, consider the dyadic rationals partitioning $[m, M]$. Using the countability property above, one shows that the oscillation of $f$ on a tail of $\Omega_0$ must be zero. More formally: for each $\varepsilon > 0$, there exists an ordinal $\alpha_\varepsilon \in \Omega_0$ such that for all $\beta, \gamma > \alpha_\varepsilon$, $|f(\beta) - f(\gamma)| < \varepsilon$.

Suppose, for contradiction, that $f$ is not eventually constant. Then there exist $\varepsilon > 0$ and ordinals $\alpha_1 < \alpha_2 < \dots$ in $\Omega_0$ cofinal in $\Omega_0$ such that $|f(\alpha_{2k-1}) - f(\alpha_{2k})| \geq \varepsilon$ for all $k$. By taking a subsequence, we may assume $f(\alpha_{2k-1}) \geq r$ and $f(\alpha_{2k}) \leq s$ for some $r > s$ with $r - s \geq \varepsilon$. This gives uncountably many points in both $A$ and $B$, contradicting the interlacing lemma which forces one of them to be countable.

Therefore $f$ must be eventually constant. (Note: the hypothesis that $f$ be bounded is actually not essential—every continuous real-valued function on $\Omega_0$ is eventually constant, but boundedness simplifies the argument via the dyadic partition.)

Hence every bounded continuous real-valued function on $\Omega_0$ extends continuously to $\Omega'$, which implies $\beta(\Omega_0)$ is homeomorphic to $\Omega'$. $\square$

**Reference:** This result is due to Tong [1].
