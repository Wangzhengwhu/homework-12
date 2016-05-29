import math
import matplotlib.pyplot as plt
import numpy as np
 ###
 GM_s=4*pi*pi
 GM_J=1.9/2000.0*GM_s
 dt=0.005
 end_t=100
 ###
 x_J=[]
 v_x_J=[]
 y_J=[]
 v_y_J=[]
 x_a=[]
 v_x_a=[]
 y_a=[]
 v_y_a=[]
 t=[0]
 ###
 for i in range(int(end_t/dt)):
     v_x_J.append(v_x_J[i]-GM_s*x_J[i]*dt/((x_J[i]**2+y_J[i]**2)**(3.0/2.0)))
     x_J.append(x_J[i]+v_x_J[i+1]*dt)
     v_y_J.append(v_y_J[i]-GM_s*y_J[i]*dt/((x_J[i]**2+y_J[i]**2)**(3.0/2.0)))
     y_J.append(y_J[i]+v_y_J[i+1]*dt)
     v_x_a.append(v_x_a[i]-GM_s*x_a[i]*dt/((x_a[i]**2+y_a[i]**2)**(3.0/2.0))+GM_J*(x_J[i]-x_a[i])*dt/(((x_a[i]-x_J[i])**2+(y_a[i]-y_J[i])**2)**(3.0/2.0)))
     x_a.append(x_a[i]+v_x_a[i+1]*dt)
     v_y_a.append(v_y_a[i]-GM_s*y_a[i]*dt/((x_a[i]**2+y_a[i]**2)**(3.0/2.0))+GM_J*(y_J[i]-y_a[i])*dt/(((x_a[i]-x_J[i])**2+(y_a[i]-y_J[i])**2)**(3.0/2.0)))
     y_a.append(y_a[i]+v_y_a[i+1]*dt)
###
plt.plot(x_a,y_a,'--' ,label='asteroid,$m_a/M_s=,gap:1/2$')
plt.title(u'the orbit of asteroid',fontsize=14)
plt.xlabel(u'x/AU',fontsize=14)
plt.ylabel(u'y/AU',fontsize=14)
plt.legend(fontsize=12,loc='best')
plt.show()