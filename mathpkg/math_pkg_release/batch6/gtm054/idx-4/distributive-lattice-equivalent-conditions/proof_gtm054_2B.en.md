---
role: proof
locale: en
of_concept: distributive-lattice-equivalent-conditions
source_book: gtm054
source_chapter: "II"
source_section: "B"
---

\textbf{(a) $\Rightarrow$ (b).} Assume (a) to hold and substitute $x \vee y$ for $x$ and $x$ for $y$, obtaining

$$[(x \vee y) \wedge x] \vee [(x \vee y) \wedge z] = (x \vee y) \wedge (x \vee z).$$

The left-hand member becomes

$$x \vee [(x \vee y) \wedge z], \quad \text{by B31b and c};$$

$$= x \vee [(x \wedge z) \vee (y \wedge z)], \quad \text{by assumption (a) (with $x$ and $z$ interchanged)};$$

$$= x \vee (y \wedge z), \quad \text{by B31b and c}.$$

\textbf{(b) $\Rightarrow$ (c).} Since $z \leq x \vee z$, B31d followed by our assumption (b) yields

$$(x \vee y) \wedge z \leq (x \vee y) \wedge (x \vee z) = x \vee (y \wedge z).$$

\textbf{(c) $\Rightarrow$ (a).} We need only prove that (c) implies the reverse inequality of B31f. With appropriate substitutions, two successive applications of assumption (c) yield

$$[(x \vee y) \wedge (x \vee z)] \leq x \vee [y \wedge (x \vee z)]$$

$$\leq x \vee [x \vee (y \wedge z)]$$

$$= x \vee (y \wedge z),$$

as required.
