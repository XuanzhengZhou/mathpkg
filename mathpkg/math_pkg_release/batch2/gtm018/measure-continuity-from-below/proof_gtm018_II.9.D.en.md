---
role: proof
locale: en
of_concept: measure-continuity-from-below
source_book: gtm018
source_chapter: "II"
source_section: "9"
---

If we write $E_0 = 0$, then

$$\mu(\lim_n E_n) = \mu(\bigcup_{i=1}^{\infty} E_i) = \mu(\bigcup_{i=1}^{\infty}(E_i - E_{i-1})) =$$

$$= \sum_{i=1}^{\infty} \mu(E_i - E_{i-1}) = \lim_n \sum_{i=1}^{n} \mu(E_i - E_{i-1}) =$$

$$= \lim_n \mu(\bigcup_{i=1}^{n}(E_i - E_{i-1})) = \lim_n \mu(E_n).$$
