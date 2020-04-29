for file in *; do
	if [ -x $file ]; then
		echo "$file is executable"
	fi
done