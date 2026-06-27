---
role: proof
locale: en
of_concept: subfield-generated-by-subring
source_book: gtm030
source_chapter: "II"
source_section: "2"
---

Clearly $\mathfrak{G} \supseteq \{ab^{-1} \mid a, b \in \mathfrak{A}, b \neq 0\}$. We show the set $\{ab^{-1}\}$ is itself a subfield. Verify:
$$ab^{-1} + cd^{-1} = adb^{-1}d^{-1} + cbb^{-1}d^{-1} = (ad + cb)(bd)^{-1},$$
$$0 = 0b^{-1}, \quad -ab^{-1} = (-a)b^{-1},$$
$$(ab^{-1})(cd^{-1}) = acb^{-1}d^{-1} = (ac)(bd)^{-1},$$
$$1 = aa^{-1} \quad (a \neq 0),$$
$$(ab^{-1})^{-1} = a^{-1}b \quad (a \neq 0).$$

These formulas show the set $\{ab^{-1}\}$ is closed under addition, multiplication, contains 0, negatives, 1, and inverses — hence it is a subfield. Since any $a \in \mathfrak{A}$ can be written as $(ab)b^{-1}$, we have $\mathfrak{A} \subseteq \{ab^{-1}\}$. Since $\mathfrak{G}$ is the smallest subfield containing $\mathfrak{A}$, and $\{ab^{-1}\}$ is a subfield containing $\mathfrak{A}$ that is contained in $\mathfrak{G}$, we must have $\mathfrak{G} = \{ab^{-1}\}$.
