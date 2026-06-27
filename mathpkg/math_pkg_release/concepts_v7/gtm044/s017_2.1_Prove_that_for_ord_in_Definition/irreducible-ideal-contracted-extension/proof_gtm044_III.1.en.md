---
role: proof
locale: en
of_concept: irreducible-ideal-contracted-extension
source_book: gtm044
source_chapter: "III"
source_section: "1"
---

# Proof of Irreducible Ideals Contained in $\mathfrak{p}$ Satisfy $\mathfrak{q} = \mathfrak{q}^{ec}$

**Theorem 3.10.** Let $R$ and $\mathfrak{p}$ be as above. Then $\mathfrak{q} = \mathfrak{q}^{ec}$ for any irreducible (primary) ideal $\mathfrak{q} \subset \mathfrak{p}$.

*Proof.* Recall from (11) the characterization of the contracted extension:

$$\mathfrak{a}^{ec} = \{\, a \in R \mid am \in \mathfrak{a} \text{ for some } m \in R \setminus \mathfrak{p} \,\}.$$

The inclusion $\mathfrak{q} \subset \mathfrak{q}^{ec}$ always holds: if $a \in \mathfrak{q}$, then $a = a \cdot 1/1$ is an element of $\mathfrak{q}^e$ and also lies in $R$, hence $a \in \mathfrak{q}^{ec}$.

For the reverse inclusion $\mathfrak{q}^{ec} \subset \mathfrak{q}$, let $a \in \mathfrak{q}^{ec}$. Then there exists $m \in R \setminus \mathfrak{p}$ such that $am \in \mathfrak{q}$. Since $\mathfrak{q}$ is irreducible (in a Noetherian ring, irreducible ideals are primary), $\mathfrak{q}$ has a prime radical $\operatorname{rad}(\mathfrak{q})$. Since $\mathfrak{q} \subset \mathfrak{p}$ and $\mathfrak{p}$ is prime, we have $\operatorname{rad}(\mathfrak{q}) \subset \mathfrak{p}$. Therefore $m \notin \mathfrak{p}$ implies $m \notin \operatorname{rad}(\mathfrak{q})$.

Now, $\mathfrak{q}$ being primary means: if $xy \in \mathfrak{q}$ and $x \notin \operatorname{rad}(\mathfrak{q})$, then $y \in \mathfrak{q}$. Applying this with $x = m$ (which is not in $\operatorname{rad}(\mathfrak{q})$) and $y = a$, we have $am \in \mathfrak{q}$ and $m \notin \operatorname{rad}(\mathfrak{q})$, hence $a \in \mathfrak{q}$. Thus $\mathfrak{q}^{ec} \subset \mathfrak{q}$.

Combining both inclusions yields $\mathfrak{q} = \mathfrak{q}^{ec}$. $\square$
