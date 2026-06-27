---
role: proof
locale: en
of_concept: lemma-8d59923cd1
source_book: gtm077
source_chapter: "30"
source_section: "30"
---

# Proof of Each number $\alpha$ of the field, for which $\mathfrak{d}\alpha$ is integral can be represented in 

For the proof we consider the polynomial in $x$

$$G(x) = \sum_{i=1}^{n} \alpha^{(i)} \frac{F(x)}{x - \theta^{(i)}},$$

where

$$F(x) = \prod_{i=1}^{n} (x - \theta^{(i)}) = c_0 + c_1x + \cdots + c_{n-1}x^{n-1} + c_nx^n.$$

$G(x)$ is a polynomial with rational integral coefficients since

$$\frac{F(x)}{x - \theta} = \frac{F(x) - F(\theta)}{x - \theta} = \sum_{h=1}^{n} c_h \sum_{0 \leq r \leq h-1} x^r \theta^{h-r-1}$$

and hence

$$G(x) = \sum_{h=1}^{n} c_h \sum_{0 \leq r \leq h-1} x^r \sum_{i=1}^{n} \alpha^{(i)} \theta^{(i)h-r-1} = \sum_{h=1}^{n} c_h \sum_{0 \leq r \leq h-1} x^r S(\alpha \theta^{h-r-1}).$$

Since by hypothesis $\mathfrak{d}\alpha$ is integral, the traces $S(\alpha \theta^{h-r-1})$ are integers, and thus $G(x)$ has integral coefficients. Setting $x = \theta$ in (66) and noting that $F(\theta) = 0$, we get

$$G(\theta) = \alpha F'(\theta).$$

Therefore $\alpha = G(\theta)/F'(\theta)$, where $G(\theta)$ is in the ring $R(\theta)$, which proves the lemma.
