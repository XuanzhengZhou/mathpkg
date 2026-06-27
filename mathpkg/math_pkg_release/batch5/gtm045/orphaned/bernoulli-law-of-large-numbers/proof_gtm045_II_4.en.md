---
role: proof
locale: en
of_concept: bernoulli-law-of-large-numbers
source_book: gtm045
source_chapter: "Introductory Part, II"
source_section: "4. Bernoulli case"
---
Upon applying the Tchebichev inequality, we have, as $n \to \infty$,

$$P\left[\left|\frac{S_n}{n} - p\right| \geq \epsilon\right] = P\left[|S_n - ES_n| \geq \epsilon n\right] \leq \frac{1}{\epsilon^2 n^2} \sigma^2 S_n = \frac{pq}{\epsilon^2 n} \to 0.$$

Here $ES_n = np$, $\sigma^2 S_n = npq$ (by the Bienaymé equality), and $q = 1-p$.
