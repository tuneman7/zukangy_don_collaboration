# zukangy_don_collaboration   

To pull down and run final project:

This will not work on an ARM / M1 / M2 box as the images are for the X86 architecture.


Get on your AWS linux box, then run the following command (it will prompt you for your credentials on that box).

```

git clone https://github.com/tuneman7/zukangy_don_collaboration && cd ./zukangy_don_collaboration/ && . run205final.sh

```

Alternatively -- you can execute each of the commands independently.

```
git clone https://github.com/tuneman7/zukangy_don_collaboration
```

```
cd ./zukangy_don_collaboration/
```

```
. run205final.sh
```

```
sudo su
apt update && apt install docker -y && apt install docker-compose -y && apt install git -y && apt install python-is-python3 -y
```
