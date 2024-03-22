oneRun <- function(p,init_val){
  
  T = 0
  Money = init_val
  Max = Money
  
  while (Money > 0) {
    
    Money = Money + (2*rbinom(1,1,p)-1)
    
    if (Money > Max) {
      
      Max = Money
    
    }
    
    T = T + 1
  
  }
  
  return(c(T,Max))
}

caset.seed(19)
R =  10^5
p_vals = c(0.4, 0.45, 0.48)
init_val = 5

for(p in p_vals){
  
  res = matrix(0,R,2)
  
  for(r in 1:R){ 
  
    res[r,] = oneRun(p,init_val)
  
  }
  
  # report E[T], sd[T]
  cat('p=',p, '\nExp. Bets',  mean(res[,1]),' Standard dev.', sd(res[,1]), '\n')
  
  #report E[1(X_T == 0)], sd[1(X_T == 0]
  cat('Exp. Max', mean(c(res[,2])),' Standard dev.' , sd(res[,2]), '\n')
  
  # P(Max>=10)
  P = sum(res[,2] >= 10)/R
  cat('P(Max=>10)', P,'\n\n')

}

