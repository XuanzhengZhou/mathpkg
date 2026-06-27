---
role: proof
locale: en
of_concept: submartingale-decomposition
source_book: gtm046
source_chapter: "X"
source_section: "32"
---

The decomposition of a submartingale into a martingale plus an increasing process is due to Doob. There are two cases considered.

**1. Submartingale sequence \(X_1, X_2, \ldots\) with \(\sup E|X_n| < \infty\).**

Define the increasing process (the "compensator") by

$$
A_1 = 0, \quad A_n = \sum_{k=1}^{n-1} E(X_{k+1} - X_k \mid \mathcal{B}_k), \quad n \geq 2.
$$

Since \(X_n\) is a submartingale, \(E(X_{k+1} \mid \mathcal{B}_k) \geq X_k\), so each increment \(E(X_{k+1} - X_k \mid \mathcal{B}_k) \geq 0\). Hence \(0 \leq A_n \uparrow\).

Define \(M_n = X_n - A_n\). Then \(M_n\) is \(\mathcal{B}_n\)-measurable, and

$$
E(M_{n+1} \mid \mathcal{B}_n) = E(X_{n+1} \mid \mathcal{B}_n) - A_{n+1} = E(X_{n+1} \mid \mathcal{B}_n) - A_n - E(X_{n+1} - X_n \mid \mathcal{B}_n)
$$
$$
= X_n + (E(X_{n+1} \mid \mathcal{B}_n) - X_n) - A_n - (E(X_{n+1} \mid \mathcal{B}_n) - X_n) = X_n - A_n = M_n.
$$

Thus \(M_n\) is a martingale. Since \(\sup E|X_n| < \infty\) and \(A_n \geq 0\) a.s., we have \(E A_n = EX_n - EM_n = EX_n - EX_1 \leq 2 \sup E|X_n| < \infty\). Hence \(A_n \uparrow A\) with \(A\) finite a.s. by the monotone convergence theorem. Therefore \(X_n = M_n + A_n\) with \(M_n\) a martingale and \(0 \leq A_n \uparrow A\) finite a.s.

The alternate decomposition \(X_n = X'_n + X''_n\) where \(X'_n\) is a martingale with \(\sup E|X'_n| < \infty\) and \(0 \leq X''_n \uparrow X''\) finite a.s. follows by the same construction with appropriate centering.

**2. Submartingale reversed sequence \(\cdots, X_2, X_1\).**

For a reversed submartingale, define

$$
B_n = \sum_{k=n}^{\infty} E(X_k - X_{k+1} \mid \mathcal{B}_{k+1}),
$$

where the terms are nonnegative since \(E(X_k \mid \mathcal{B}_{k+1}) \geq X_{k+1}\) in the reversed filtration. The sum converges a.s. because \(E B_1 = EX_1 - \lim EX_n < \infty\) (using \(\sup E|X_1| < \infty\) and \(\lim EX_n > -\infty\)). Then \(M_n = X_n - B_n\) is a reversed martingale, and \(B_n\) decreases as \(n\) decreases (i.e., increases as we go backward in the sequence). This yields the decomposition \(X_n = X'_n + X''_n\) where \(X'_n\) is a reversed martingale and \(X''_n\) is an a.s. convergent increasing sequence.
