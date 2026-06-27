---
role: proof
locale: en
of_concept: "let-be-any-ordinal-number-and-let-denote"
source_book: gtm025
source_chapter: "Unknown Chapter"
source_section: "4.47"
---

Let $\beta \in P_\alpha$ and let $A$ and

Clearly $\alpha \leq \beta$ for each $\alpha \in C$ for otherwise $\beta \in D$. This proves (iv).

(4.50) Remark. The cardinal number of the set $P_O$ is denoted $\aleph_1$. The continuum hypothesis is the assertion that $\aleph_1 = c$. This is equivalent to the assertion that each infinite subset of $R$ is either countable or of cardinal number $c$. Many interesting and important theorems have been proved with the aid of this hypothesis. It was recently shown by Paul J. Cohen [loc. cit. (3.2)] that the continuum hypothesis is independent of the Zermelo-Fraenkel axioms of set theory.

(4.51) Exercise. Prove that every nonvoid set of cardinal numbers has a smallest member.

(4.52) Exercise. Let $A$ be an infinite linearly ordered set. Suppose that no infinite subset of $A$ has a largest element. Prove that ord $A = \omega$. [Recall that $\omega = \text{ord} N$.]

(4.53) Exercise. Let $A$ be a linearly ordered set such that:
(i) $A$ is countably infinite;
(ii) $A$ has no first or last element;
(iii) $x, y \in A$, $x < y$ imply that there is a $z \in A$ such that $x < z < y$. Prove that ord $A = \eta$. [Recall that $\eta = \text{ord} Q$.]

(4.54) Exercise. Prove that there are uncountably many different ways to well order the set $N$ such that no two of these different well-ordered sets are order isomorphic.

(4.55) Exercise. Let $A$ be any infinite set. Prove that $A$ can be well ordered in such a way that it has no last element. Also show that there is a well-ordering of $A$ in which there is a last element.

(4.56) Exercise. A permutation of a set $A$ is any one-to-one mapping of $A$ onto $A$. Let $A$ be a set such that $\bar{A} > 1$.

(a) Prove that there exists

functions $f$ such that:

(1) $\text{dom}f \subset A$;
(2) $\text{rng}f \subset B$;
(3) $(\text{rng}f) \cup [A \cap (\text{dom}f)']$ is linearly independent over $F$.

The fact that $A$ is linearly independent shows that the empty function $\varnothing$ is an element of $\mathfrak{B}$. Thus $\mathfrak{B} \neq \varnothing$. Partially order $\mathfrak{B}$ by inclusion. To show that Zorn's lemma applies to $\mathfrak{B}$, let $\mathfrak{C}$ be any nonvoid chain contained in $\mathfrak{B}$ and let $g = \cup \mathfrak{C}$. An application of (2.19) shows that $g$ is a function and that (1) and (2) hold for the function $g$. One easily sees that $g$ is one-to-one. We have

$(\text{rng}g) \cup [A \cap (\text{dom}g)'] = (\bigcup_{f \in \mathfrak{C}} \text{rng}f) \cup [A \cap (\bigcup_{f \in \mathfrak{C}} \text{dom}f)']$. (4)

Now let $F$ be any finite subset of the set in (4). Since $\{\text{rng}f : f \in \mathfrak{C}\}$ is a chain under inclusion, there is a function $f_0 \in \mathfrak{C}$ such that

$$F \subset (\text{rng}f_0) \cup [A \cap (\bigcup_{f \in \mathfrak{C}} \text{dom}f)']$$

$$\subset (\text{rng}f_0) \cup [A \cap (\text{dom}f_0)'].$$

Therefore $F$ is linearly independent, and so $g$ satisfies condition (3). Thus $g$ is in $\mathfrak{B}$, and $g$ is an upper bound for $\mathfrak{C}$. By Zorn's lemma

(4.60) Exercise. Let $X$ be a vector space over a field $F$ and let $B$ be a Hamel basis for this space. Prove that:
(a) $\bar{X} = \max\{\bar{B}, \bar{F}\}$ if $B$ is infinite;
(b) $\bar{X} = \bar{F}^{\bar{B}}$ if $B$ is finite.

(4.61) Exercise. Without using the continuum hypothesis, find the algebraic dimension of the vector space $R$ over the field $Q$.

(4.62) Exercise [proposed by M. Hewitt]. Let $A$ be a nonvoid set. Suppose that there is a family $\mathcal{S}$ of subsets of $A$ with the following properties:
(i) $\bar{B} = 3$ for all $B \in \mathcal{S}$;
(ii) $\bigcup \mathcal{S} = A$;
(iii) $\overline{B_1 \cap B_2} = 1$ for distinct $B_1, B_2 \in \mathcal{S}$;
(iv) if $x, y \in A$ and $x \neq y$, then there is exactly one $B \in \mathcal{S}$ containing $\{x, y\}$.

Prove that such an $\mathcal{S}$ exists if and only if $\bar{A} = 3$ or $\bar{A} = 7$.

§ 5. Construction of the real and complex number fields

We give in this section a short and reasonably sophisticated construction of the real and complex numbers, assuming the rational numbers as known. It seems appropriate to do this, since completeness of the real number field is the rock on which elementary analysis rests. Also there is a strong interplay between algebra and contemporary analysis, which demands the use of the ideas and methods of algebra in analysis. We begin with a few facts about groups and other algebraic structures.
