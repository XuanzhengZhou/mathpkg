---
role: proof
locale: en
of_concept: self-reference-lemma
source_book: gtm053
source_chapter: "III"
source_section: "7"
---

Assume we have a fixed Godel numbering $N$ of formulas, and that the diagonal function is definable in the language. We denote by "$y = \operatorname{diag} x$" the formula expressing that $y$ is the Godel number of the diagonalization of the formula with Godel number $x$.

Given a formula $P(x)$ with one free variable, we construct:

$$R(x) : \exists y (\text{"$y = \operatorname{diag} x$"} \wedge P(y)).$$

Then we set

$$Q_P : \neg R(\overline{N}(\neg R(x))),$$

i.e., $Q_P$ is the diagonalization of $\neg R(x)$. By definition of the diagonal function, the Godel number of $Q_P$ is exactly $\operatorname{diag}(N(\neg R(x)))$.

Now we compute the truth condition:

$$Q_P \text{ is true} \iff \neg R(\overline{N}(\neg R(x))) \text{ is true}$$

$$\iff \text{the number } \operatorname{diag}(N(\neg R(x))) \text{ does not satisfy } R(x)$$

$$\iff \text{the number of } Q_P \text{ does not satisfy } R(x)$$

$$\iff \neg \exists y (\text{"$y = \operatorname{diag} \overline{N}(\neg R(x))$"} \wedge P(y)) \text{ is true}$$

$$\iff \neg P(\overline{N}(Q_P)) \text{ is true}$$

$$\iff P(\overline{N}(Q_P)) \text{ is false}.$$

Thus $Q_P$ is true if and only if $P(\overline{N}(Q_P))$ is false, as required. The lemma is proved.
