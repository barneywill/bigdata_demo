# Linux Commands

## Resource: CPU, Memory, Disk, Network
```
# System Resource
vmstat
htop
top
top -H -p $pid
echo 'obase=16;$pid'|bc

# check system version
uname -a
cat /proc/version

# Devices
lspci

# CPU
cat /proc/cpuinfo
cat /proc/cpuinfo| grep "physical id"
cat /proc/cpuinfo| grep "cpu cores"
cat /proc/cpuinfo| grep "processor" 

# Memory
cat /proc/meminfo
free -m

# Disk
iostat
hdparm -t /dev/sda
smartctl -a /dev/sda

# Disk usage
df -h
df -T
df -i

# Network
ifconfig
ip route get 1
tcpdump -i eth1 tcp port $port -Xxv
```

## Directory, File, tar, zip
```
# check usage by directory
du -h --max-depth=1 $path
du -sh $path/*

# find file
find $path -name $file_name
find $path -size +100M

# check file info
ls -l $path
ls -i $path
stat $path

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
```

## Internet: curl, wget, ping, nc
```
# see http request and response
curl -v https://www.google.com

# download
wget $url

# test host connectivity
ping www.google.com
nslookup www.baidu.com

# test ip connectivity
ping 220.181.112.244
traceroute 220.181.112.244

# test port connectivity
telnet 220.181.112.244 80
nc 220.181.112.244 80 -v
curl http://220.181.112.244:80 -v
```

## Process, Thread
```
# Process
ps aux
ps -T -p $pid
ps -T -p $pid

# check process and port
netstat -tnlp|grep $pid
netstat -tnlp|grep $port
lsof -i:$port
netstat -nat|grep $port
```

## Crontab
```
# Crontab
crontab -l
crontab -e
tail -f /var/log/cron
```

## User, Group
```
# add and delete user
useradd $user
userdel $user

# add and delete group
groupdel $group
groupadd $group

# set new password for a user
passwd $user

# change user's home directory
usermod -d /path/to/home $user

# see user info and his group
id $user

# see group members
groupmems -g $group -l
grep $group /etc/group

# add a user to a group
usermod -G $group $user
groupmems -g $group -a $user

# remove a user from a group
groupmems -g $group -d $user

```

# Mount Disk
```
# show all disks and partitions
fdisk -l

# create a partition
fdisk /dev/sdb

# create file system
mkfs.xfs -f /dev/sda1

# check file system
parted -l
file -s /dev/sda1
df -T

# mount a partition to a directory
mkdir /test
mount /dev/sda1 /test

# show uuid
ls /dev/disk/by-uuid/

# mount by config
vi /etc/fstab
```

# Other
```
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

# copy remotely
scp /local_dir/filename user@server_ip:/remote/path
scp user@server_ip:/remote/path/filename /local_dir
```

# session
```
# list all sessions
screen -list

# create a new session
screen -S $session_name

# detach current session
Ctrl+A d

# kill current session
Ctrl+A k

# re-enter a session
screen -r $session_name

# detach a session by force
screen -d $session_name
```

# tmux
## tmux session
```
# list all session
tmux ls

# create a new session
tmux new -s myname

# kill current session
Ctrl+d or exit

# detach current session
Ctrl+b d or tmux detach

# re-enter a session
tmux a -t myname
tmux attach -t myname 

# kill a session by force
tmux kill-session -t myname

# rename a session
tmux rename -t myname1 myname2

# show all session
Ctrl+b s

# switch to another session
tmux switch -t myname 

# rename current session
Ctrl+b $
```

## tmux window
```
# create a new window
Ctrl+b c

# move focus to the next window
Ctrl+b n

# move focus to the previous window
Ctrl+b p

# move focus to selected window
Ctrl+b 0-9

# rename current window
Ctrl+b ,

# show all windows
Ctrl+b w

# close current window
Ctrl+b &
```

## tmux pane
```
# split pane vertically
Ctrl+b %
tmux split-window

# split pane horizonally
Ctrl+b "
tmux split-window -h

# show numbers of each pane, and click the number to focus
Ctrl+b q

# move focus across panes
Ctrl+b Left|Right|Up|Down

tmux select-pane -L|R|U|D 

# move focus to the previous pane
Ctrl+b ;

# move focus to the next pane
Ctrl+b o

# close current pane
Ctrl+b x

# re-arrange all panes
Ctrl+b space

# change current pane to full screen, or change back
Ctrl+b z

# show time in current pane
Ctrl+b t

# anti-clockwize
Ctrl+b Ctrl+o

# resize current pane
tmux resize-pane -L|R|U|D

# page up or down mode
Ctrl+b PageUp|PageDown
# quit
q

# copy mode
Ctrl+b [
# quit
q
```