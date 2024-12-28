# Linux Commands

```
# Devices
lspci

# Disk usage
df -h
df -T
df -i

# check file info
ls -l $path
ls -i $path
stat $path

# check usage by directory
du -h --max-depth=1 $path
du -sh $path/*

# find file
find $path -name $file_name
find $path -size +100M

# Disk
iostat
hdparm -t /dev/sda
smartctl -a /dev/sda

# CPU
cat /proc/cpuinfo
cat /proc/cpuinfo| grep "physical id"
cat /proc/cpuinfo| grep "cpu cores"
cat /proc/cpuinfo| grep "processor" 

# Memory
cat /proc/meminfo
free -m

# Resource
vmstat
htop
top
top -H -p $pid
echo 'obase=16;$pid'|bc

# Process
ps aux
ps -T -p $pid
ps -T -p $pid

# Crontab
crontab -l
crontab -e
tail -f /var/log/cron

# Network
ifconfig
ip route get 1

# check process and port
netstat -tnlp|grep $pid
netstat -tnlp|grep $port
lsof -i:$port
netstat -nat|grep $port

# tcpdump
tcpdump -i eth1 tcp port $port -Xxv

# tar
tar cvf $tar_name.tar $dir_name
tar cvf $tar_name.tar $dir_name --exclude $exclude_file --exclude $exclude_dir
tar cvf $tar_name.tar $dir_name --exclude $dir_name/$exclude_name
gzip $tar_name.tar
tar xvf $tar_name.tar
tar xvf $tar_name.tar.gz

# zip
zip -r $zip_name.zip $dir_name
unzip $zip_name.zip

# shell
echo $SHELL
cat /etc/shells
chsh -s /bin/zsh

# check current users
w

# switch user
su - $user -c 'whoami'

# command
whereis $cmd
which $cmd
history

# system limit
ulimit -a

# run cmd in background
nohup $cmd $arg 1>output.log 2>&1 &

# copy
cp -R /source /target
rsync -rv --progress /source /target
```
