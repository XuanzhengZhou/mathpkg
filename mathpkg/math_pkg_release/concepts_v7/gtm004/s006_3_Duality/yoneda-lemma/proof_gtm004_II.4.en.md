---
role: proof
locale: en
of_concept: yoneda-lemma
source_book: gtm004
source_chapter: "II"
source_section: "4"
---

# Proof of the Yoneda Lemma

Let $\tau : \mathfrak{C}(A, -) \to F$ be a natural transformation. We show first that $\tau$ is entirely determined by the element $\tau_A(1_A) \in F(A)$.

Let $\varphi : A \to B$ and consider the commutative diagram

$$\begin{array}{ccc}
\mathfrak{C}(A, A) & \xrightarrow{\varphi_*} & \mathfrak{C}(A, B) \\
\downarrow \tau_A & & \downarrow \tau_B \\
FA & \xrightarrow{F\varphi} & FB
\end{array}$$

where $\varphi_*(\alpha) = \varphi \circ \alpha$. Then

$$\tau_B(\varphi) = \tau_B(\varphi_*(1_A)) = (F\varphi)(\tau_A(1_A)),$$

proving the assertion. The proposition is therefore established if we show that, for any $\kappa \in FA$, the rule

$$\tau_B(\varphi) = (F\varphi)(\kappa), \quad \varphi \in \mathfrak{C}(A, B), \tag{4.1}$$

does define a natural transformation from $\mathfrak{C}(A, -)$ to $F$.

Let $\theta : B_1 \to B_2$ and consider the diagram

$$\begin{array}{ccc}
\mathfrak{C}(A, B_1) & \xrightarrow{\theta_*} & \mathfrak{C}(A, B_2) \\
\downarrow \tau_{B_1} & & \downarrow \tau_{B_2} \\
FB_1 & \xrightarrow{F\theta} & FB_2
\end{array}$$

We must show that this diagram commutes if $\tau_{B_1}, \tau_{B_2}$ are defined as in (4.1). For $\varphi : A \to B_1$,

$$(\tau_{B_2}) \theta_*(\varphi) = \tau_{B_2}(\theta \varphi) = F(\theta \varphi)(\kappa) = F(\theta) F(\varphi)(\kappa) = F(\theta) \tau_{B_1}(\varphi).$$

Thus the diagram commutes and the proposition is completely proved.

The correspondence $\tau \mapsto \tau_A(1_A)$ establishes a bijection between natural transformations $\mathfrak{C}(A, -) \to F$ and elements of $FA$.
