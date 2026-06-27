---
role: proof
locale: en
of_concept: pullback-properties-lemma
source_book: gtm004
source_chapter: "III. Extensions of Modules"
source_section: "1. Extensions"
---

# Proof of Lemma 1.2: Properties of Pullback Diagrams

Recall the square (1.2):

\[
\begin{CD}
Y @>\alpha>> A \\
@V\beta VV @VV\varphi V \\
B @>>\psi> X
\end{CD}
\]

**Proof of (i).** Part (i) has been proved in complete generality in Theorem II.6.2. Indeed, if the square is a pullback, then $\beta$ maps the kernel of $\alpha$ into the kernel of $\psi$, inducing a homomorphism $\ker \alpha \to \ker \psi$.

**Proof of (ii).** Suppose $\psi$ is an epimorphism. By Lemma 1.1, the sequence

\[
0 \longrightarrow Y \xrightarrow{\{\alpha,\beta\}} A \oplus B \xrightarrow{\langle\varphi, -\psi\rangle} X
\]

is exact. Let $a \in A$. Since $\psi$ is epimorphic, there exists $b \in B$ with $\varphi a = \psi b$. Then

\[
\langle\varphi, -\psi\rangle(a, b) = \varphi a - \psi b = 0,
\]

so $(a, b) \in \ker \langle\varphi, -\psi\rangle = \operatorname{im} \{\alpha,\beta\}$ by exactness. Thus there exists $y \in Y$ with

\[
\{\alpha,\beta\}(y) = (\alpha y, \beta y) = (a, b),
\]

and in particular $\alpha y = a$. Hence $\alpha$ is epimorphic. $\square$
