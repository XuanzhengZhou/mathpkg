---
role: proof
locale: en
of_concept: distribution-action-via-fourier-coefficients
source_book: gtm012
source_chapter: "5"
source_section: "§1. Fourier series of smooth periodic functions and of periodic distributions"
---

# Proof of Action of Periodic Distribution Expressed via Fourier Coefficients

**Theorem 1.3.** Suppose $F \in \mathcal{P}'$ has $(a_n)_{-\infty}^{\infty}$ as its sequence of Fourier coefficients, and suppose $u \in \mathcal{P}$ has $(b_n)_{-\infty}^{\infty}$ as its sequence of Fourier coefficients. Then

$$F(u) = \sum_{-\infty}^{\infty} a_n b_{-n} = \sum_{-\infty}^{\infty} a_{-n} b_n.$$

*Proof.* Let

$$u_N(x) = \sum_{n=-N}^{N} b_n \exp(inx)$$

be the $N$-th partial sum of the Fourier series of $u$. By Theorem 1.1 (or the general theory of Fourier series of smooth periodic functions), we have

$$u_N \to u \quad \text{in } \mathcal{P}.$$

Since $F \in \mathcal{P}'$ is a continuous linear functional on $\mathcal{P}$, it follows that

$$F(u) = \lim_{N \to \infty} F(u_N).$$

Now compute $F(u_N)$ using linearity:

$$F(u_N) = F\left(\sum_{n=-N}^{N} b_n e_n\right) = \sum_{n=-N}^{N} b_n F(e_n).$$

Recall from definition (3) that the Fourier coefficients of $F$ are given by

$$a_n = F(e_{-n}), \qquad e_{-n}(x) = \exp(-inx).$$

Replacing $n$ by $-n$ in this definition, we obtain

$$F(e_n) = a_{-n}.$$

Substituting this into the expression for $F(u_N)$ yields

$$F(u_N) = \sum_{n=-N}^{N} b_n a_{-n}.$$

Taking the limit as $N \to \infty$, we get

$$F(u) = \lim_{N \to \infty} \sum_{n=-N}^{N} a_{-n} b_n = \sum_{n=-\infty}^{\infty} a_{-n} b_n.$$

By re-indexing the sum (replacing $n$ by $-n$), we also have

$$\sum_{n=-\infty}^{\infty} a_{-n} b_n = \sum_{n=-\infty}^{\infty} a_n b_{-n}.$$

This completes the proof. $\square$

**Remark.** This theorem shows that the action of any periodic distribution on any smooth periodic function can be expressed purely in terms of their Fourier coefficient sequences. In particular, if we write the Fourier series formally as

$$u \sim \sum b_n e^{inx}, \qquad F \sim \sum a_n e^{inx},$$

then the pairing $\langle F, u \rangle = F(u)$ corresponds to the formal sum $\sum a_n b_{-n}$, which resembles the $L^2$ inner product with conjugation on one factor.
