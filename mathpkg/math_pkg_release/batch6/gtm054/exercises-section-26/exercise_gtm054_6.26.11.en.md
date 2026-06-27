---
role: exercise
locale: en
chapter: "6"
section: "26"
exercise_number: 11
---

Let $L$ be a $\{0, 1\}$-matrix and let $n$ be the largest number of 1's in any line. Prove that $L$ is a submatrix of a $\{0, 1\}$-matrix each of whose lines contains exactly $n$ 1's.

VF Enumerative Considerations

The results in the first four sections of this chapter have been largely concerned with questions of existence—existence of matchings, of LDR's, of sets of lines in matrices with given properties, and so forth. Here in the final section of the chapter, we consider questions of the form, “Given existence, how many are there?” The flavor is reminiscent of §IC, but the earlier sections of this chapter permit extension again of our numerical answers to a wide variety of superficially dissimilar models.

Let $M = [m_{ij}]$ be an $r \times s$ matrix over some integral domain. If $r \leq s$, the permanent of $M$ is given by

$$\text{perm}(M) = \sum_{\

Before the next theorem, due to Marshall Hall, it may be well to stand off for a moment and consider the logical relationships among the results of Chapters IV, V, and VI. The Max-Flow–Min-Cut Theorem was proved in Chapter IV essentially from first principles developed in Chapters I, II, and III. From it we deduced the Main Matching Theorem, one of whose corollaries (A6) has been demonstrated (§C, §D, §E) to be equivalent to various other results, notably the Philip Hall Theorem. The Main Matching Theorem can straightforwardly be shown to imply the Max-Flow–Min-Cut Theorem. Looking ahead to Chapter VI, we anticipate proving the equivalence between the Max-Flow–Min-Cut Theorem and the Menger Theorem for separation in graphs. Marshall Hall’s theorem below is totally independent of this logical chain. It will be proved from first principles; yet it yields the Philip Hall Theorem as a trivial corollary. Marshall Hall’s theorem, therefore, might have been used as our logical starting point rather than Max-Flow–Min-Cut. The choice of a starting point for this presentation is very much a matter of taste.
