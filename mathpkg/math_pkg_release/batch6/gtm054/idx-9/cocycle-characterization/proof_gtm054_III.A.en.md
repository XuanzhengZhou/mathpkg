---
role: proof
locale: en
of_concept: cocycle-characterization
source_book: gtm054
source_chapter: "III"
source_section: "A"
---

(a) If $C$ is an arbitrary vertex cocycle of $\Gamma$, then $\pi_{E+F}[C] = C \cap (E + F)$ is a vertex cocycle of $\Gamma_{(F)}$. Moreover, all vertex cocycles of $\Gamma_{(F)}$ are of this form. Thus $\pi_{E+F} : \mathcal{L}^{\perp}(\Gamma) \rightarrow \mathcal{L}^{\perp}(\Gamma_{(F)})$ is a surjection. Hence $\dim(\mathcal{L}^{\perp}(\Gamma)) = \dim(\ker \pi_{E+F}) + \dim(\mathcal{L}^{\perp}(\Gamma_{(F)}))$.

Now $F$ contains a nonempty cocycle if and only if $\ker \pi_{E+F} \neq \{\varnothing\}$, which is equivalent to $\dim(\mathcal{L}^{\perp}(\Gamma)) > \dim(\mathcal{L}^{\perp}(\Gamma_{(F)}))$. By A15a, this inequality is equivalent to $\nu_{-1}(\Gamma_{(F)}) > \nu_{-1}(\Gamma)$. This proves (a).

(b) If $F$ is an elementary cocycle, then by definition $F$ is a minimal nonempty cocycle, so $F$ contains a nonempty cocycle and by (a) we have $\nu_{-1}(\Gamma_{(F)}) > \nu_{-1}(\Gamma)$. For any $e \in F$, $F + \{e\}$ (i.e., $F \setminus \{e\}$ being a proper subset of $F$) does not contain any nonempty cocycle, so by (a) $\nu_{-1}(\Gamma_{(F+e)}) = \nu_{-1}(\Gamma)$.

Conversely, if the two rank conditions hold, then by (a) $F$ contains a nonempty cocycle, and the minimality condition on the ranks implies that no proper subset of $F$ contains a nonempty cocycle, so $F$ is an elementary cocycle.
