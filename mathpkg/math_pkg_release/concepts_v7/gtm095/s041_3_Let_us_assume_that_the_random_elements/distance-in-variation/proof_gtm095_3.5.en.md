---
role: proof
locale: en
of_concept: distance-in-variation
source_book: gtm095
source_chapter: "3"
source_section: "5"
---

# Proof of Lemma 1 (Distance in Variation as Twice the Supremum over Events)

The distance in variation between two probability measures $P$ and $\tilde{P}$ is defined by

$$\|P - \tilde{P}\| = \sup_{|\varphi| \leq 1} |E\varphi - \tilde{E}\varphi|,$$

where the supremum is over all $\mathcal{F}$-measurable functions $\varphi$ with $|\varphi(\omega)| \leq 1$.

The claim is:

$$\|P - \tilde{P}\| = 2 \sup_{A \in \mathcal{F}} |P(A) - \tilde{P}(A)|.$$

*Proof.* First, we prove $2\sup_{A \in \mathcal{F}} |P(A) - \tilde{P}(A)| \leq \|P - \tilde{P}\|$.

Since for all $A \in \mathcal{F}$,

$$P(A) - \tilde{P}(A) = \tilde{P}(\overline{A}) - P(\overline{A}),$$

we have

$$2|P(A) - \tilde{P}(A)| = |P(A) - \tilde{P}(A)| + |P(\overline{A}) - \tilde{P}(\overline{A})| \leq \|P - \tilde{P}\|,$$

where the last inequality follows from the definition of $\|\cdot\|$ applied to the indicator functions $I_A$ and $I_{\overline{A}}$, each having absolute value bounded by 1.

For the proof of the converse inequality, we turn to the Hahn decomposition (see, for example, [52], §5, Chapter VI, or [39], p. 121) of the signed measure $\mu \equiv P - \tilde{P}$. In this decomposition, the measure $\mu$ is represented in the form $\mu = \mu_+ - \mu_-$, where the nonnegative measures $\mu_+$ and $\mu_-$ (the upper and lower variations of $\mu$) are of the form

$$\mu_+(A) = \int_{A \cap M} d\mu, \quad \mu_-(A) = -\int_{A \cap \overline{M}} d\mu, \quad A \in \mathcal{F},$$

where $M$ is a set in $\mathcal{F}$. Here

$$\operatorname{var} \mu = \operatorname{var} \mu_+ + \operatorname{var} \mu_- = \mu_+(\Omega) + \mu_-(\Omega).$$

Since

$$\mu_+(\Omega) = P(M) - \tilde{P}(M), \quad \mu_-(\Omega) = \tilde{P}(\overline{M}) - P(\overline{M}),$$

it follows that

$$\|P - \tilde{P}\| = \operatorname{var}(P - \tilde{P}) = 2(P(M) - \tilde{P}(M)) \leq 2 \sup_{A \in \mathcal{F}} |P(A) - \tilde{P}(A)|.$$

Combining the two inequalities yields the desired equality.

$\square$

**Remark.** The Hahn set $M$ appearing in the proof is the set on which the Radon–Nikodym derivative $dP/dQ$ exceeds $d\tilde{P}/dQ$ (with respect to a dominating measure $Q$). This provides the link to the alternative characterization of variation distance via $L^1$-distance of densities (Lemma 2).
