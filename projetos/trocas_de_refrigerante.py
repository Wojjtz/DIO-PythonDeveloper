def garrafas(N, K):
  
  trocas = N // K
  sobra = N % K
  num_garrafas = trocas + sobra
    
  return int(num_garrafas)
  
T = int(input())
for i in range(T):
    
  N, K = map(int, input().split())
  
  print(garrafas(N, K))