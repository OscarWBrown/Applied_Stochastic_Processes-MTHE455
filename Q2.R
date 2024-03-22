collectCoupons<-function(n){
  
  coupons <- array(1:n)
  collectedCoupons <- array(0, n)
  T = 0
  
  while(sum(collectedCoupons != 0) != n){
  
      curr = sample(coupons, 1)
    collectedCoupons[curr] = collectedCoupons[curr] + 1
    T = T+1
    max = max(collectedCoupons)
  
  }
  
  return (c(T, max))

}

N = c(10, 20);
R = 10^5;

for (n in N){
  
  res = matrix(0,R,2)
  for(r in 1:R){ 
    res[r,] = collectCoupons(n)
  }
  
  # report E[T]
  cat('# coupons=',n, '\nExp. Coupons',  mean(res[,1]),' Standard dev.', sd(res[,1]), '\n')
  
  #report E[X]
  cat('Exp. Max of 1 type', mean(res[,2]),' Standard dev.', sd(res[,2]), '\n')
  
}
  
