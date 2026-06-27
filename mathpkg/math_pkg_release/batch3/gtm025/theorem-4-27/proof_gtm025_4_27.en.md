---
role: proof
locale: en
of_concept: "theorem-4-27"
source_book: gtm025
source_chapter: "Unknown Chapter"
source_section: "4.27"
---

Let $A = \{0, 1\}^N$. Definition (4.23) shows that $\bar{A} = 2^{N_0}$. By (4.26), $$]0, 1[ = c.$$ Define $f$ on $A$ by $f(\varphi) = \sum_{n=1}^{\infty} \frac{\varphi(n)}{3^n}$. Then [see (5.40)] $f$ is a one-to-one mapping of $A$ into $[0, 1[$, and so $2^{N_0} \leq c.$ For each $x \in [0, 1[$ there is a unique representation of $x$ in the form

$$x = \sum_{n=1}^{\infty} \frac{x_n}{2^n}$$

where each $x_n$ is 0 or 1 and $x_n = 0$ for infinitely many $n \in N$: see (5.40). Define $g$ on $[0, 1[$ into $A$ by $g(x) = \varphi$ where $\varphi(n) = x

is a one-to-one function $f$ with $\text{dom}f = C$ and $\text{rng}f = C \times \{0, 1\}$. This proves that $\mathfrak{F} \neq \varnothing$. Partially order $\mathfrak{F}$ by $\subseteq$. According to the Hausdorff Maximality Principle (3.9), $\mathfrak{F}$ contains a maximal chain $\mathfrak{C}$. Let $g = \bigcup \mathfrak{C}$. It is easily checked that $g \in \mathfrak{F}$. Let $D = \text{dom}g$. The existence of the function $g$ shows that $\bar{D} = \bar{D} + \bar{D}$. Thus, to complete the proof, it suffices to show that $\bar{D} = a$. Let $E = A \cap D'$. If $E$ is finite, our Lemma (4.28) shows that $\bar{D} = \overline{D \cup E} = a$. If $E$ is infinite, let $G$ be a countably infinite subset of $E$. Let $f$ be any one-to-one mapping of $G$ onto $G \times \{0, 1\}$. Then $h = f \cup g \in \mathfrak{F}$ and $g \subseteq h$. This contradicts the maximality of $\mathfrak{C}$. Therefore $E$ is finite and $\bar{D} = a$.
