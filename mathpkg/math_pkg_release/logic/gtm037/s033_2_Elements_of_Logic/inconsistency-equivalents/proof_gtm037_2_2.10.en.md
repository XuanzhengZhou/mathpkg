---
role: proof
locale: en
of_concept: inconsistency-equivalents
source_book: gtm037
source_chapter: "2"
source_section: "2.10"
---

These equivalences follow from basic properties of deductive systems.

$(i) \Rightarrow (ii)$: If $\Gamma$ is inconsistent, then $\Gamma \vdash \varphi$ for every formula $\varphi$. In particular, $\Gamma \vdash \psi$ and $\Gamma \vdash \neg\psi$ for any chosen $\psi$, establishing (ii).

$(ii) \Rightarrow (iii)$: If $\Gamma \vdash \varphi$ and $\Gamma \vdash \neg\varphi$ for some $\varphi$, then by the tautology $\varphi \to (\neg\varphi \to \psi)$ and two applications of modus ponens, we obtain $\Gamma \vdash \psi$ for every formula $\psi$.

$(iii) \Rightarrow (i)$: If $\Gamma \vdash \varphi$ for every formula $\varphi$, then in particular $\Gamma$ proves some formula, so $\Gamma$ is inconsistent by definition (the negation of consistency).

[Note: The source text for Proposition 10.90 is truncated in the extracted section — condition (iii) is cut off. The statement and proof above are reconstructed from standard logical reasoning about inconsistency, which is consistent with the established properties of the deductive system.]
