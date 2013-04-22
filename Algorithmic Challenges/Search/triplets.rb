def find_triplets
	array = []
	triplets = []

	ARGV.each do |num|
		array << num.chomp.to_i
	end

	array.each_with_index do |first, i|
		array.each_with_index do |second, j|
			if j <= i
				next
			end
			array.each_with_index do |third, k|
				if k <= j
					next
				end
				
				if i < j && j < k
					if first < second && second < third
						triplets.push [first,second,third]
					end
				end
			end
		end
	end
	puts triplets.uniq.size
end

find_triplets