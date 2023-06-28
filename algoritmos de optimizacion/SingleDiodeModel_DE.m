function [y,iter]= SingleDiodeModel_DE(n,x,CON,Fn,stop)
   [r,~]=size(x);
    F = 0.1;
    CR= 0.2;
    n = 40;  %poblacion
    D = 2;   %individuo
    %%
    NFES=10000;
    If=1e19;
    G(1:2) = If; Gval = If;
    %% Poblacion inicial 
    X = x;
    out=0;
    minimo=zeros(1,NFES);
    for i=1:NFES
    V = mutationDE(X, F, n);
    U=RecombiDE(X,V,D,n,CR);
    RMSE=Fn(X');
    RMSE2=Fn(U');
     if Gval>min(RMSE)
    [Gval,k]=min(RMSE); %minimo global
     G=X(k,:);
      out=0;
    else
        out=out+1;
    end
    if out==stop 
        break; 
    end
    minimo(i) = Gval;
    X=seleccion(X,U,RMSE,RMSE2);
    X=limit(X,repmat(CON(:,1)',r,1),repmat(CON(:,2)',r,1));
    end
 minimo(i:end)=Gval;
iter=i;
x1 = G(1);
y1 = G(2);
y = cat(1,x1,y1,minimo');
end
function V=mutationDE(X, F, N)
     V = zeros(size(X));
    M = randi(N, N, 2);
    for i = 1 : N
        j = M(i,1);
        k = M(i,2);
        while (i==k), k = randi(N,1,1); end %%avoiding repetitiobs
        V(i,:) = X(i,:) + F*(X(j,:) - X(k,:));
    end
   
end
function U=RecombiDE(X,V,D,N,Cr)
X=X';
LG1=(rand(D,N)<=Cr);
LG2=(randi(D,D,N)==(1:D)'*ones(1,N));
LG=(LG1|LG2);
U=(LG).*V'+(~LG).*X;
U=U';
end
function S=seleccion(X,U,RMSE,RMSE2)
    LG=RMSE<RMSE2;
    S=LG'.*X+(~LG)'.*U;
    
end
