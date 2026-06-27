---
role: proof
locale: en
of_concept: free-module-universal-characterization
source_book: gtm004
source_chapter: "I. Modules"
source_section: "4. Free and Projective Modules"
---

# Proof of Universal Characterization of the Free Module

Let $f(s) = m_s$. Every element $a \in P$ can be written uniquely as $a = \sum_{s \in S} \lambda_s s$ with $\lambda_s \in \Lambda$ and $\lambda_s \neq 0$ for only finitely many $s \in S$. Define

$$\varphi(a) = \varphi\left(\sum_{s \in S} \lambda_s s\right) = \sum_{s \in S} \lambda_s m_s.$$

This defines a $\Lambda$-module homomorphism $\varphi : P \to M$, and for $s \in S$, $\varphi(s) = m_s = f(s)$, so $\varphi$ extends $f$.

To prove uniqueness, suppose $\psi : P \to M$ is another homomorphism extending $f$. Then for any $a = \sum_{s \in S} \lambda_s s \in P$,

$$\psi(a) = \psi\left(\sum_{s \in S} \lambda_s s\right) = \sum_{s \in S} \lambda_s \psi(s) = \sum_{s \in S} \lambda_s f(s) = \sum_{s \in S} \lambda_s m_s = \varphi(a).$$

Hence $\psi = \varphi$, so $\varphi$ is the unique homomorphism having the required property.
