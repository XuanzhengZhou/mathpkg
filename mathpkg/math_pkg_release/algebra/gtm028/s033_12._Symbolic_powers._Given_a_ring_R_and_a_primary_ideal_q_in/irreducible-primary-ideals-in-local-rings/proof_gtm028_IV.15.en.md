---
role: proof
locale: en
of_concept: irreducible-primary-ideals-in-local-rings
source_book: gtm028
source_chapter: "IV"
source_section: "15"
---

**Proof that (1) implies (2):** If $\mathfrak{q}$ is irreducible, then in $R/\mathfrak{q}$ the zero ideal is irreducible. In a ring satisfying DCC (as $R/\mathfrak{q}$ does), an irreducible ideal is primary. Hence any two non-zero ideals in $R/\mathfrak{q}$ have non-zero intersection. If $(\mathfrak{q} : \mathfrak{m})/\mathfrak{q}$ had dimension $\geq 2$, it would contain two independent one-dimensional subspaces whose intersection would be zero mod $\mathfrak{q}$, contradicting irreducibility.

**Proof that (2) implies (3):** By Corollary 1 to Theorem 28 (§13), if $\mathfrak{a}$ is a minimal proper overideal of an ideal $\mathfrak{b}$, then $\mathfrak{a}\mathfrak{m} \subset \mathfrak{b}$. For any minimal proper overideal $\mathfrak{a}$ of $\mathfrak{q}$, we have $\mathfrak{a}\mathfrak{m} \subset \mathfrak{q}$, i.e., $\mathfrak{q} \subsetneq \mathfrak{a} \subset \mathfrak{q} : \mathfrak{m}$. If (2) holds, $\mathfrak{a} = \mathfrak{q} : \mathfrak{m}$ is the only minimal proper overideal, hence the smallest proper overideal.

**Proof that (3) implies (4):** Uses Lemma 1 and Lemma 2 below. Lemma 1: If (3) holds and $\mathfrak{a}$ is a minimal overideal of $\mathfrak{b}$ containing $\mathfrak{q}$, then $\mathfrak{q} : \mathfrak{b}$ is a minimal overideal of $\mathfrak{q} : \mathfrak{a}$ or equals it. Lemma 2: Using a composition series, the lengths satisfy $\lambda(\mathfrak{q} : \mathfrak{a}) = \lambda(\mathfrak{q}) - \lambda(\mathfrak{a})$. Then $\mathfrak{a} \subset \mathfrak{q} : (\mathfrak{q} : \mathfrak{a})$ and both have the same length, so they are equal.

**Proof that (4) implies (1):** If $\mathfrak{q} = \mathfrak{a} \cap \mathfrak{a}'$, write $\mathfrak{a} = \mathfrak{q} : \mathfrak{b}$, $\mathfrak{a}' = \mathfrak{q} : \mathfrak{b}'$. Then $\mathfrak{q} = (\mathfrak{q} : \mathfrak{b}) \cap (\mathfrak{q} : \mathfrak{b}') = \mathfrak{q} : (\mathfrak{b} + \mathfrak{b}')$. This forces $\mathfrak{b} + \mathfrak{b}' = R$. Since $\mathfrak{m}$ is the unique maximal ideal, either $\mathfrak{b} = R$ or $\mathfrak{b}' = R$, giving either $\mathfrak{a} = \mathfrak{q}$ or $\mathfrak{a}' = \mathfrak{q}$.
