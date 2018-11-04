def are_overlapping(A, B):
  return A[1] >= B[0] and B[1] >= A[0]

print(are_overlapping((1,5),(2,6)))