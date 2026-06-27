---
role: proof
locale: en
of_concept: phragmen-lindelof-theorem
source_book: gtm011
source_chapter: "VI"
source_section: "§4"
---

Let $|\varphi(z)| \leq \kappa$ for all $z \in G$. Since $G$ is simply connected, there exists an analytic branch of $\log \varphi(z)$ on $G$ (Corollary IV.6.17). Hence $g(z) = \exp(\eta \log \varphi(z))$ is an analytic branch of $\varphi(z)^\eta$ for $\eta > 0$, and $|g(z)| = |\varphi(z)|^\eta$.

Define $F: G \to \mathbb{C}$ by
\[
F(z) = f(z) g(z) \kappa^{-\eta}.
\]
Then $F$ is analytic on $G$ and $|F(z)| \leq |f(z)|$ since $|\varphi(z)| \leq \kappa$ for all $z \in G$.

Now examine the behavior of $F$ on $\partial_\infty G = A \cup B$. For $a \in A$, condition (a) gives
\[
\limsup_{z \to a} |F(z)| = \kappa^{-\eta} \limsup_{z \to a} |f(z)| |\varphi(z)|^\eta \leq \kappa^{-\eta} \kappa^\eta \limsup_{z \to a} |f(z)| \leq M.
\]
For $b \in B$, condition (b) gives
\[
\limsup_{z \to b} |F(z)| = \kappa^{-\eta} \limsup_{z \to b} |f(z)| |\varphi(z)|^\eta \leq \kappa^{-\eta} M.
\]

Thus $F$ satisfies the hypothesis of Theorem 1.4 (Maximum Modulus Theorem — Third Version), so
\[
|F(z)| \leq \max(M, \kappa^{-\eta} M) \quad \text{for all } z \in G.
\]

This yields
\[
|f(z)| \leq \left| \frac{\kappa}{\varphi(z)} \right|^\eta \max(M, \kappa^{-\eta} M)
\]
for all $z \in G$ and all $\eta > 0$. Letting $\eta \to 0$ gives $|f(z)| \leq M$ for all $z \in G$.
