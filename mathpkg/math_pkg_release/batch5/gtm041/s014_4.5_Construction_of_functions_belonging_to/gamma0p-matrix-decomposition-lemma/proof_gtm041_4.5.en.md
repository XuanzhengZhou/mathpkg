---
role: proof
locale: en
of_concept: gamma0p-matrix-decomposition-lemma
source_book: gtm041
source_chapter: "4"
source_section: "4.5"
---

*Proof.* Write the matrix representations in $\mathrm{SL}(2, \mathbb{Z})$:

$$
T_\lambda = \begin{pmatrix} 1 & \lambda \\ 0 & p \end{pmatrix}, \qquad
V = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \Gamma_0(p),
$$

so $ad - bc = 1$ and $p \mid c$. We seek

$$
W_\mu = \begin{pmatrix} A & B \\ C & D \end{pmatrix} \in \Gamma_0(p^2)
$$

(meaning $AD - BC = 1$ and $p^2 \mid C$) and an integer $\mu$ with $0 \leq \mu \leq p-1$ such that $T_\lambda V = W_\mu T_\mu$.

Expanding both sides,

$$
\begin{pmatrix} 1 & \lambda \\ 0 & p \end{pmatrix}
\begin{pmatrix} a & b \\ c & d \end{pmatrix}
=
\begin{pmatrix} A & B \\ C & D \end{pmatrix}
\begin{pmatrix} 1 & \mu \\ 0 & p \end{pmatrix},
$$

which gives the matrix equality

$$
\begin{pmatrix} a + \lambda c & b + \lambda d \\ pc & pd \end{pmatrix}
=
\begin{pmatrix} A & A\mu + Bp \\ C & C\mu + Dp \end{pmatrix}.
$$

Equating entries, we must satisfy

$$
\begin{cases}
A = a + \lambda c, \\[4pt]
C = pc,
\end{cases}
\qquad
\begin{cases}
A\mu + Bp = b + \lambda d, \\[4pt]
C\mu + Dp = pd,
\end{cases}
$$

with the conditions $C \equiv 0 \pmod{p^2}$ and $AD - BC = 1$ for membership in $\Gamma_0(p^2)$.

The relations $A = a + \lambda c$ and $C = pc$ are determined uniquely. Since $p \mid c$ (because $V \in \Gamma_0(p)$), we have $p^2 \mid pc = C$, so $C \equiv 0 \pmod{p^2}$ holds automatically.

Substituting $A$ and $C$ into the remaining equations yields

$$
\begin{cases}
(a + \lambda c)\mu + Bp = b + \lambda d, \\[4pt]
cp\mu + Dp = pd.
\end{cases}
$$

From the second equation, $Dp = pd - cp\mu = p(d - c\mu)$, hence $D = d - c\mu$.

For the first equation, observe that it is equivalent to

$$
Bp = b + \lambda d - (a + \lambda c)\mu.
$$

We choose $\mu$ to be the unique solution of the congruence

$$
\mu a \equiv b + \lambda d \pmod{p}
$$

lying in the interval $0 \leq \mu \leq p-1$. This is possible because $ad - bc = 1$ and $p \mid c$ together imply $p \nmid a$, so $a$ is invertible modulo $p$.

With this choice of $\mu$, the integer $b + \lambda d - (a + \lambda c)\mu$ is divisible by $p$ (since it is $b + \lambda d - \mu a - \mu\lambda c \equiv 0 \pmod{p}$, noting $\mu\lambda c \equiv 0 \pmod{p}$ because $p \mid c$). Hence $B$ is an integer.

It remains to verify $AD - BC = 1$. Computing,

$$
\begin{aligned}
AD - BC &= (a + \lambda c)(d - c\mu) - B \cdot pc \\
&= ad - ac\mu + \lambda cd - \lambda c^2\mu - Bpc.
\end{aligned}
$$

Using the relation $Bp = b + \lambda d - (a + \lambda c)\mu$, we substitute $Bpc = c(b + \lambda d - (a + \lambda c)\mu)$ and expand. After simplification using $ad - bc = 1$, the determinant reduces to $1$. Thus $W_\mu \in \Gamma_0(p^2)$.

Finally, if $\lambda_1 \not\equiv \lambda_2 \pmod{p}$ give the same $\mu$, then from the congruence $\mu a \equiv b + \lambda d \pmod{p}$ we would obtain $\lambda_1 d \equiv \lambda_2 d \pmod{p}$. Since $p \nmid d$ (otherwise $p \mid ad - bc = 1$), this forces $\lambda_1 \equiv \lambda_2 \pmod{p}$, a contradiction. Hence distinct $\lambda$ modulo $p$ yield distinct $\mu$ modulo $p$, so $\mu$ also runs through a complete residue system modulo $p$. ∎
