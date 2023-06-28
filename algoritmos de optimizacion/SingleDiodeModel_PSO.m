function [y,iter] = SingleDiodeModel_PSO(Npar,X,v,CON,vmax,Fn,stop)
NFES = 10000;
x=X;
c1 = 2;
c2 = 2;
If=1e19;
[r,m]=size(x);
G(1:m) = If; Gval = If;
P= If*ones(r,m); Pval= If*ones(1,Npar);
out=0; 
% TRADITIONAL PSO: OPTIMIZATION (Iph,Io,Rs,Rsh,n)
minimo=zeros(1,NFES);
for i=1:NFES
    RMSE=Fn(x'); 
    [Pval,P]=CheckError(RMSE,Pval,P,x,m);
    if Gval>min(RMSE)
    [Gval,k]=min(RMSE);
    G=x(k,:);
    out=0;
    else
        out=out+1;
    end
    if out==stop 
        break; 
    end
    minimo(i) = Gval;
    % Updating positions and velocities
   [x,v]=PosVel(x,v,c1,c2,r,P,G);
    x=limit(x,repmat(CON(:,1)',r,1),repmat(CON(:,2)',r,1));%Delimitar la funcion
    v=limit(v,-vmax*ones(size(v)),vmax*ones(size(v)));
end
% OUTPUTS
minimo(i:end)=Gval;
iter=i;
x1 = G(1);
y1 = G(2);
y = cat(1,x1,y1,minimo');
end
function [X,V]=PosVel(x,v,c1,c2,r,P,G)
    C1=c1*rand(size(x));
    C2=c2*rand(size(x));
    V=v + C1.*(P - x) + C2.*(repmat(G,r,1) - x);
    X=x+V;
end