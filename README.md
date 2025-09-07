exploit usage:
  proxychains python3 spip_exploit.py -u http://web.prob.local

suggested privesc path:
  step 1: establishing ssh session with user auditor /
  step 2: creating a folder and creating 2 files privesc.c and privesc.py /
  step 3: inside the folder, run sudo pip install . /
  step 4: running the executable privesc
