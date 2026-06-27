---
role: proof
locale: en
of_concept: long-exact-homology-sequence
source_book: gtm004
source_chapter: "IV"
source_section: "2. The Long Exact (Co)Homology Sequence"
---

# Proof of Long Exact Homology Sequence

*Proof of Theorem 2.1.* We give the proof for chain complexes only, the proof for cochain complexes being analogous.

Let $A \xrightarrow{\varphi} B \xrightarrow{\psi} C$ be a short exact sequence of chain complexes, so that for each $n \in \mathbb{Z}$ the sequence
$$0 \to A_n \xrightarrow{\varphi_n} B_n \xrightarrow{\psi_n} C_n \to 0$$
is exact. We first look at the diagram

$$
\begin{array}{cccccc}
& 0 & 0 & 0 & \\
& \downarrow & \downarrow & \downarrow & \\
0 \longrightarrow & \ker \partial_n^A & \longrightarrow & \ker \partial_n^B & \longrightarrow & \ker \partial_n^C \\
& \downarrow & & \downarrow & & \downarrow \\
& A_n & \xrightarrow{\varphi_n} & B_n & \xrightarrow{\psi_n} & C_n & \longrightarrow 0 \\
& \downarrow \partial_n^A & & \downarrow \partial_n^B & & \downarrow \partial_n^C \\
0 \longrightarrow & A_{n-1} & \xrightarrow{\varphi_{n-1}} & B_{n-1} & \xrightarrow{\psi_{n-1}} & C_{n-1} \\
& \downarrow & & \downarrow & & \downarrow \\
& \operatorname{coker} \partial_n^A & \longrightarrow & \operatorname{coker} \partial_n^B & \longrightarrow & \operatorname{coker} \partial_n^C & \longrightarrow 0 \\
& \downarrow & & \downarrow & & \downarrow \\
& 0 & 0 & 0 &
\end{array}
$$

By Lemma III.5.1 (the Snake Lemma), the sequence at the top and the sequence at the bottom are exact. Thus, by Lemma 2.2 (which relates $H_n$ to $\operatorname{coker} \partial_{n+1}$ and $\ker \partial_{n-1}$), we obtain the diagram

$$
\begin{array}{cccccc}
H_n(A) & \longrightarrow & H_n(B) & \longrightarrow & H_n(C) \\
\downarrow & & \downarrow & & \downarrow \\
\operatorname{coker} \partial_{n+1}^A & \longrightarrow & \operatorname{coker} \partial_{n+1}^B & \longrightarrow & \operatorname{coker} \partial_{n+1}^C & \longrightarrow 0 \\
\downarrow & & \downarrow & & \downarrow \\
0 \longrightarrow & \ker \partial_{n-1}^A & \longrightarrow & \ker \partial_{n-1}^B & \longrightarrow & \ker \partial_{n-1}^C \\
\downarrow & & \downarrow & & \downarrow \\
H_{n-1}(A) & \longrightarrow & H_{n-1}(B) & \longrightarrow & H_{n-1}(C)
\end{array}
$$

Applying Lemma III.5.1 (the Snake Lemma) again, we deduce the existence of a connecting morphism

$$\omega_n : H_n(C) \to H_{n-1}(A)$$

such that the long sequence

$$\cdots \xrightarrow{\omega_{n+1}} H_n(A) \xrightarrow{\varphi_n} H_n(B) \xrightarrow{\psi_n} H_n(C) \xrightarrow{\omega_n} H_{n-1}(A) \xrightarrow{\varphi_{n-1}} \cdots \tag{2.1}$$

is exact.

Explicitly, $\omega_n$ is defined as follows. Let $c \in C_n$ be a cycle representing a homology class $[c] \in H_n(C)$. Since $\psi_n$ is surjective, there exists $b \in B_n$ with $\psi_n(b) = c$. Then $\psi_{n-1}(\partial_n^B(b)) = \partial_n^C(\psi_n(b)) = \partial_n^C(c) = 0$, so by exactness of the middle row, $\partial_n^B(b) = \varphi_{n-1}(a)$ for some $a \in A_{n-1}$. Moreover, $\varphi_{n-2}(\partial_{n-1}^A(a)) = \partial_{n-1}^B(\varphi_{n-1}(a)) = \partial_{n-1}^B(\partial_n^B(b)) = 0$, and since $\varphi_{n-2}$ is injective, $a$ is a cycle. One verifies that $[a] \in H_{n-1}(A)$ is independent of the choices made, and we set $\omega_n([c]) = [a]$.

The long exact sequence is natural: given a commutative diagram of short exact sequences of chain complexes

$$
\begin{array}{cccccc}
A & \longrightarrow & B & \longrightarrow & C \\
\downarrow & & \downarrow & & \downarrow \\
A' & \longrightarrow & B' & \longrightarrow & C'
\end{array}
$$

with exact rows, the homology sequence (2.1) is mapped into the homology sequence arising from $A' \to B' \to C'$ in such a way that the resulting diagram is commutative. $\square$
