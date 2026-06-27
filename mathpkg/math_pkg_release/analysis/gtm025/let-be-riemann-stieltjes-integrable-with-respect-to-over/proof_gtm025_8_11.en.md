---
role: proof
locale: en
of_concept: "let-be-riemann-stieltjes-integrable-with-respect-to-over"
source_book: gtm025
source_chapter: "Riemann-Stieltjes Integral"
source_section: "8.11"
---

Let $\varepsilon > 0$ be given. Choose $\Delta \in \mathcal{D}([a, b])$ such that

$$U(f, \alpha, \Delta) - L(f, \alpha, \Delta) < \varepsilon.$$

In view of (8.4) we may, and do, suppose that $c \in \Delta$; say

$$\Delta = \{a = t_0 < \cdots < t_m = c < t_{m+1} < \cdots < t_n = b\}.$$

Let

$$\Delta_1 = \{a = t_0 < \cdots < t_m = c\} \in \mathcal{D}([a, c])$$

and

$$\Delta_2 = \{c = t_m < \cdots < t_n = b\} \in \mathcal{D}([c, b]).$$

Then

$$(U(f, \alpha, \Delta_1) - L(f, \alpha, \Delta_1)) + (U(f, \alpha, \Delta_2) - L(f, \alpha, \Delta_2))$$

$$= U(f, \alpha, \Delta) - L(f, \alpha, \Delta) < \varepsilon.$$

It follows that $f$ is integrable over both $[a, c]$ and $[c, b]$. Let $S_{\alpha}(f; [a, c]) = \gamma_1$ and $S_{\alpha}(f; [c, b]) = \gamma_2$. Clearly $0 \leq U(f, \alpha, \Delta_1) - \gamma_1 < \varepsilon$ and $0 \leq U(f, \alpha, \Delta

(ii) $S_{\alpha}(cf) = cS_{\alpha}(f)$,
(iii) $S_{\alpha}(f) \geq 0$ if $f \in \mathfrak{C}_{00}^{+}(R)$.
This simple computation is left to the reader.
