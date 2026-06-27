---
role: proof
locale: en
of_concept: irreducible-ideal-noetherian-primary
source_book: gtm030
source_chapter: "VI"
source_section: "7. Representation of an ideal as intersection of primary ideals"
---

Suppose $\mathfrak{B}$ is not primary. Then there exist elements $c, d \in \mathfrak{A}$ such that $cd \equiv 0 \pmod{\mathfrak{B}}$, $c \not\equiv 0 \pmod{\mathfrak{B}}$, and no power of $d$ is congruent to $0$ modulo $\mathfrak{B}$. Consider the ascending chain of ideals
$$\mathfrak{B} : (d) \subseteq \mathfrak{B} : (d^2) \subseteq \mathfrak{B} : (d^3) \subseteq \cdots$$
Since $\mathfrak{A}$ is Noetherian, this chain stabilizes: there exists a positive integer $r$ such that
$$\mathfrak{B} : (d^r) = \mathfrak{B} : (d^{r+1}) = \cdots.$$

We claim that
$$\mathfrak{B} = (\mathfrak{B} : (d^r)) \cap (\mathfrak{B} + (d^{r+1})).$$

Let $u \in (\mathfrak{B} + (d^{r+1})) \cap (\mathfrak{B} : (d^r))$. Then $u = b + md^{r+1} + cd^{r+1}$ where $b \in \mathfrak{B}$, $m \in I$, $c \in \mathfrak{A}$. Since $u \in \mathfrak{B} : (d^r)$, we have $ud^r \equiv 0 \pmod{\mathfrak{B}}$, so
$$bd^r + md^{2r+1} + cd^{2r+1} \equiv 0 \pmod{\mathfrak{B}}.$$
This gives $(md + cd)d^{2r} \equiv 0 \pmod{\mathfrak{B}}$, so $md + cd \in \mathfrak{B} : (d^{2r}) = \mathfrak{B} : (d^r)$. Hence $(md + cd)d^r \equiv 0 \pmod{\mathfrak{B}}$, i.e., $md^{r+1} + cd^{r+1} \equiv 0 \pmod{\mathfrak{B}}$. Therefore $u = b + (md^{r+1} + cd^{r+1}) \in \mathfrak{B}$.

Both ideals on the right side of the intersection properly contain $\mathfrak{B}$ (since $c \not\equiv 0 \pmod{\mathfrak{B}}$ implies $\mathfrak{B} : (d^r) \supset \mathfrak{B}$, and $d^{r+1} \notin \mathfrak{B}$ implies $\mathfrak{B} + (d^{r+1}) \supset \mathfrak{B}$). Hence $\mathfrak{B}$ is reducible. The contrapositive is the theorem: every irreducible ideal is primary.
