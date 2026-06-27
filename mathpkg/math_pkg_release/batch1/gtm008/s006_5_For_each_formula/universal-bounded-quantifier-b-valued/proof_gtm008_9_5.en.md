---
role: proof
locale: en
of_concept: universal-bounded-quantifier-b-valued
source_book: gtm008
source_chapter: "9"
source_section: "5"
---

The bounded universal quantifier is interpreted as:
$$\llbracket (\forall x \in a)\varphi(x) \rrbracket = \llbracket (\forall x)(x \in a \to \varphi(x)) \rrbracket = \prod_{x \in M} (\llbracket x \in a \rrbracket \Rightarrow \llbracket \varphi(x) \rrbracket).$$

Since $\llbracket x \in a \rrbracket = 0$ for $x \notin M_{\alpha}$ (as $a \in M_{\alpha}$ and all elements outside $M_{\alpha}$ have membership value $0$ in $a$), the product can be restricted to $x \in M_{\alpha}$, yielding the stated formula. The dual result for bounded existential quantifiers follows by duality.
