force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    alias grep='grep --color=auto'
fi

if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

# Aliases:
alias act='source ~/env/bin/activate'
alias c='clear'
alias copy='xclip -selection clipboard <'
alias clear_recents='rm ~/.local/share/recently-used.xbel'
alias deact='deactivate'
alias dock='sudo docker start jmp && sudo docker exec -it jmp /bin/bash'
alias e='exit'
alias fd='fdfind'
alias fox='python3 ~/Github/personal-peccadillos/Python/fox.py'
alias gitpull='/home/jpell/Github/gitpull.sh'
alias gitpush='/home/jpell/Github/gitpush.sh'
alias ip='ifconfig'
alias ipscan='sudo arp-scan --localnet'
alias mac='ssh joepellegrino@192.168.1.4'
alias publicip='curl ifconfig.me'
alias shred='shred -zvu -n 1'
alias size='du -sh'
alias sus='sudo systemctl suspend'
alias tr='trans -b'
type='file --mime-type -b'
alias video_res='ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0'
alias rs='rsync -ah --progress'
