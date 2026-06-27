---
role: proof
locale: en
of_concept: irreducible-closed-ideal-is-prime
source_book: gtm044
source_chapter: "4"
source_section: "4.8"
---

# Proof of Every Irreducible Closed Ideal is Prime

**Lemma 4.8.** Every irreducible closed ideal in $\mathbb{C}[X_1, \ldots, X_n]$ is prime.

**Proof.** Let $\mathfrak{c}$ be an irreducible and closed ideal in $\mathbb{C}[X_1, \ldots, X_n]$, and suppose it is not prime. Then there exist $a_1, a_2 \in \mathbb{C}[X_1, \ldots, X_n] \setminus \mathfrak{c}$ such that $a_1 \cdot a_2 \in \mathfrak{c}$.

Define $\mathfrak{c}_1 = \mathfrak{c} + (a_1)$ and $\mathfrak{c}_2 = \mathfrak{c} + (a_2)$. Since $a_1, a_2 \notin \mathfrak{c}$, both $\mathfrak{c}_1$ and $\mathfrak{c}_2$ are strictly larger than $\mathfrak{c}$.

Since $\mathfrak{c}$ is closed, $\mathfrak{c} = \mathcal{J}(V)$ for some variety $V = \mathcal{V}(\mathfrak{c})$. Under the ideal-variety correspondence, let $\mathfrak{c}_1 \rightarrow V_1$ and $\mathfrak{c}_2 \rightarrow V_2$. Because $\mathfrak{c}_1 \supsetneq \mathfrak{c}$ and $\mathfrak{c}_2 \supsetneq \mathfrak{c}$, the inclusion-reversing nature of $\mathcal{V}$ yields

$$V_1 \subsetneq V, \qquad V_2 \subsetneq V.$$

Now we claim that $V = V_1 \cup V_2$. Indeed, take any point $P \in V$. Since $a_1 a_2 \in \mathfrak{c} = \mathcal{J}(V)$, the product $a_1 a_2$ vanishes on all of $V$, so in particular $a_1(P) a_2(P) = 0$. Hence either $a_1(P) = 0$ or $a_2(P) = 0$.

- If $a_1(P) = 0$, then every polynomial in $\mathfrak{c}_1 = \mathfrak{c} + (a_1)$ vanishes at $P$ (elements of $\mathfrak{c}$ vanish on $V$, and $a_1(P) = 0$), so $P \in V_1$.
- If $a_2(P) = 0$, then similarly $P \in V_2$.

Thus $V \subseteq V_1 \cup V_2$. The reverse inclusion $V_1 \cup V_2 \subseteq V$ follows from $\mathfrak{c}_1, \mathfrak{c}_2 \supseteq \mathfrak{c}$, which implies $V_1, V_2 \subseteq V$.

We have therefore written $V$ as a union of two proper subsets: $V = V_1 \cup V_2$ with $V_1 \subsetneq V$ and $V_2 \subsetneq V$. This contradicts the hypothesis that $\mathfrak{c}$ is irreducible, for an irreducible closed ideal corresponds (via the ideal-variety correspondence) to an irreducible variety. Since $\mathfrak{c}$ is irreducible, $V$ must be irreducible under Definition 4.3, meaning it cannot be expressed as the union of two properly contained subvarieties.

The contradiction shows that our assumption was false; hence $\mathfrak{c}$ must be prime. $\square$

**Remark.** This lemma is actually valid in the general "$S, k, R$" setting of Section 2 of the book. The converse — that every prime ideal is an irreducible closed ideal — is established later (Theorem 5.11 and Corollary 5.9 together), showing that in $\mathbb{C}[X_1, \ldots, X_n]$, the irreducible closed ideals are precisely the prime ideals.
