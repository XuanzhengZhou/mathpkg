---
role: proof
locale: en
of_concept: measure-preserving-s-and-t
source_book: gtm018
source_chapter: "XI"
source_section: "59. Measurable Groups"
---

To show that $S$ is measure preserving, we use Fubini's theorem and the translation invariance of $\mu$ and $\nu$. For any measurable set $E \subseteq X \times X$, we have

$$(\mu \times \nu)(S(E)) = \int \nu((S(E))_x) \, d\mu(x).$$

By Theorem A, $(S(E))_x = xE_x$. Since $\nu$ is invariant under left translations (property (c) of a measurable group), we have $\nu(xE_x) = \nu(E_x)$. Therefore

$$(\mu \times \nu)(S(E)) = \int \nu(E_x) \, d\mu(x) = (\mu \times \nu)(E).$$

This establishes the measure preserving character of $S$.

The result for $T$ follows similarly by considering the sections $(T(E))^y$. By Theorem A, $(T(E))^y = yE^y$, and by the left translation invariance of $\mu$, we have $\mu(yE^y) = \mu(E^y)$. Hence

$$(\mu \times \nu)(T(E)) = \int \mu((T(E))^y) \, d\nu(y) = \int \mu(E^y) \, d\nu(y) = (\mu \times \nu)(E),$$

which shows that $T$ is also measure preserving.
