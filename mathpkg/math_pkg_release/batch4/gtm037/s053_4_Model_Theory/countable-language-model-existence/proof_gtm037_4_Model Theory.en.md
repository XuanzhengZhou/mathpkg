---
role: proof
locale: en
of_concept: countable-language-model-existence
source_book: gtm037
source_chapter: "4"
source_section: "Model Theory"
---

In the proof of Theorem 18.9, the induction hypothesis

$$\left| \{c \in C : c \text{ occurs in some } \varphi \in \Theta_\alpha\} \right| \leq \left| \{c \in C : c \text{ occurs in some } \varphi \in \Gamma\} \right| + |\alpha| + \aleph_0$$

is used to ensure that the construction never requires more new constants than are available. When $|\text{Fmla}_\mathcal{L}| = \aleph_0$, the set $C$ of new constants can be taken to be countably infinite, and at each stage $\alpha < \aleph_0$ only finitely many new constants have been introduced. Since there are only countably many stages, the total number of constants ever used remains countable. Thus the induction hypothesis (labeled condition (0) in the proof) is automatically satisfied without invoking condition (C11). All other steps of the proof proceed unchanged.
