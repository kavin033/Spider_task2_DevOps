# Spider_task2_DevOps


``cd /home``  
``git clone https://github.com/kavin033/Spider_task2_DevOps.git``  
``cd /Spider_task2_DevOps``  
``cp your_domain.conf /etc/apache2/sites-available/.``  
``cp hosts /etc/hosts``  

``sudo a2enmod proxy``   
``sudo a2enmod proxy_http``    
``sudo a2enmod proxy_balancer``  
``sudo a2enmod lbmethod_byrequests``  
``sudo service apache2 restart`` 

search ''http://ecorpcredit/customers'' and ''http://ecorpcredit/headquarters'' on web
