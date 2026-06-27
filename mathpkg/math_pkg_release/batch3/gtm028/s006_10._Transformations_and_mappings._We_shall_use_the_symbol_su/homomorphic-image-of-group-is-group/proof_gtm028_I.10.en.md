---
role: proof
locale: en
of_concept: homomorphic-image-of-group-is-group
source_book: gtm028
source_chapter: "I"
source_section: "10. Transformations and mappings"
---

**Proof.** We first prove the associative law in $\bar{G}$. Let $\bar{a}, \bar{b}, \bar{c}$ be arbitrary elements of $\bar{G}$; they are images of certain elements $a, b, c$ of $G$, since $T$ maps $G$ onto $\bar{G}$. We have $(ab)c = a(bc)$. We have

$$[(ab)c]T = [(ab)T]cT = [(aT)(bT)]cT = (\bar{a}\bar{b})\bar{c}.$$

In a similar fashion we find that $[a(bc)]T = \bar{a}(\bar{b}\bar{c})$, and hence $(\bar{a}\bar{b})\bar{c} = \bar{a}(\bar{b}\bar{c})$. One shows then, as in the proof of Theorem 1, that $\bar{G}$ has an identity, namely, $eT$, where $e$ is the identity of $G$, and that every element $\bar{a}$ of $\bar{G}$ has an inverse, namely, if $\bar{a} = aT$, then $\bar{a}^{-1} = (a^{-1})T$. Thus $\bar{G}$ is a group. The second assertion of the lemma is obvious.
