---
role: proof
locale: en
of_concept: rational-substitution-formula
source_book: gtm015
source_chapter: "54"
source_section: "54.7"
---

# Proof of Rational substitution formula

Assume now that $g$ is not a constant. Let us regard $g \in \mathbb{C}(t; \sigma(x))$ as fixed and $f \in \mathbb{C}(t; \sigma(g(x)))$ as variable. We have shown that $f \circ g \in \mathbb{C}(t; \sigma(x))$ for all such $f$. We may therefore define a mapping

$$\Phi: \mathbb{C}(t; \sigma(g(x))) \rightarrow A$$

by the formula $\Phi(f) = (f \circ g)(x)$. Since $1 \circ g = 1$ and $t \circ g = g$, we have $\Phi(1) = 1$ and $\Phi(t) = g(x)$. Moreover, $\Phi$ is an algebra homomorphism; indeed, it is clear from (54.7) and (54.1) that $\Phi$ is the composite of two homomorphisms,

$$f \mapsto f \circ g \mapsto (f \circ g)(x)$$

(note that $\mathbb{C}(t; \sigma(g(x))) \subset \mathbb{C}(t) = \text{the domain of } \Phi_g$). These properties of $\Phi$ are characteristic of $\Phi_{g(x)}$; thus, for all $f \in \mathbb{C}(t; \sigma(g(x)))$, we have

$$\Phi_{g(x)}(f) = \Phi(f),$$

that is, $f(g(x)) = (f \circ g)(x)$.
