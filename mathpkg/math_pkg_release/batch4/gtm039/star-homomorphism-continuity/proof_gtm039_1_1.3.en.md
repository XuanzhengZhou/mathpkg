---
role: proof
locale: en
of_concept: "star-homomorphism-continuity"
source_book: gtm039
source_chapter: "1"
source_section: "1.3"
---
First assume $A$ and $B$ are unital and $\pi(e_A) = e_B$. For $x = x^*$, $\|\pi(x)\| = r(\pi(x)) \leqslant r(x) \leqslant \|x\|$ by the spectral radius formula. If $\|\pi(x)\| < \|x\|$, there exists $\lambda \in \text{sp}(x)$ with $|\lambda| = \|x\|$ and $f \in C(\text{sp}(x))$ with $f(\lambda) \neq 0$ but $f|_{\text{sp}(\pi(x))} = 0$. By the functional calculus, $\pi(f(x)) = f(\pi(x)) = 0$, but $f(x) \neq 0$, contradicting injectivity of the reduced map $\dot{\pi}$. Hence $\|\pi(x)\| = \|x\|$. For non-injective $\pi$, apply the above to $\dot{\pi}: A/\ker\pi \to \pi(A)$. General case reduces to unital by adjoining identities. $\square$
