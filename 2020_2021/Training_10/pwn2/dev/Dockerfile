FROM ubuntu

RUN dpkg --add-architecture i386
RUN apt-get update
RUN apt-get install -y socat
RUN apt-get install -y libc6:i386 libncurses5:i386 libstdc++6:i386
RUN useradd -d /home/ctf/ -m -p ctf -s /bin/bash ctf
RUN echo "ctf:ctf" | chpasswd

WORKDIR /home/ctf

COPY pwn2 .
COPY flag .

RUN chown -R root:root /home/ctf

USER ctf
EXPOSE 13337
CMD socat -dd TCP4-LISTEN:13337,fork,reuseaddr EXEC:./pwn2,pty,echo=0,raw,iexten=0
