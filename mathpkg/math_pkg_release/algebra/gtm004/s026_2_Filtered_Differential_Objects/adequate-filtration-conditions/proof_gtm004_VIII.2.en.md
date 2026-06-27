---
role: proof
locale: en
of_concept: adequate-filtration-conditions
source_book: gtm004
source_chapter: "VIII. Spectral Sequences"
source_section: "2. Filtered Differential Objects"
---

# Proof of Adequate Filtration Conditions for Homology

**Statement.** Let $C \in (\mathfrak{A}, d, f)$ be a filtered differential object with filtration

$$\cdots \subseteq C^{(p-1)} \subseteq C^{(p)} \subseteq \cdots \subseteq C, \qquad -\infty < p < \infty.$$

Let $M = H(C)$ be the homology of $C$ and let

$$\cdots \subseteq M^{(p-1)} \subseteq M^{(p)} \subseteq \cdots \subseteq M$$

be the induced filtration, where $M^{(p)} = \operatorname{Im}\big(H(C^{(p)}) \rightarrow H(C)\big)$. In order that the associated graded quotients $M^{(p)}/M^{(p-1)}$ adequately represent $M$, the filtration must satisfy

$$\text{(i)} \quad \bigcap_{p} M^{(p)} = 0, \qquad \text{(ii)} \quad \bigcup_{p} M^{(p)} = M. \tag{2.8}$$

**Proof.** We argue informally in the language of concrete categories (abelian categories whose objects have underlying sets and whose morphisms are set maps), which suffices to exhibit the necessity of these conditions.

*Failure of (i).* Suppose $\bigcap_p M^{(p)} \neq 0$. Then there exists a non-zero element $x \in M$ such that $x \in M^{(p)}$ for every $p$. In the passage to the associated graded object

$$Gr(M) = \bigoplus_p M^{(p)}/M^{(p-1)},$$

the element $x$ projects to zero in every quotient $M^{(p)}/M^{(p-1)}$, because $x \in M^{(p-1)}$ for all $p$ implies $x \equiv 0 \pmod{M^{(p-1)}}$ in $M^{(p)}/M^{(p-1)}$. Hence $x$ is lost in $Gr(M)$: a non-zero element of $M$ is not detected by $Gr(M)$.

*Failure of (ii).* Suppose $\bigcup_p M^{(p)} \neq M$. Then there exists a non-zero element $x \in M$ such that $x \notin M^{(p)}$ for every $p$. Such an element never appears in any filtration step, hence its image cannot be represented in any homogeneous component $M^{(p)}/M^{(p-1)}$ of $Gr(M)$. Thus $x$ is unrepresented in $Gr(M)$.

*Conclusion.* If either condition fails, $Gr(M)$ cannot faithfully encode the elements of $M$. Therefore both conditions (i) and (ii) are necessary for the associated graded object to faithfully represent $M$. These conditions are added to the criterion for a "good" spectral sequence, namely that $Gr \circ H(C) = E_\infty$, and are often fulfilled when $\mathfrak{A}$ is itself a graded category (e.g., filtered chain complexes).
