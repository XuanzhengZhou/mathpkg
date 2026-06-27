---
role: proof
locale: en
of_concept: equivalent-conditions-for-dense-c-embedded
source_book: gtm043
source_chapter: "8"
source_section: "8.6"
---

We notice that each of the conditions listed here is stronger than the corresponding condition in Theorems 6.4 and 6.7. Therefore, if $T$ satisfies any one of the present conditions, then
$$X \subset T \subset \beta X, \quad \text{and} \quad \beta T = \beta X.$$

The pattern of proof is $(1) \to (2) \to (7) \to (5) \to (4) \to (3) \to (6) \to (1)$.

$(1) \implies (2)$: Since $\mathbb{R}$ is realcompact, (2) is just a special case of (1).

$(2) \implies (7)$: The hypothesis implies that $X$ is $C$-embedded in $vT$; therefore $vT \subset vX$, by (a) of Corollary 8.5, and $vT \supset vX$, by (b).

$(7) \implies (5)$: By definition (8.4), if $p \in vX$, then $A^p$, which is the unique $z$-ultrafilter converging to $p$ (6.6(a)), is real.

$(5) \implies (4)$: Evidently, the left member in (4) is contained in the right member. For the reverse inclusion, let $p \in \bigcap_n \mathrm{cl}_T Z_n$. The $z$-ultrafilter $A^p$ on $X$ converging to $p$ contains each $Z_n$, hence the family $\{Z_n\}$ has the countable intersection property with respect to $A^p$. Since $A^p$ is real, it has the countable intersection property, so $\bigcap_n Z_n \neq \emptyset$. Therefore $p \in \mathrm{cl}_T \bigcap_n Z_n$.

$(4) \implies (3)$: Immediate.

$(3) \implies (6)$: By Theorem 6.7, $X \subset T \subset \beta X$. Condition (3) implies that for each $p \in T$, $A^p$ has the countable intersection property, so $p \in vX$.

$(6) \implies (1)$: Since $vX \subset \beta X$, the Stone extension $\bar{\tau}: \beta X \to \beta Y$ restricts to a mapping $T \to \beta Y$. Because $Y$ is realcompact, $\bar{\tau}(vX) \subset Y$, and since $T \subset vX$, the restriction $\bar{\tau}|T$ maps $T$ into $Y$, giving the required extension.

This completes the proof of the theorem. An alternative proof that (2) implies (1) will be given in Theorem 10.7. Proofs of other implications are indicated in 8D.
