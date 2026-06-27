---
role: proof
locale: en
of_concept: infa-wedge-clr-1-a-wedge-cdots-wedge-clr-m-a-wedge-cl-2s-1-a-wedge-cdots-wedge-c
source_book: gtm001
source_chapter: "11"
source_section: ""
---

The proof proceeds as for Proposition 9.6. We then note that since $R_i$ and $S_i$ are single valued

$$\overline{R_i} \overline{f'k} \leq \overline{f'k} \quad i = 1, \ldots, m$$

$$\overline{S_i} \overline{(f'k)^2} \leq \overline{(f'k)^2} = \overline{f'k}, \quad i = 1, \ldots, n.$$

Therefore $f'(k+1)$ is the union of a finite number of sets each of cardinality not greater than $\overline{f'k}$. Then by *Proposition 10.41

$$\overline{f'(k+1)} = \overline{f'k} = \cdots = \overline{f'0} = \bar{a}.$$

Then from *Proposition 10.48, and the fact that $a$ is infinite

$$\bar{b} \leq \overline{a \times \omega} = \bar{a}.$$

Furthermore since

We turn now to the very interesting subject of models of set theory. Intuitively by a model of set theory we mean a system in which the axioms and theorems of ZF are true. Such a system must consist of a domain of objects that we interpret as the universe $V$ of our theory and a binary relation that we interpret as the $\epsilon$-relation of our theory.

Assuming consistency there is a model of ZF consisting of a universe of “sets” $V$ on which there is defined an “$\epsilon$-relation.” Given such a universe $V$ it is possible that some subclass $A$ of $V$ together with some relation $R$ on $A$ is also a model of ZF. With $A \subseteq V$ and $R \subseteq A \times A$ the language of ZF is adequate for the development of a theory of such internal models. Our next objective is to make the foregoing ideas precise and thereby compel ZF to tell us about some of its models.

In order to define “model” we first introduce the idea of a structure or relational system. For each nonempty class $A$ and each relation $R \subseteq A \times A$ we introduce the term

$$[A, R]$$

which we call a structure (or relational system); $A$ is the universe of this structure and the elements of $A$ we call individuals.

We next define “the structure $[A, R]$ satisfies the wff $\varphi$.” Our definition is by induction on the number of logical symbols in $\varphi$. For this purpose we assume $\neg$, $\wedge$, and $\forall$ as primitive.
