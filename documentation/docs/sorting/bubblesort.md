# Bubble Sort

The basic idea of Bubble Sort is to swap the values of two elements, `A[i]` and `A[i+1]`. For this, we need an `aux` variable to temporarily store the value of `A[i]`, so we can move the larger value to the last position in the array.

We use two loops: the inner loop is responsible for comparing and swapping values, and the outer loop ensures that we repeat this operation for the number of elements in the array.

<div align="center">
```mermaid
flowchart TD 
    BS("Start") --> I@{ shape: notch-pent, label: "I > N-1" }
    I -->J@{ shape: notch-pent, label: "J > N-1" }
    I -->|Done| E@{ shape: circle, label: "End"}
    J -->|Done| I
    J --> if@{ shape: diamond, label: "X[J] > X[J+1]"}
    if -->|Yes| B["AUX = X[J]<br /> X[J] = X[J+1]<br />X[J+1]=AUX"]
    if -->|No| E2@{ shape: circle, label: "End"}
    B -->E2
```
</div>
