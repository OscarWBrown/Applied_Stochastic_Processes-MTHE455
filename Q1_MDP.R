P_super1 = matrix(c(1/2,1/4,1/4,
                    1/4,1/2,1/4,
                    1/4,1/4,1/2), nrow = 3, byrow = T)

P_super2 = matrix(rep(1/3,9), nrow = 3, byrow = T)

gamma = 0.8

#define the policy function
policy_mu <- function(s){
  if(s == 1){
    u = 1
  }else if(s == 2){
    u = 2
  }else{
    u = 1
  }
  return(u)
}

#define the cost function
cost_c <- function(s,u){
  return(s*u)
}


#find C and P_mu
C = matrix(0, nrow =3, ncol = 1)
for(s in c(1:3)){
  C[s] = cost_c(s, policy_mu(s))
}

P_mu = matrix(0, nrow = 3, ncol = 3)
for(i in c(1:3)){
  for(j in c(1:3)){
    u = policy_mu(i)
    if(u == 1){
      P_mu[i,j] = P_super1[i,j]
    }else{
      P_mu[i,j] = P_super2[i,j]
    }
  }
}

#solve the equation J = C + gamma*P*J
C
P_mu
solve(diag(3) - gamma * P_mu) %*% C

