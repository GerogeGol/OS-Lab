swapfile=$1
new_swap_size=$2

if [ $# -eq 0 ]; then
    echo "No arguments"
    exit
fi

if [ -z "$1" ]; then
    echo "No swapfile name"
    exit
fi

if [ -z "$2" ]; then
    echo "No swapfile size"
    exit
fi


swapoff $swapfile

dd if=/dev/zero of=$swapfile bs=1M count=$new_swap_size status=progress

chmod 600 $swapfile

mkswap $swapfile

swapon $swapfile