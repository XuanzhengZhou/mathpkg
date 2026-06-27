---
role: proof
locale: en
of_concept: ext-classifies-extensions
source_book: gtm004
source_chapter: "III"
source_section: "2. The Functor Ext"
---

# Proof of Natural Equivalence between Ext and Extension Classes

We construct a natural equivalence of set-valued bifunctors $\eta : E(-, -) \to \operatorname{Ext}_\Lambda(-, -)$.

## Step 1: An isomorphism natural in $B$

Fix a projective presentation $R \xrightarrow{\mu} P \xrightarrow{\varepsilon} A$ of $A$. We first define an isomorphism of sets

$$
\eta : E(A, B) \to \operatorname{Ext}_\Lambda^\varepsilon(A, B),
$$

natural in $B$.

Given an extension $B \xrightarrow{\kappa} E \xrightarrow{\nu} A$ representing an element of $E(A, B)$, since $P$ is projective and $\nu$ is epic, there exists $\varphi : P \to E$ lifting $1_A$ (i.e., $\nu\varphi = \varepsilon$). Restricted to $R$, we obtain a map $\psi = \varphi\mu : R \to E$. Since $\nu\varphi\mu = \varepsilon\mu = 0$, $\psi$ factors uniquely through $\kappa : B \to E$ (by exactness), yielding $\psi' : R \to B$ with $\kappa\psi' = \psi = \varphi\mu$. Define

$$
\eta(E) = [\psi'] \in \operatorname{Ext}_\Lambda^\varepsilon(A, B) = \operatorname{coker}(\mu^* : \operatorname{Hom}_\Lambda(P, B) \to \operatorname{Hom}_\Lambda(R, B)).
$$

## Step 2: Inverse map

Define $\xi : \operatorname{Ext}_\Lambda^\varepsilon(A, B) \to E(A, B)$ as follows. Given a representative $\psi : R \to B$, form the push-out diagram

$$
\begin{CD}
R @>{\mu}>> P @>{\varepsilon}>> A \\
@V{\psi}VV @V{\varphi}VV @| \\
B @>{\kappa}>> E @>{\nu}>> A
\end{CD}
$$

By the dual of Lemma 1.2, the bottom row $B \xrightarrow{\kappa} E \xrightarrow{\nu} A$ is an extension. The equivalence class of this extension is independent of the representative $\psi$ chosen: if $\psi' = \psi + \tau\mu$ with $\tau : P \to B$, then $\varphi' = \varphi + \kappa\tau$ yields a commutative diagram, and by the dual of Lemma 1.3 the left-hand square is a push-out, giving the same extension class.

## Step 3: $\eta$ and $\xi$ are inverse

Using Lemma 1.3, one easily checks that $\eta \circ \xi = 1$ and $\xi \circ \eta = 1$. Thus we have an equivalence

$$
\eta : E(A, B) \rightsquigarrow \operatorname{Ext}_\Lambda^\varepsilon(A, B)
$$

natural in $B$.

## Step 4: Independence of projective presentation and naturality in $A$

Given $\alpha : A' \to A$, form the pull-back $E^\alpha$ of $E \to A$ and $A' \to A$. Since $P' \to E \to A$ and $P' \to A' \to A$ agree, they define a homomorphism $\varphi : P' \to E^\alpha$ into the pull-back. This induces $\psi : R' \to B$, and all faces of the resulting 3-dimensional diagram are commutative. This yields a commutative diagram

$$
\begin{CD}
E(A, B) @>{\alpha^*}>> E(A', B) \\
@V{\eta}V{\xi}V @V{\eta}V{\xi}V \\
\operatorname{Ext}_\Lambda^\varepsilon(A, B) @>{\alpha^*}>> \operatorname{Ext}_\Lambda^{\varepsilon'}(A', B)
\end{CD}
$$

For $A' = A$, $\alpha = 1_A$, this shows that $\eta$ is independent of the chosen projective presentation. In general, it shows that $\eta$ and $\xi$ are natural in $A$.

Therefore $\eta : E(-, -) \to \operatorname{Ext}_\Lambda(-, -)$ is a natural equivalence of set-valued bifunctors.
