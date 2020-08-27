NotNotFlag=(s l L e H s A e S T O N s L L e h S s l l e s E H S)
NotFlag=(g a l f e k a f y l e t u l o s b a e t u l o s b a)

for i in ${!NotNotFlag[@]};do
	echo ${NotNotFlag[$i]};
	echo ${NotFlag[$i]};
	sleep 0.2
done

