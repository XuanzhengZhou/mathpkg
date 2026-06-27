---
role: proof
locale: en
of_concept: godels-second-incompleteness-theorem
source_book: gtm053
source_chapter: "VII"
source_section: "1"
---

# Proof of Gödel's Second Incompleteness Theorem

**Theorem (Gödel's Second Incompleteness Theorem).** Let $T$ be a consistent, recursively axiomatizable theory containing enough arithmetic (e.g., Peano Arithmetic). Then $T$ cannot prove its own consistency. Formally, if $\operatorname{Con}_T$ is the sentence $\neg \operatorname{Prov}_T(\ulcorner 0 = 1 \urcorner)$ expressing "$T$ is consistent," then $T \not\vdash \operatorname{Con}_T$.

*Proof.* The proof builds on the construction used for the First Incompleteness Theorem.

**Step 1: Formalizing the First Incompleteness Theorem.** The entire proof of the First Incompleteness Theorem can be formalized within $T$ itself. In particular, the implication
$$\operatorname{Con}_T \to \neg \operatorname{Prov}_T(\ulcorner G \urcorner)$$
is provable in $T$, where $G$ is the Gödel sentence from the First Theorem. This formalization relies on the fact that the construction of $G$ and the reasoning about provability are finitary and can be carried out in $T$.

**Step 2: The fixed point yields provable equivalence.** Recall from the First Theorem that
$$T \vdash G \leftrightarrow \neg \operatorname{Prov}_T(\ulcorner G \urcorner).$$
Combining this with the formalized implication from Step 1, we obtain:
$$T \vdash \operatorname{Con}_T \to G.$$

**Step 3: Deriving the contradiction.** Suppose, for contradiction, that $T \vdash \operatorname{Con}_T$. Then by modus ponens, $T \vdash G$. But by the First Incompleteness Theorem, $T \not\vdash G$ (under the assumption that $T$ is consistent). This contradiction shows that $T \not\vdash \operatorname{Con}_T$.

**Step 4: The derivability conditions (Hilbert-Bernays-Löb).** The formalization in Step 1 requires that the provability predicate $\operatorname{Prov}_T$ satisfies three key derivability conditions (the Hilbert-Bernays-Löb conditions):

**(D1)** If $T \vdash P$, then $T \vdash \operatorname{Prov}_T(\ulcorner P \urcorner)$.

**(D2)** $T \vdash \operatorname{Prov}_T(\ulcorner P \to Q \urcorner) \to (\operatorname{Prov}_T(\ulcorner P \urcorner) \to \operatorname{Prov}_T(\ulcorner Q \urcorner))$.

**(D3)** $T \vdash \operatorname{Prov}_T(\ulcorner P \urcorner) \to \operatorname{Prov}_T(\ulcorner \operatorname{Prov}_T(\ulcorner P \urcorner) \urcorner)$.

These conditions are provable in theories like PA for the standard Gödel provability predicate, and they suffice to formalize the reasoning of the First Incompleteness Theorem within $T$.

Thus, any sufficiently strong, consistent theory cannot prove its own consistency. This result shows a fundamental limitation of the Hilbert program, which sought to prove the consistency of mathematics by finitary means within formal systems. $\square$
